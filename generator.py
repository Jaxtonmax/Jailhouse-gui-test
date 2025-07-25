"""
Jailhouse配置生成器模块。

本模块提供了用于生成Jailhouse虚拟机监控器配置的功能，包括:
- 根单元格(Root Cell)配置生成
- 客户单元格(Guest Cell)配置生成
- Linux设备树配置生成
- 资源表配置生成

主要类:
- JailhouseMemory: 内存区域配置类
- GeneratorCommon: 通用配置生成功能
- RootCellGenerator: 根单元格配置生成器
- GuestCellGenerator: 客户单元格配置生成器
"""

import logging
from typing import TypedDict, List, Optional
import ctypes
from mako.template import Template
from mako import exceptions
from jh_resource import Resource, ResourceGuestCell, ResourceCPU, ResourceGuestCellList, ResourcePCIDeviceList, ResourceRootCell
from jh_resource import ResourceComm, ARMArch
from jh_resource import ResourceMgr, PlatformMgr
from utils import get_template_path
import click
import fdt
import cellconfig
from cellconfig import Revision14
import json

logger = logging.getLogger("generator")


class JailhouseMemory:
    """
    Jailhouse内存区域配置类。
    
    定义了内存区域的物理地址、虚拟地址、大小和访问权限标志。
    
    属性:
        MEM_READ: 读权限
        MEM_WRITE: 写权限
        MEM_EXECUTE: 执行权限
        MEM_DMA: DMA访问权限
        MEM_IO: IO访问权限
        MEM_COMM_REGION: 通信区域标志
        MEM_LOADABLE: 可加载标志
        MEM_ROOTSHARED: 与根单元格共享标志
        MEM_NO_HUGEPAGES: 禁用大页标志
        MEM_IO_UNALIGNED: 允许非对齐IO访问
        MEM_IO_WIDTH_SHIFT: IO宽度位移值
        MEM_IO_8/16/32/64: IO访问宽度定义
        MEM_RESOURCE_TABLE: 资源表标志
    """
    MEM_READ           = 0x0001
    MEM_WRITE          = 0x0002
    MEM_EXECUTE        = 0x0004
    MEM_DMA            = 0x0008
    MEM_IO             = 0x0010
    MEM_COMM_REGION    = 0x0020
    MEM_LOADABLE       = 0x0040
    MEM_ROOTSHARED     = 0x0080
    MEM_NO_HUGEPAGES   = 0x0100
    MEM_IO_UNALIGNED   = 0x8000
    MEM_IO_WIDTH_SHIFT = 16
    MEM_IO_8           = (1 << 16)
    MEM_IO_16          = (2 << 16)
    MEM_IO_32          = (4 << 16)
    MEM_IO_64          = (8 << 16)
    MEM_RESOURCE_TABLE = 0x10000000

    def __init__(self, phys=0, virt=0, size=0, flag=0) -> None:
        self.phys = phys
        self.virt = virt
        self.size = size
        self.flag = flag


class GeneratorCommon(object):
    """
    配置生成器通用功能类。
    
    提供了生成Jailhouse配置时需要的通用功能。
    """
    
    @staticmethod
    def get_ivshmem(rsc: Resource, cell: Optional[ResourceGuestCell]=None ) -> Optional[dict]:
        """
        获取IVSHMEM(Inter-VM Shared Memory)配置。
        
        Args:
            rsc: 资源对象
            cell: 客户单元格对象，可选
            
        Returns:
            包含IVSHMEM配置信息的字典，包括:
            - 物理地址
            - 虚拟地址
            - 状态区大小
            - 读写区大小
            - 输出区大小
            - 单元格数量
            - 单元格ID
        """
        phys = rsc.jailhouse().ivshmem().ivshmem_phys()
        virt = phys
        cell_id = 0
        if cell is not None:
            virt = cell.ivshmem_virt_addr()
            cell_id = cell.my_index()+1
        return {
            "phys": phys,
            "virt": virt,
            "state_size": rsc.jailhouse().ivshmem().ivshmem_state_size(),
            "rw_size": rsc.jailhouse().ivshmem().ivshmem_rw_size(),
            "out_size": rsc.jailhouse().ivshmem().ivshmem_out_size(),
            "count": rsc.jailhouse().guestcells().cell_count() + 1,
            "id": cell_id
        }

    @staticmethod
    def get_gic_info(rsc: Resource) -> dict:
        return {
            "gic_version": rsc.platform().cpu().gic_version(),
            "gicd_base": rsc.platform().cpu().gicd_base(),
            "gicr_base": rsc.platform().cpu().gicr_base(),
            "gicc_base": rsc.platform().cpu().gicc_base(),
            "gich_base": rsc.platform().cpu().gich_base(),
            "gicv_base": rsc.platform().cpu().gicv_base(),
        }


