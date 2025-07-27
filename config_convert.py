import json
import os
from jh_resource import ResourceJailhouse, ResourceGuestCell

class ConfigConverter:
    """配置文件转换工具类，用于将资源对象转换为目标JSON格式"""
    
    @staticmethod
    def get_examples_path():
        """获取examples目录路径，确保目录存在"""
        examples_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "examples")
        if not os.path.exists(examples_dir):
            os.makedirs(examples_dir)
        return examples_dir

    @staticmethod
    def convert_root_cell(rsc: ResourceJailhouse) -> dict:
        """转换根单元格配置"""
        root_cell = rsc.jailhouse().rootcell()
        platform = rsc.platform()
        cpu = platform.cpu()
        
        # 收集内存区域
        memory_regions = []
        # 添加RAM区域
        for region in platform.board().ram_regions():
            memory_regions.append({
                "type": "ram",
                "physical_start": f"0x{region.addr():x}",
                "virtual_start": f"0x{region.addr():x}",
                "size": f"0x{region.size():x}"
            })
        # 添加设备区域
        for dev in cpu.devices():
            memory_regions.append({
                "type": "virtio",
                "physical_start": f"0x{dev.addr():x}",
                "virtual_start": f"0x{dev.addr():x}",
                "size": f"0x{dev.size():x}"
            })

        return {
            "arch": "arm64" if cpu.arch() == "AArch64" else cpu.arch().lower(),
            "name": "root_cell",
            "zone_id": 0,  # 根单元格通常为0
            "cpus": [cpu.cpu_count()],  # 总CPU核心数
            "memory_regions": memory_regions,
            "interrupts": [irq for dev in cpu.devices() for irq in dev.irq()],
            "ivc_configs": [],
            "kernel_filepath": f"./zone0/{root_cell.kernel_file()}",
            "dtb_filepath": f"./zone0/{root_cell.dtb_file()}",
            "kernel_load_paddr": f"0x{root_cell.kernel_load_addr():x}",
            "dtb_load_paddr": f"0x{root_cell.dtb_load_addr():x}",
            "entry_point": f"0x{root_cell.entry_point():x}",
            "kernel_args": root_cell.cmdline(),
            "arch_config": {
                "gic_version": f"v{cpu.gic_version()}",
                "gicd_base": f"0x{cpu.gicd_base():x}",
                "gicd_size": f"0x{cpu.gicd_size():x}",
                "gicr_base": f"0x{cpu.gicr_base():x}",
                "gicr_size": f"0x{cpu.gicr_size():x}",
                "gits_base": "0x0",
                "gits_size": "0x0"
            }
        }

    @staticmethod
    def convert_guest_cell(rsc: ResourceJailhouse, cell: ResourceGuestCell) -> dict:
        """转换客户单元格配置"""
        cpu = rsc.platform().cpu()
        
        # 收集内存区域
        memory_regions = []
        for mem in cell.memories():
            mem_type = "ram" if mem.type() == "NORMAL" else "virtio"
            memory_regions.append({
                "type": mem_type,
                "physical_start": f"0x{mem.phys():x}",
                "virtual_start": f"0x{mem.virt():x}",
                "size": f"0x{mem.size():x}"
            })

        return {
            "arch": "arm64" if cpu.arch() == "AArch64" else cpu.arch().lower(),
            "name": cell.name(),
            "zone_id": cell.id(),
            "cpus": cell.cpus(),
            "memory_regions": memory_regions,
            "interrupts": cell.irqs(),
            "ivc_configs": [],
            "kernel_filepath": f"./zone{cell.id()}/{cell.image_file()}",
            "dtb_filepath": f"./zone{cell.id()}/{cell.dtb_file()}",
            "kernel_load_paddr": f"0x{cell.kernel_load_addr():x}",
            "dtb_load_paddr": f"0x{cell.dtb_load_addr():x}",
            "entry_point": f"0x{cell.entry_point():x}",
            "kernel_args": cell.cmdline(),
            "arch_config": {
                "gic_version": f"v{cpu.gic_version()}",
                "gicd_base": f"0x{cpu.gicd_base():x}",
                "gicd_size": f"0x{cpu.gicd_size():x}",
                "gicr_base": f"0x{cpu.gicr_base():x}",
                "gicr_size": f"0x{cpu.gicr_size():x}",
                "gits_base": "0x0",
                "gits_size": "0x0"
            }
        }

    @staticmethod
    def save_config(config: dict, filename: str):
        """保存配置到examples目录"""
        save_path = os.path.join(ConfigConverter.get_examples_path(), filename)
        with open(save_path, 'w') as f:
            json.dump(config, f, indent=4)
        return save_path

    # 仅用于测试：生成并保存配置文件
    if __name__ == "__main__":
        # 注意：这里需要根据实际项目的资源对象创建逻辑修改
        # 以下为示例代码，需替换为真实的资源对象获取方式
        try:
            # 假设通过ResourceJailhouse获取根单元格和客户单元格资源
            # 实际项目中可能需要从配置文件或其他模块加载资源
            from jh_resource import ResourceJailhouse  # 确保导入正确

            # 1. 创建/加载资源对象（根据项目实际逻辑修改）
            # 例如：从现有配置加载资源
            rsc = ResourceJailhouse()  # 实际项目中可能需要传入参数
            
            # 2. 生成根单元格配置并保存
            root_config = ConfigConverter.convert_root_cell(rsc)
            root_save_path = ConfigConverter.save_config(root_config, "root_cell_config.json")
            print(f"根单元格配置已保存到：{root_save_path}")
            
            # 3. 生成客户单元格配置并保存（如果有客户单元格）
            # 假设rsc中包含客户单元格列表
            guest_cells = rsc.jailhouse().guestcells()  # 实际项目中获取客户单元格的方法可能不同
            for guest_cell in guest_cells:
                guest_config = ConfigConverter.convert_guest_cell(rsc, guest_cell)
                guest_save_path = ConfigConverter.save_config(guest_config, f"guest_cell_{guest_cell.id()}_config.json")
                print(f"客户单元格{guest_cell.id()}配置已保存到：{guest_save_path}")
                
        except Exception as e:
            print(f"生成配置文件失败：{str(e)}")