class RootCellGenerator(object):
    """
    根单元格配置生成器。
    
    负责生成Jailhouse根单元格(Root Cell)的配置，包括:
    - 设备内存区域配置
    - GIC(Generic Interrupt Controller)配置
    - PCI设备配置
    - 调试控制台配置
    - 系统内存配置
    """
    
    def __init__(self) -> None:
        pass

    @classmethod
    def get_devices(cls, rsc: Resource) -> List:
        """
        获取设备内存区域列表。
        
        处理设备内存映射，包括:
        1. 获取所有设备的基本信息
        2. 按地址排序设备列表
        3. 合并相邻的设备内存区域
        4. 处理内存对齐要求
        
        Args:
            rsc: 资源对象
            
        Returns:
            包含设备信息的字典列表，每个字典包含:
            - name: 设备名称
            - addr: 设备基地址
            - size: 设备内存大小
        """
        devices = list()
        # 设备
        for dev in rsc.platform().cpu().devices():
            devices.append({"name": dev.name(), "addr": dev.addr(), "size": dev.size()})
        devices = sorted(devices, key=lambda x: x['addr'])

        def is_align(v):
            return (v & (4096-1)) == 0
        def be_align(v):
            return (v+4096-1) & (~(4096-1))

        # 合并
        merged_devices = list()
        temp = None
        for dev in devices:
            if is_align(dev['addr']) and is_align(dev['size']):
                if temp is not None:
                    if not is_align(temp['size']):
                        # XXX 强制4K对齐，非对齐时jailhouse可能报错
                        temp['size'] = be_align(temp['size'])
                    merged_devices.append(temp)
                    temp = None
                merged_devices.append(dev)
                continue

            if temp is None:
                temp = dev
                continue

            if temp['addr']+temp['size'] == dev['addr']:
                temp['name'] = temp['name'] + ',' + dev['name']
                temp['size'] = temp['size'] + dev['size']
            else:
                merged_devices.append(temp)
                temp = dev

        if temp is not None:
            merged_devices.append(temp)
            temp = None

        return merged_devices

    @classmethod
    def get_regions(cls, rsc: Resource) -> Optional[list]:
        """
        获取内存区域列表。
        
        获取系统中定义的内存区域信息，不包括DRAM区域。
        
        Args:
            rsc: 资源对象
            
        Returns:
            内存区域信息列表，每个元素包含:
            - name: 区域名称
            - addr: 区域基地址
            - size: 区域大小
        """
        regions: List[ResourceCPU.Region] = rsc.platform().cpu().regions()
        values = list()
        for region in regions:
            # 忽略dram空间，使用系统内存代替
            if region.type() is region.Type.DRAM:
                continue
            values.append({
                'name': region.name(),
                'addr': region.addr(),
                'size': region.size()
            })
        return values

    @classmethod
    def get_debug_console(cls, rsc: Resource) -> Optional[dict]:
        """
        获取调试控制台配置。
        
        查找并配置用于调试输出的串口设备。
        
        Args:
            rsc: 资源对象
            
        Returns:
            调试控制台配置字典，包含:
            - addr: 控制台设备地址
            - size: 设备内存大小
            - type: 设备类型
            如果未找到调试控制台则返回None
        """
        debug_console = rsc.jailhouse().rootcell().get_debug_console()
        if debug_console is None:
            return None

        for dev in rsc.platform().cpu().devices():
            if dev.name() == debug_console:
                type_value = cellconfig.jailhouse_con_type_form_str(dev.type())
                if type_value is None:
                    cls.logger.error("invalid consle device type.")
                    return False
                return {
                    "addr": dev.addr(),
                    "size": dev.size(),
                    "type": type_value
                }
        return False

    @classmethod
    def get_pci_mmconfig(cls, rsc: Resource) -> Optional[dict]:
        rootcell = rsc.jailhouse().rootcell()

        pci_mmconfig = rootcell.pci_mmconfig()
        end_bus = pci_mmconfig.bus_count - 1
        if end_bus < 0:
            end_bus = 1
        return {
            "base": pci_mmconfig.base_addr,
            "end_bus": end_bus,
            "pci_domain": pci_mmconfig.domain,
        }

    @classmethod
    def get_hypervisor(cls, rsc: Resource) -> dict:
        return {
            "addr": rsc.jailhouse().rootcell().hypervisor().addr(),
            "size": rsc.jailhouse().rootcell().hypervisor().size(),
        }

    @classmethod
    def get_root_pci_devices(cls, rsc: Resource) -> list:
        return list()

    @classmethod
    def get_board_mem(cls, rsc: Resource) -> Optional[List[dict]]:
        mems = list()
        for region in rsc.platform().board().ram_regions():
            mems.append({
                "name": "ram",
                "addr": region.addr(),
                "size": region.size()
            })
        return mems

    @classmethod
    def get_system(cls, rsc: Resource) -> Optional[dict]:
        cpu = rsc.platform().cpu()

        return {
            "cpu_name": cpu.name(),
        }

    @classmethod
    def get_cpu(cls, rsc: Resource) -> Optional[dict]:
        """
        通过board获取支持的CPU
        """
        cpus = rsc.platform().board().cpus()
        cpu_count = len(cpus)
        if cpu_count <= 0:
            logger.error("cpu count is 0")
            return None

        cpu_max = max(cpus)

        bitmap_count = cpu_max//64 + 1
        values = [0,]*bitmap_count
        for c in cpus:
            i = c//64
            values[i] = values[i] | (1<<(c%64))

        bitmap = list(map(lambda x: f"0x{x:016x}", values))

        return {
            "count": cpu_count,
            "cpus": list(cpus),
            "values": values,
            "bitmap": bitmap
        }

    @classmethod
    def gen_kwargs(cls, rsc: Resource) -> dict:
        rootcell = rsc.jailhouse().rootcell()

        name = rootcell.name()
        if len(name) == 0:
            name = rsc.platform().cpu().name()
        kwargs = {
            "system": cls.get_system(rsc),
            "debug_console": cls.get_debug_console(rsc),
            "gic_info": GeneratorCommon.get_gic_info(rsc),
            "devices": cls.get_devices(rsc),
            "regions": cls.get_regions(rsc),
            "pci_mmconfig": cls.get_pci_mmconfig(rsc),
            "name": name,
            "cpu": cls.get_cpu(rsc),
            "cpu_count": rsc.platform().cpu().cpu_count(),
            "hypervisor": cls.get_hypervisor(rsc),
            "pci_devices": cls.get_root_pci_devices(rsc),
            "ivshmem": GeneratorCommon.get_ivshmem(rsc),
            "board_mems": cls.get_board_mem(rsc),
            "vpci_irq_base": rootcell.vpci_irq_base(),
        }
        return kwargs


    @classmethod
    def gen_config_source(cls, rsc: Resource) -> Optional[str]:
        kwargs = cls.gen_kwargs(rsc)

        mako_txt = open(get_template_path("root_cell.mako"), "rt", encoding='utf-8').read()
        try:
            txt = Template(mako_txt).render(**kwargs)
            return txt.strip()
        except:
            print(exceptions.text_error_template().render())
            return None

    @classmethod
    def gen_config_bin(cls, rsc: Resource) -> bytes:
        logger.debug("开始生成根单元格二进制配置")
        try:

            kwargs = cls.gen_kwargs(rsc)

            config_filename = f"root_cell_{kwargs['name']}_config.json"
            with open(config_filename, 'w', encoding='utf-8') as f:
                json.dump(kwargs, f, ensure_ascii=False, indent=4)
            logger.info(f"根单元格配置数据已保存到: {config_filename}")

            cpu = rsc.platform().cpu()
            rootcell = rsc.jailhouse().rootcell()
            Rev = Revision14



            # len(devices)+len(board_mems)+len(regions)+ivshmem['count']+2}
            regions: List[JailhouseMemory] = list()
            ivsm: ResourceComm = rsc.jailhouse().ivshmem()
            ivsm_state_size = ivsm.ivshmem_state_size()
            ivsm_rw_size = ivsm.ivshmem_rw_size()
            ivsm_out_size = ivsm.ivshmem_out_size()
            ivsm_state = ivsm.ivshmem_phys()
            ivsm_rw = ivsm_state + ivsm_state_size
            ivsm_out = ivsm_state + ivsm_state_size + ivsm_rw_size
            peer_count = rsc.jailhouse().guestcells().cell_count()+1

            regions.append(JailhouseMemory(ivsm_state, ivsm_state, ivsm_state_size, JailhouseMemory.MEM_READ))
            regions.append(JailhouseMemory(ivsm_rw, ivsm_rw, ivsm_rw_size, JailhouseMemory.MEM_READ|JailhouseMemory.MEM_WRITE))
            regions.append(JailhouseMemory(ivsm_out, ivsm_out, ivsm_out_size, JailhouseMemory.MEM_READ|JailhouseMemory.MEM_WRITE))
            for i in range(1,peer_count):
                addr = ivsm_out + i*ivsm_out_size
                regions.append(JailhouseMemory(addr, addr, ivsm_out_size, JailhouseMemory.MEM_READ))

            for mem in cls.get_board_mem(rsc):
                flag = JailhouseMemory.MEM_READ | JailhouseMemory.MEM_WRITE | JailhouseMemory.MEM_EXECUTE
                print(mem)
                regions.append(JailhouseMemory(mem['addr'], mem['addr'], mem['size'], flag))

            for dev in cls.get_devices(rsc):
                flag = JailhouseMemory.MEM_READ | JailhouseMemory.MEM_WRITE | JailhouseMemory.MEM_IO
                regions.append(JailhouseMemory(dev['addr'], dev['addr'], dev['size'], flag))

            for mem in cpu.regions():
                if mem.type() is mem.Type.DRAM:
                    continue
                flag = JailhouseMemory.MEM_READ | JailhouseMemory.MEM_WRITE | JailhouseMemory.MEM_IO
                regions.append(JailhouseMemory(mem.addr(), mem.addr(), mem.size(), flag))

            class RootCell(ctypes.Structure):
                _pack_ = 1
                _fields_ = [
                    ("header", Rev.system),
                    ('cpus', ctypes.c_uint64*1),
                    ('mem_regions', Rev.memory*len(regions)),
                    ('irqchips', Rev.irqchip),
                    ('pci_devices', Rev.pci_device)
                ]

            config = RootCell()

            header = config.header
            header.signature = Rev.sys_signature
            header.revision = Rev.revision
            header.flags = cellconfig.JAILHOUSE_SYS_VIRTUAL_DEBUG_CONSOLE
            header.hypervisor_memory.phys_start = rootcell.hypervisor().addr()
            header.hypervisor_memory.size = rootcell.hypervisor().size()
            header.debug_console.address = kwargs['debug_console']['addr']
            header.debug_console.size = 0x1000
            header.debug_console.type = kwargs['debug_console']['type'].value
            header.debug_console.flags = cellconfig.JAILHOUSE_CON_ACCESS_MMIO | cellconfig.JAILHOUSE_CON_REGDIST_4

            pltinfo = config.header.platform_info
            pci_ecam = rsc.platform().cpu().find_region("pci_ecam")
            if pci_ecam is not None:
                pltinfo.pci_machine_mmconfig_base = pci_ecam.addr()

            pltinfo.pci_mmconfig_base = rootcell.pci_mmconfig().base_addr
            pltinfo.pci_mmconfig_end_bus = rootcell.pci_mmconfig().bus_count-1
            pltinfo.pci_is_virtual = 1
            pltinfo.pci_domain = rootcell.pci_mmconfig().domain
            pltinfo.plt.arm.gic_version = cpu.gic_version()
            pltinfo.plt.arm.gicd_base = cpu.gicd_base()
            pltinfo.plt.arm.gicr_base = cpu.gicr_base()
            pltinfo.plt.arm.gicc_base = cpu.gicc_base()
            pltinfo.plt.arm.gich_base = cpu.gich_base()
            pltinfo.plt.arm.gicv_base = cpu.gicv_base()
            pltinfo.plt.arm.maintenance_irq = 25

            header.root_cell.name = kwargs['name'].encode()
            header.root_cell.cpu_set_size = ctypes.sizeof(config.cpus)
            header.root_cell.num_memory_regions = ctypes.sizeof(config.mem_regions)//ctypes.sizeof(config.mem_regions[0])
            header.root_cell.num_irqchips = 1
            header.root_cell.num_pci_devices = 1
            header.root_cell.vpci_irq_base = kwargs['vpci_irq_base']

            config.cpus[0] = kwargs['cpu']['values'][0]
            mem_regions = config.mem_regions
            for idx, mem in enumerate(regions):
                mem_regions[idx].phys_start = mem.phys
                mem_regions[idx].virt_start = mem.virt
                mem_regions[idx].size       = mem.size
                mem_regions[idx].flags      = mem.flag

            irqchip = config.irqchips
            irqchip.address = cpu.gicd_base()
            irqchip.pin_base = 32
            irqchip.pin_bitmap[0] = 0xffffffff
            irqchip.pin_bitmap[1] = 0xffffffff
            irqchip.pin_bitmap[2] = 0xffffffff
            irqchip.pin_bitmap[3] = 0xffffffff

            pci_dev = config.pci_devices
            pci_dev.type = cellconfig.JAILHOUSE_PCI_TYPE_IVSHMEM
            pci_dev.domain = 1
            pci_dev.bdf = 0
            pci_dev.bar_mask = cellconfig.JAILHOUSE_IVSHMEM_BAR_MASK_INTX
            pci_dev.shmem_regions_start = 0
            pci_dev.shmem_dev_id = kwargs['ivshmem']['id']
            pci_dev.shmem_peers = peer_count
            pci_dev.shmem_protocol = cellconfig.JAILHOUSE_SHMEM_PROTO_UNDEFINED

            return ctypes.string_at(ctypes.addressof(config), ctypes.sizeof(config))
        except Exception as e:
            logger.error(f"生成根单元格配置时出错: {str(e)}")
            return None


class GuestCellGenerator(object):
    """
    客户单元格配置生成器。
    
    负责生成Jailhouse客户单元格(Guest Cell)的配置，包括:
    - 客户单元格基本配置
    - CPU分配配置
    - 内存映射配置
    - 设备分配配置
    - PCI设备配置
    - Linux设备树生成
    - 资源表生成
    """
    
    logger = logging.getLogger("GuestCellGenerator")
    
    @classmethod
    def get_cpu(cls, guestcell: ResourceGuestCell) -> Optional[dict]:
        """
        获取客户单元格的CPU配置。
        
        计算分配给客户单元格的CPU核心的位图。
        
        Args:
            guestcell: 客户单元格资源对象
            
        Returns:
            CPU配置字典，包含:
            - count: CPU总数
            - cpus: 分配的CPU核心列表
            - values: CPU位图值列表
            - bitmap: CPU位图的十六进制字符串表示
        """
        rsc_cpu: ResourceCPU = guestcell.find(ResourceCPU)
        cpu_count = rsc_cpu.cpu_count()
        cpus = guestcell.cpus()

        if cpu_count <= 0:
            logger.error("cpu count is 0")
            return None
        if len(cpus)==0:
            logger.error("no cpu for cell")
            return None

        bitmap_count = (cpu_count-1)//64 + 1
        values = [0,]*bitmap_count
        for c in cpus:
            i = c//64
            values[i] = values[i] | (1<<(c%64))

        bitmap = list(map(lambda x: f"0x{x:x}", values))

        return {
            "count": cpu_count,
            "cpus": list(cpus),
            "values": values,
            "bitmap": bitmap
        }

    @classmethod
    def get_gic_bitmaps(cls, guestcell: ResourceGuestCell) -> list:
        """
        获取GIC(Generic Interrupt Controller)中断位图。
        
        为客户单元格配置中断控制器访问权限。
        
        Args:
            guestcell: 客户单元格资源对象
            
        Returns:
            中断位图列表，每个元素包含:
            - bitmap: 中断位图值
            - comment: 位图说明
        """
        cpu: ResourceCPU = guestcell.find(ResourceCPU)
        rootcell: ResourceRootCell = guestcell.find(ResourceRootCell)

        vpci_irq_base = rootcell.vpci_irq_base() + guestcell.my_index() + 1

        irq_bitmaps = [
            {'bitmap': 0, 'comment': ''},
            {'bitmap': 0, 'comment': ''},
            {'bitmap': 0, 'comment': ''},
            {'bitmap': 0, 'comment': ''},
        ]

        def add_irq(_irq, _name):
            _irq = _irq - 32
            if _irq < 0 or _irq/32 >= len(irq_bitmaps):
                logger.warning(f"invalid irq {_irq+32}")
                return

            n, o = _irq//32, _irq%32
            irq_bitmaps[n]['bitmap']  = irq_bitmaps[n]['bitmap'] | (1 << o)
            irq_bitmaps[n]['comment'] = irq_bitmaps[n]['comment'] + f' {_name}({_irq})'

        add_irq(vpci_irq_base+32, "vpci")
        for name in guestcell.devices():
            dev = cpu.find_device(name)
            if dev is None:
                continue
            for irq in dev.irq():
                add_irq(irq, dev.name())

        return irq_bitmaps

    @classmethod
    def get_system(cls, guestcell: ResourceGuestCell) -> Optional[dict]:
        """
        获取客户单元格的系统配置。
        
        配置客户单元格的基本系统参数。
        
        Args:
            guestcell: 客户单元格资源对象
            
        Returns:
            系统配置字典，包含:
            - virt_console: 虚拟控制台配置
            - virt_cpuid: 虚拟CPU ID配置
            - arch: 架构类型
            - vpci_irq_base: 虚拟PCI中断基址
            - irq_bitmaps: 中断位图
            - reset_addr: 复位向量地址
            - cpu_name: CPU名称
        """
        cpu: ResourceCPU = guestcell.find(ResourceCPU)
        rootcell: ResourceRootCell = guestcell.find(ResourceRootCell)
        irq_bitmaps = cls.get_gic_bitmaps(guestcell)

        return {
            "virt_console": guestcell.virt_console(),
            "virt_cpuid": guestcell.virt_cpuid(),
            "arch": guestcell.arch().name,
            "vpci_irq_base": rootcell.vpci_irq_base() + guestcell.my_index() + 1,
            "irq_bitmaps": irq_bitmaps,
            "reset_addr": guestcell.reset_addr(),
            "cpu_name": cpu.name(),
        }

    @classmethod
    def get_system_mem(cls, guestcell: ResourceGuestCell) -> Optional[List[dict]]:
        mmaps = list()
        sysmem = guestcell.system_mem()
        if len(sysmem) == 0:
            return None
        for mm in sysmem:
            if mm.size() == 0:
                return None
            mmaps.append( {
                "phys": mm.phys(),
                "virt": mm.virt(),
                "size": mm.size(),
                "comment": mm.comment(),
                "type": mm.type().name
            })
        return mmaps

    @classmethod
    def get_memmaps(cls, guestcell: ResourceGuestCell) -> Optional[List[dict]]:
        mmaps = list()
        for mm in guestcell.memmaps():
            if mm.size() == 0:
                return None
            mmaps.append({
                "phys": mm.phys(),
                "virt": mm.virt(),
                "size": mm.size(),
                "comment": mm.comment()
            })
        return mmaps

    @classmethod
    def get_devices(cls, guestcell: ResourceGuestCell) -> Optional[List[dict]]:
        devices = list()
        cpu: ResourceCPU = guestcell.find(ResourceCPU)
        if cpu is None:
            return None
        for name in guestcell.devices():
            dev = cpu.find_device(name)
            if dev is None:
                continue
            devices.append({
                "name": dev.name(),
                "addr": dev.addr(),
                "size": dev.size(),
                "irq" : dev.irq()
            })
        return devices

    @classmethod
    def get_pci_device(cls, guestcell: ResourceGuestCell) -> Optional[dict]:
        devices = list()
        caps = list()
        rootcell: ResourceRootCell = guestcell.find(ResourceRootCell)

        pci_mmconfig = {
            "addr": rootcell.pci_mmconfig().base_addr,
            "irq": rootcell.vpci_irq_base() + guestcell.my_index() + 1
        }

        pci_devices: ResourcePCIDeviceList = guestcell.find(ResourcePCIDeviceList)
        for name in guestcell.pci_deivces():
            dev = pci_devices.find_device(name)
            if dev is None:
                logger.error(f"PCI device {name} not found")
                continue

            devices.append({
                "name": dev.name(),
                "type": "JAILHOUSE_PCI_TYPE_DEVICE",
                "domain": dev.domain(),
                "bdf": dev.bdf_value(),
                "bar_mask": list(map(lambda b: b.mask()&0xFFFFFFFF, dev.bars())),
                "caps_start": len(caps),
                "num_caps": len(dev.caps()),
            })
            for cap in dev.caps():
                caps.append({
                    "id": cap.id(),
                    "start": cap.start(),
                    "len": cap.len(),
                    "extended": cap.is_extended(),
                    "flags": cellconfig.JAILHOUSE_PCICAPS_WRITE,
                    "flags_str": 'JAILHOUSE_PCICAPS_WRITE',
                })

        return {
            "mmconfig": pci_mmconfig,
            "devices": devices,
            "caps": caps,
        }

    @classmethod
    def get_console(cls, guestcell: ResourceGuestCell) -> Optional[dict]:
        """
        获取console设备信息
        没有指定console设备返回None， 失败返回False
        """
        console = guestcell.console()
        if len(console) == 0:
            return None

        for dev in guestcell.find(ResourceCPU).devices():
            if dev.name() == console:
                type_value = cellconfig.jailhouse_con_type_form_str(dev.type())
                if type_value is None:
                    cls.logger.error("invalid consle device type.")
                    return False
                return {
                    "addr": dev.addr(),
                    "size": dev.size(),
                    "type": type_value
                }
        return False

    @classmethod
    def gen_kwargs(cls, guestcell: ResourceGuestCell) -> Optional[dict]:
        rsc: Resource = guestcell.ancestor(Resource)

        if rsc is None:
            return None
        kwargs = {
            "name": guestcell.name(),
            "cpu": cls.get_cpu(guestcell),
            "system": cls.get_system(guestcell),
            "gic": GeneratorCommon.get_gic_info(rsc),
            "ivshmem": GeneratorCommon.get_ivshmem(rsc, guestcell),
            "system_mem": cls.get_system_mem(guestcell),
            "memmaps": cls.get_memmaps(guestcell),
            "devices": cls.get_devices(guestcell),
            "comm_region": guestcell.comm_region(),
            "pci_devices": cls.get_pci_device(guestcell),
        }
        optional_kwargs = {
            "console": cls.get_console(guestcell),
        }

        for k in kwargs:
            if kwargs[k] is None:
                logger.error(f"{k} is None")
                return None
        kwargs.update(optional_kwargs)
        return kwargs

    @classmethod
    def gen_config_source(cls, guestcell: ResourceGuestCell) -> Optional[str]:
        """
        生成客户单元格的C语言配置源代码。
        
        使用模板生成客户单元格的配置源代码。
        
        Args:
            guestcell: 客户单元格资源对象
            
        Returns:
            配置源代码字符串，失败返回None
        """
        kwargs = cls.gen_kwargs(guestcell)
        if kwargs is None:
            return None

        try:
            mako_txt = open(get_template_path("guest_cell.mako"), "rt", encoding='utf-8').read()
            txt = Template(mako_txt).render(**kwargs)
        except:
            print(exceptions.text_error_template().render())
            return None

        return txt.strip()

    @classmethod
    def gen_config_bin(cls, guestcell: ResourceGuestCell) -> bytes:

        kwargs = cls.gen_kwargs(guestcell)  # 假设已有gen_kwargs方法
        
        # 👇 新增：保存配置数据结构到当前目录
        config_filename = f"guest_cell_{guestcell.name()}_config.json"
        with open(config_filename, 'w', encoding='utf-8') as f:
            json.dump(kwargs, f, ensure_ascii=False, indent=4)
        cls.logger.info(f"客户单元格配置数据已保存到: {config_filename}")
        """
        生成客户单元格的二进制配置数据。
        
        生成可以直接加载到Jailhouse的二进制配置数据。
        
        Args:
            guestcell: 客户单元格资源对象
            
        Returns:
            二进制配置数据
        """
        Rev = Revision14
        cpu: ResourceCPU = guestcell.find(ResourceCPU)
        rootcell: ResourceRootCell = guestcell.find(ResourceRootCell)

        regions = list()

        ivsm: ResourceComm = guestcell.find(ResourceComm)
        guestcells: ResourceGuestCellList = guestcell.ancestor(ResourceGuestCellList)
        ivsm_state_size = ivsm.ivshmem_state_size()
        ivsm_rw_size = ivsm.ivshmem_rw_size()
        ivsm_out_size = ivsm.ivshmem_out_size()
        ivsm_phys = ivsm.ivshmem_phys()
        ivsm_virt = guestcell.ivshmem_virt_addr()
        ivsm_rw_off = ivsm_state_size
        ivsm_out_off = ivsm_state_size + ivsm_rw_size
        peer_count = guestcells.cell_count()+1

        regions.append(JailhouseMemory(ivsm_phys, ivsm_virt, ivsm_state_size, JailhouseMemory.MEM_READ|JailhouseMemory.MEM_ROOTSHARED))
        regions.append(JailhouseMemory(ivsm_phys+ivsm_rw_off , ivsm_virt+ivsm_rw_off, ivsm_rw_size, JailhouseMemory.MEM_READ|JailhouseMemory.MEM_WRITE|JailhouseMemory.MEM_ROOTSHARED))
        for i in range(0,peer_count):
            phys = ivsm_phys + ivsm_out_off + i*ivsm_out_size
            virt = ivsm_virt + ivsm_out_off + i*ivsm_out_size
            if i == guestcell.my_index()+1:
                regions.append(JailhouseMemory(phys, virt, ivsm_out_size, JailhouseMemory.MEM_READ|JailhouseMemory.MEM_WRITE|JailhouseMemory.MEM_ROOTSHARED))
            else:
                regions.append(JailhouseMemory(phys, virt, ivsm_out_size, JailhouseMemory.MEM_READ|JailhouseMemory.MEM_ROOTSHARED))

        for mm in guestcell.system_mem():
            if mm.type().name ==  'RESOURCE_TABLE':
                flags = JailhouseMemory.MEM_READ | JailhouseMemory.MEM_WRITE | JailhouseMemory.MEM_LOADABLE | JailhouseMemory.MEM_DMA | JailhouseMemory.MEM_RESOURCE_TABLE
            else:
                flags = JailhouseMemory.MEM_READ | JailhouseMemory.MEM_WRITE | JailhouseMemory.MEM_EXECUTE | JailhouseMemory.MEM_LOADABLE | JailhouseMemory.MEM_DMA
            regions.append(JailhouseMemory(mm.phys(), mm.virt(), mm.size(), flags))

        for mm in guestcell.memmaps():
            flags = JailhouseMemory.MEM_READ | JailhouseMemory.MEM_WRITE
            regions.append(JailhouseMemory(mm.phys(), mm.virt(), mm.size(), flags))

        for dev in cls.get_devices(guestcell):
            flag = JailhouseMemory.MEM_READ | JailhouseMemory.MEM_WRITE | JailhouseMemory.MEM_IO|JailhouseMemory.MEM_ROOTSHARED
            regions.append(JailhouseMemory(dev['addr'], dev['addr'], dev['size'], flag))

        regions.append(JailhouseMemory(0, guestcell.comm_region(), 0x1000, JailhouseMemory.MEM_READ|JailhouseMemory.MEM_WRITE|JailhouseMemory.MEM_COMM_REGION))

        pci_devices = cls.get_pci_device(guestcell)

        class GuestcellStruct(ctypes.Structure):
            _pack_ = 1
            _fields_ = [
                ("cell", Rev.cell_desc),
                ('cpus', ctypes.c_uint64*1),
                ('mem_regions', Rev.memory*len(regions)),
                ('irqchips', Rev.irqchip),
                ('pci_devices', Rev.pci_device*(1+len(pci_devices['devices']))),
                ('pci_caps', Rev.pci_capability*len(pci_devices['caps'])),
            ]

        config = GuestcellStruct()

        cell = config.cell
        cell.signature = Rev.cell_signature
        cell.revision = Rev.revision
        cell.name = guestcell.name().encode()
        cell.flags = cellconfig.JAILHOUSE_CELL_PASSIVE_COMMREG
        if guestcell.virt_console():
            cell.flags = cell.flags + cellconfig.JAILHOUSE_CELL_VIRTUAL_CONSOLE_PERMITTED
        if guestcell.arch() is ARMArch.AArch32:
            cell.flags = cell.flags + cellconfig.JAILHOUSE_CELL_AARCH32
        if guestcell.virt_cpuid():
            cell.flags = cell.flags + cellconfig.JAILHOUSE_CELL_VIRT_CPUID
        cell.cpu_reset_address = guestcell.reset_addr()
        cell.cpu_set_size = ctypes.sizeof(config.cpus)
        cell.num_memory_regions = ctypes.sizeof(config.mem_regions)//ctypes.sizeof(config.mem_regions[0])
        cell.num_irqchips = 1
        cell.num_pci_devices = ctypes.sizeof(config.pci_devices)//ctypes.sizeof(config.pci_devices[0])
        cell.num_pci_caps = len(pci_devices['caps'])
        cell.vpci_irq_base =  rootcell.vpci_irq_base() + guestcell.my_index() + 1

        console = cls.get_console(guestcell)
        if console is False:
            return None
        if console is not None:
            cell.console.address = console['addr']
            cell.console.size = 0x1000
            cell.console.type = console['type'].value
            cell.console.flags = cellconfig.JAILHOUSE_CON_ACCESS_MMIO | cellconfig.JAILHOUSE_CON_REGDIST_4

        config.cpus[0] = cls.get_cpu(guestcell)['values'][0]

        mem_regions = config.mem_regions
        for idx, mem in enumerate(regions):
            mem_regions[idx].phys_start = mem.phys
            mem_regions[idx].virt_start = mem.virt
            mem_regions[idx].size       = mem.size
            mem_regions[idx].flags      = mem.flag

        irqchip = config.irqchips
        irqchip.address = cpu.gicd_base()
        irqchip.pin_base = 32
        for idx, bitmap in enumerate(cls.get_gic_bitmaps(guestcell)):
            irqchip.pin_bitmap[idx] = bitmap['bitmap']

        pci_ivshmem = config.pci_devices[0]
        pci_ivshmem.type = cellconfig.JAILHOUSE_PCI_TYPE_IVSHMEM
        pci_ivshmem.domain = 1
        pci_ivshmem.bdf = 0
        pci_ivshmem.bar_mask = cellconfig.JAILHOUSE_IVSHMEM_BAR_MASK_INTX
        pci_ivshmem.shmem_regions_start = 0
        pci_ivshmem.shmem_dev_id = guestcell.my_index()+1
        pci_ivshmem.shmem_peers = peer_count
        pci_ivshmem.shmem_protocol = cellconfig.JAILHOUSE_SHMEM_PROTO_UNDEFINED

        for idx, dev in enumerate(pci_devices['devices']):
            pci_dev = config.pci_devices[idx+1]
            pci_dev.type = cellconfig.JAILHOUSE_PCI_TYPE_DEVICE
            pci_dev.domain = dev['domain']
            pci_dev.bdf = dev['bdf']
            pci_dev.virt_bdf = (idx+1) << 3
            if dev['num_caps'] > 0:
                pci_dev.caps_start = dev['caps_start']
                pci_dev.num_caps = dev['num_caps']
            for i in range(6):
                pci_dev.bar_mask[i] = dev['bar_mask'][i]

        pci_caps = config.pci_caps
        for idx, cap in enumerate(pci_devices['caps']):
            pci_cap = config.pci_caps[idx]
            if cap['extended']:
                pci_cap.id = cap['id'] | cellconfig.JAILHOUSE_PCI_EXT_CAP
            else:
                pci_cap.id = cap['id']
            pci_cap.start = cap['start']
            pci_cap.len = cap['len']
            pci_cap.flags = cap['flags']

        return ctypes.string_at(ctypes.addressof(config), ctypes.sizeof(config))

    @classmethod
    def gen_guestlinux_dts(cls, guestcell: ResourceGuestCell) -> Optional[str]:
        cpu: ResourceCPU = guestcell.find(ResourceCPU)
        fname = f'guestos-{cpu.name()}.dts.mako'
        kwargs = cls.gen_kwargs(guestcell)
        if kwargs is None:
            return None
        from mako import exceptions
        try:
            mako_txt = open(get_template_path(fname), "rt", encoding='utf-8').read()
            txt = Template(mako_txt).render(**kwargs)
        except:
            print(exceptions.text_error_template().render())
            return None

        return txt.strip()

    @classmethod
    def dts_to_dtb(cls, dts):
        x = fdt.parse_dts(dts)
        return x.to_dtb(version=17)

    @classmethod
    def gen_guestlinux_dtb(cls, guestcell: ResourceGuestCell) -> Optional[bytes]:
        dts = cls.gen_guestlinux_dts(guestcell)
        if dts is None:
            return None
        return cls.dts_to_dtb(dts)

    @classmethod
    def gen_resource_table_src(cls, guestcell: ResourceGuestCell) -> Optional[str]:
        kwargs = cls.gen_kwargs(guestcell)
        if kwargs is None:
            return None
        from mako import exceptions
        try:
            mako_txt = open(get_template_path("resource_table.dts.mako"), "rt", encoding='utf-8').read()
            txt = Template(mako_txt).render(**kwargs)
        except:
            print(exceptions.text_error_template().render())
            return None

        return txt.strip()

    @classmethod
    def gen_resource_table_bin(cls, guestcell: ResourceGuestCell) -> Optional[bytes]:
        src = cls.gen_resource_table_src(guestcell)
        if src is None:
            return None
        return cls.dts_to_dtb(src)


def test():
    import logging
    import pprint
    logging.basicConfig(level=logging.DEBUG)
    PlatformMgr.get_instance().load("platform/index.toml")

    rsc = ResourceMgr.get_instance().open("demos/D2000.jhr")
    if rsc is None:
        logging.error("open failed.")
        return False

    guestcell: ResourceGuestCellList = rsc.find(ResourceGuestCellList)
    txt = GuestCellGenerator.gen_config_source(guestcell.cell_at(0))
    print(txt)

    kwargs = GuestCellGenerator.gen_kwargs(guestcell.cell_at(0))

    dts = GuestCellGenerator.gen_guestlinux_dts(guestcell.cell_at(0))
    print(dts)
    GuestCellGenerator.gen_guestlinux_dtb(guestcell)

    #xx = RootCellGenerator.gen_config_source(rsc)
    #print(xx)

@click.group()
def cli():
    """Jailhouse配置生成工具命令行接口。"""
    pass


@cli.command("resource-table")
@click.argument("jhr")
@click.argument("name")
@click.argument("output")
def cli_resource_table(jhr, name, output):
    """
    生成资源表配置。
    
    Args:
        jhr: Jailhouse资源文件路径
        name: 客户单元格名称
        output: 输出文件路径(.dts或.dtb)
    """
    rsc = ResourceMgr.get_instance().open(jhr)
    if rsc is None:
        logging.error("open failed.")
        return False
    guestcell: Optional[ResourceGuestCell] = rsc.jailhouse().guestcells().find_cell(name)
    if guestcell is None:
        logging.error("cell not found.")
        print("available guest cells:")
        guestcells = rsc.jailhouse().guestcells()
        for i in range(guestcells.cell_count()):
            print("    ", guestcells.cell_at(i).name())
        return False

    txt = GuestCellGenerator.gen_resource_table_src(guestcell)
    if txt is None:
        logging.error("generate failed.")
        return False
    print(txt)

    dtb = GuestCellGenerator.dts_to_dtb(txt)
    if dtb is None:
        logging.error("generate dtb failed.")
        return False

    if output.endswith(".dtb"):
        try:
            with open(output, "wb") as f:
                f.write(dtb)
        except:
            logging.error("write dtb failed.")
            return False
    elif output.endswith(".dts"):
        try:
            with open(output, "wt") as f:
                f.write(txt)
        except:
            logging.error("write dts failed.")
            return False
    return True

@cli.command("linux-dtb")
@click.argument("jhr")
@click.argument("name")
@click.argument("output")
def generate_linux_dtb(jhr, name, output):
    """
    生成Linux设备树配置。
    
    Args:
        jhr: Jailhouse资源文件路径
        name: 客户单元格名称
        output: 输出文件路径(.dts或.dtb)
    """
    import logging

    rsc = ResourceMgr.get_instance().open(jhr)
    if rsc is None:
        logging.error("open failed.")
        return False

    guestcell = rsc.jailhouse().guestcells().find_cell(name)
    if guestcell is None:
        logging.error(f"guestcell {name} not found.")
        print("available guest cells:")
        guestcells = rsc.jailhouse().guestcells()
        for i in range(guestcells.cell_count()):
            print("    ", guestcells.cell_at(i).name())
        return False

    dts = GuestCellGenerator.gen_guestlinux_dts(guestcell)
    if dts is None:
        logging.error(f"generate dts failed.")
        return False

    print(GuestCellGenerator.gen_kwargs(guestcell))
    print(dts)
    dtb = GuestCellGenerator.gen_guestlinux_dtb(guestcell)
    if dtb is None:
        logging.error(f"generate dtb failed.")
        return False

    if output.endswith(".dtb"):
        with open(output, "wb") as f:
            f.write(dtb)
    if output.endswith(".dts"):
        with open(output, "wt") as f:
            f.write(dts)

@cli.command("kwargs")
@click.argument("jhr")
@click.argument("name")
def print_kwargs(jhr, name):
    """
    打印客户单元格配置参数。
    
    Args:
        jhr: Jailhouse资源文件路径
        name: 客户单元格名称
    """
    import logging

    rsc = ResourceMgr.get_instance().open(jhr)
    if rsc is None:
        logging.error("open failed.")
        return False

    guestcell = rsc.jailhouse().guestcells().find_cell(name)
    if guestcell is None:
        logging.error(f"guestcell {name} not found.")
        print("available guest cells:")
        guestcells = rsc.jailhouse().guestcells()
        for i in range(guestcells.cell_count()):
            print("    ", guestcells.cell_at(i).name())
        return False
    import pprint
    pprint.pprint(GuestCellGenerator.gen_kwargs(guestcell))

@cli.command("rootcell")
@click.argument("jhr")
@click.argument("output")
def generate_rootcell(jhr, output: str):
    """
    生成根单元格配置。
    
    Args:
        jhr: Jailhouse资源文件路径
        output: 输出文件路径(.c或.cell)
    """
    import logging

    rsc = ResourceMgr.get_instance().open(jhr)
    if rsc is None:
        logging.error("open failed.")
        return False

    if output.endswith(".c"):
        txt = RootCellGenerator.gen_config_source(rsc)
        if txt is None:
            print("generate failed.")
            return False
        try:
            with open(output, "wt") as f:
                f.write(txt)
        except:
            print("open failed.")
            return False
        return True

    elif output.endswith(".cell"):
        cell = RootCellGenerator.gen_config_bin(rsc)
        if cell is None:
            print("generate failed.")
            return False
        try:
            with open(output, "wb") as f:
                f.write(cell)
        except:
            print("open failed.")
            return False
        return True

@cli.command("guestcell")
@click.argument("jhr")
@click.argument("name")
@click.argument("output")
def generate_guestcell(jhr, name, output: str):
    """
    生成客户单元格配置。
    
    Args:
        jhr: Jailhouse资源文件路径
        name: 客户单元格名称
        output: 输出文件路径(.c或.cell)
    """
    import logging

    rsc = ResourceMgr.get_instance().open(jhr)
    if rsc is None:
        logging.error("open failed.")
        return False

    guestcell = rsc.jailhouse().guestcells().find_cell(name)
    if guestcell is None:
        logging.error(f"guestcell {name} not found.")
        print("available guest cells:")
        guestcells = rsc.jailhouse().guestcells()
        for i in range(guestcells.cell_count()):
            print("    ", guestcells.cell_at(i).name())
        return False

    if output.endswith(".c"):
        txt = GuestCellGenerator.gen_config_source(guestcell)
        if txt is None:
            print("generate failed.")
            return False
        try:
            with open(output, "wt") as f:
                f.write(txt)
        except:
            print("open failed.")
            return False
        return True

    elif output.endswith(".cell"):
        cell = GuestCellGenerator.gen_config_bin(guestcell)
        if cell is None:
            print("generate failed.")
            return False
        try:
            with open(output, "wb") as f:
                f.write(cell)
        except:
            print("open failed.")
            return False
        return True


if __name__ == "__main__":
    cli()