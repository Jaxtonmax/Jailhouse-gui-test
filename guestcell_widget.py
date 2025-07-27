import logging
from typing import Optional
from PySide2 import QtWidgets
from cpu_edit_widget import CPUEditWidget
from jh_resource import ARMArch, ResourceCPU, ResourceGuestCell, ResourceGuestCellList, ResourcePCIDeviceList
from jh_resource import ResourceSignals
from mem_edit_widget import MemEditWidget
from utils import from_human_num, to_human_addr
from flowlayout import FlowLayout
from common_widget import clean_layout, set_lineedit_status, SelectButton
from forms.ui_guestcell_widget import Ui_GuestCellWidget
from forms.ui_guestcells_widget import Ui_GuestCellsWidget
from tip_widget import TipMgr
from json_config_updater import JSONConfigUpdater
from rpc_server.rpc_client import RPCClient 


tip_sys_mem = """\
配置guest cell系统的内存段的简介、物理地址、虚拟地址、大小, 可以增加删除相应的条目。
系统内存: DDR中内存段。
物理地址: root cell中看到的真实的物理地址。
虚拟地址: guest cell中看到的物理地址。
内存设置要注意分段，地址不能重合，保证各个内存段之间的唯一性。
另外, 地址和大小支持表达式, 如: 物理地址(0x2009000000+16*MB)、大小4*MB等格式。
"""

tip_add_map = """\
地址空间映射：在系统中需要使用一块特定的内存区域，就需要在此处单独申请，该段内存必须在系统内存范围内，不能和其他内存空间重合。
该段内存空间不支持load操作, 天脉需要单独添加Debug空间, Debug空间添加如下:
物理地址: 0x3a000000 虚拟地址: 0x3a000000 大小: 16*MB
"""

tip_ivshmem = """\
核间通信: 不同CPU核之间进行通信
ivshmem虚拟地址: 共享内存通信地址的基地址, 该地址是guest cell看到的物理地址
communication region: jailhouse提供的一种简易的通信机制, 通过它可以获取一些平台的信息
"""

tip_comm_region = """\
Communication region是jailhouse实现guestcell信息交互的一种方式.
jailhouse中的linux-loader程序固定使用0x80000000地址，因此针对Linux系统该值必须填写为0x80000000,
其他系统根据需要填写，只要不与其他地址冲突即可
"""

class GuestCellsWidget(QtWidgets.QWidget):
    logger = logging.getLogger("GuestCellsWidget")
    def __init__(self, parent=None):
        super().__init__(parent)
        self._ui = Ui_GuestCellsWidget()
        self._ui.setupUi(self)

        self._guestcells: Optional[ResourceGuestCellList] = None
        self._guestcell_widget = GuestCellWidget(self)
        self._ui.frame_guestcell_content.layout().addWidget(self._guestcell_widget)

        self._ui.btn_create_cell.clicked.connect(self._on_create_cell)
        self._ui.btn_remove_cell.clicked.connect(self._on_remove_cell)
        self._ui.listwidget_guestcells.currentRowChanged.connect(self._on_guestcell_selected)

        self._json_template_path = "/home/wzm/work/Jailhouse-gui/template.json"  # 替换为你的模板路径
        self._output_json_path = "/home/wzm/work/Jailhouse-gui/dist/config.json"    # 输出JSON路径
        self._rpc_server_addr = "tcp://192.168.1.52:4240"            # 替换为实际RPC地址

        ResourceSignals.value_changed.connect(self._on_resource_value_changed)

    def set_guestcells(self, guestcells: ResourceGuestCellList):
        if guestcells is None:
            self._guestcells = None
            return

        self._guestcells = guestcells
        self._update_guestcells()
        self._ui.frame_guestcell_content.hide()

    def _on_resource_value_changed(self, sender, **kwargs):
        if isinstance(sender, ResourceGuestCell):
            cell: ResourceGuestCell = sender
            part = kwargs.get('part')
            if part == 'name':
                self._ui.label_guestcell_name.setText(cell.name())
                self._update_guestcells()

    def _update_guestcells(self):
        if self._guestcells is None:
            self._ui.listwidget_guestcells.clear()
            return

        guestcells = self._guestcells

        current_name = ""
        if self._ui.listwidget_guestcells.currentRow() >= 0:
            current_name = self._ui.listwidget_guestcells.currentItem().text()

        self._ui.label_guestcell_name.clear()
        self._ui.btn_remove_cell.setEnabled(False)
        self._ui.frame_guestcell_content.hide()

        self._ui.listwidget_guestcells.blockSignals(True)
        self._ui.listwidget_guestcells.clear()
        for i in range(guestcells.cell_count()):
            guestcell = guestcells.cell_at(i)
            name = guestcell.name()
            item = QtWidgets.QListWidgetItem(name, self._ui.listwidget_guestcells)
            self._ui.listwidget_guestcells.addItem(item)
        self._ui.listwidget_guestcells.blockSignals(False)

        height = self._ui.listwidget_guestcells.sizeHintForRow(0)*self._ui.listwidget_guestcells.count()
        self._ui.listwidget_guestcells.setFixedHeight(height+10)

        for i in range(guestcells.cell_count()):
            if current_name == guestcells.cell_at(i).name():
                self._ui.listwidget_guestcells.setCurrentRow(i)

    def _on_guestcell_selected(self, row):
        if self._guestcells is None:
            return
        guestcell = self._guestcells.cell_at(row)
        if guestcell is not None:
            self._guestcell_widget.set_guestcell(guestcell)
            self._ui.label_guestcell_name.setText(guestcell.name())
            self._ui.btn_remove_cell.setEnabled(True)
            self._ui.frame_guestcell_content.show()

    def _on_create_cell(self):
        if self._guestcells is None:
            return

        name = "new_cell"
        for i in range(1,999):
            _name = f'new_cell_{i}'
            if self._guestcells.find_cell(_name) is None:
                name = _name
                break

        cell = self._guestcells.create_cell(name)
        if cell is None:
            self.logger.error("create cell failed")
            return
        self.logger.info("create cell success")
        self._update_guestcells()

    def _on_remove_cell(self):
        if self._guestcells is None:
            return
        row = self._ui.listwidget_guestcells.currentRow()
        if row < 0:
            return
        guestcell = self._guestcells.cell_at(row)
        if guestcell is None:
            return

        x = QtWidgets.QMessageBox.question(self, "删除Guest Cell", f"是否删除Guest Cell {guestcell.name()}?",
                                           QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if x == QtWidgets.QMessageBox.Yes:
            self._guestcells.remove_cell(guestcell)
            self._ui.listwidget_guestcells.clear()
            self._update_guestcells()


class GuestCellWidget(QtWidgets.QWidget):
    logger = logging.getLogger("GuestCellWidget")
    not_use = "不使用"

    def __init__(self, parent=None):
        super().__init__(parent)
        # 初始化UI布局框架（只执行一次）
        self._ui = Ui_GuestCellWidget()
        self._ui.setupUi(self)
        
        # 初始化_cpu_editor（最优先，只初始化一次）
        self._cpu_editor = None
        try:
            # 尝试创建CPUEditWidget实例
            self._cpu_editor = CPUEditWidget(self)
            self.logger.debug("CPUEditWidget实例创建成功")
            
            # 确保frame_cpus有布局
            if self._ui.frame_cpus.layout() is None:
                self._ui.frame_cpus.setLayout(QtWidgets.QVBoxLayout())
                self.logger.debug("为frame_cpus创建新布局")
            
            # 添加到布局
            self._ui.frame_cpus.layout().addWidget(self._cpu_editor)
            self.logger.debug("CPUEditWidget已添加到布局")
        except Exception as e:
            self.logger.error(f"初始化_cpu_editor失败: {str(e)}", exc_info=True)
            QtWidgets.QMessageBox.critical(self, "初始化错误", f"CPU编辑器加载失败: {str(e)}")
            return  # 初始化失败则终止后续流程
        
        # 初始化其他组件
        self._init_other_components()
        
        # 绑定信号（确保在_cpu_editor初始化后）
        self._cpu_editor.cpus_changed.connect(self._on_cpus_changed)
        self.logger.debug("GuestCellWidget初始化完成")

    def _init_other_components(self):
        """初始化其他组件（与CPU编辑器无关的部分）"""
        self._ui.combobox_console.setView(QtWidgets.QListView())

        # 系统内存编辑组件
        self._sysmem_widget = MemEditWidget(self)
        self._ui.frame_sys_mem.layout().addWidget(self._sysmem_widget)
        self._sysmem_widget.signal_changed.connect(self._on_sysmem_changed)

        # 设备布局
        self._devices_layout = FlowLayout()
        self._ui.frame_devices.setLayout(self._devices_layout)

        # PCI设备布局
        self._pci_devices_layout = FlowLayout()
        self._ui.frame_pci_devices.setLayout(self._pci_devices_layout)

        # 内存映射编辑组件
        self._mmaps_widget = MemEditWidget(self)
        self._ui.frame_memmaps.layout().addWidget(self._mmaps_widget)
        self._mmaps_widget.signal_changed.connect(self._on_memmaps_changed)

        # 绑定其他信号
        self._ui.linedit_name.editingFinished.connect(self._on_name_edit_finished)
        self._ui.linedit_name.textChanged.connect(self._on_name_changed)
        self._ui.radiobtn_aarch32.clicked.connect(self._on_arch_change)
        self._ui.radiobtn_aarch64.clicked.connect(self._on_arch_change)
        self._ui.btn_virtual_console.clicked.connect(self._on_virt_console_changed)
        self._ui.btn_use_virt_cpuid.clicked.connect(self._on_virt_cpuid_changed)
        self._ui.lineedit_ivshmem_virt_addr.editingFinished.connect(self._on_ivshmem_addr_changed)
        self._ui.lineedit_comm_region.editingFinished.connect(self._on_comm_region_changed)
        self._ui.combobox_console.currentIndexChanged.connect(self._on_console_changed)
        self._ui.lineedit_reset_addr.editingFinished.connect(self._on_reset_addr_changed)

        # 初始化属性
        self._guestcell: Optional[ResourceGuestCell] = None
        self._json_template_path = "/home/wzm/work/Jailhouse-gui/template.json"
        self._output_json_path = "/home/wzm/work/Jailhouse-gui/dist/config.json"
        self._rpc_server_addr = "tcp://192.168.1.52:4240"

        # 提示信息
        TipMgr.add(self._ui.linedit_name, "guest cell 名称，名称使用字母和数字和横线，不能包含空格, 长度不能超过31")
        tip_arch = "选择cell运行32位模式或64位模式"
        TipMgr.add(self._ui.radiobtn_aarch32, tip_arch)
        TipMgr.add(self._ui.radiobtn_aarch64, tip_arch)
        tip_virt_console = "使用hypercall方式的串口输出, 使用该功能有助于底层调试, 通过hypercall的方式让hypervisor输出"
        TipMgr.add(self._ui.btn_virtual_console, tip_virt_console)
        tip_virt_cpuid = "使用虚拟CPUID后, 可以保证guest cell在多核 (任意核) 上运行。"
        TipMgr.add(self._ui.btn_use_virt_cpuid, tip_virt_cpuid)
        TipMgr.add(self._ui.frame_sys_mem, tip_sys_mem)
        tip_cpu = "用户可以按照需要选择cpu核"
        TipMgr.add(self._ui.frame_cpus, tip_cpu)
        TipMgr.add(self._ui.frame_memmaps, tip_add_map)
        TipMgr.add(self._ui.frame_comm, tip_ivshmem)
        TipMgr.add(self._ui.lineedit_comm_region, tip_comm_region)
        tip_dev = "选择分配给guest cell的设备"
        TipMgr.add(self._ui.frame_devices, tip_dev)
        tip_pci = "选择分配给guest cell的PCI设备"
        TipMgr.add(self._ui.frame_pci_devices,tip_pci)

    def set_guestcell(self, guestcell:ResourceGuestCell):
        if guestcell is None:
            self._guestcell = None
            return

        self._guestcell = None

        self._ui.linedit_name.setText(guestcell.name())
        arch = guestcell.arch()
        if arch is ARMArch.AArch32:
            self._ui.radiobtn_aarch32.setChecked(True)
        elif arch is ARMArch.AArch64:
            self._ui.radiobtn_aarch64.setChecked(True)
        self._ui.btn_virtual_console.setChecked(guestcell.virt_console())
        self._ui.btn_use_virt_cpuid.setChecked(guestcell.virt_cpuid())
        self._ui.lineedit_reset_addr.setText(to_human_addr(guestcell.reset_addr()))

        self._sysmem_widget.set_mmaps(guestcell.system_mem())
        self._mmaps_widget.set_mmaps(guestcell.memmaps())

        self._ui.lineedit_ivshmem_virt_addr.setText(
            to_human_addr(guestcell.ivshmem_virt_addr()))
        self._ui.lineedit_comm_region.setText(
            to_human_addr(guestcell.comm_region()))

        rsc_cpu: ResourceCPU = guestcell.find(ResourceCPU)
        self._cpu_editor.set_cpu_count(rsc_cpu.cpu_count())
        self._cpu_editor.set_cpus(guestcell.cpus())

        self._update_devices(guestcell)
        self._update_pci_devices(guestcell)

        self._ui.combobox_console.clear()
        self._ui.combobox_console.addItem(self.not_use)
        for dev in guestcell.find(ResourceCPU).devices():
            if dev.name().startswith("uart"):
                self._ui.combobox_console.addItem(dev.name())
        console = guestcell.console()
        if console and len(console)>0:
            self._ui.combobox_console.setCurrentText(console)
        else:
            self._ui.combobox_console.setCurrentText(self.not_use)

        self._guestcell = guestcell

    def showEvent(self, event) -> None:
        self.set_guestcell(self._guestcell)
        return super().showEvent(event)

    def _update_devices(self, guestcell: ResourceGuestCell):
        cpu: ResourceCPU = guestcell.find(ResourceCPU)
        clean_layout(self._devices_layout)

        devices = guestcell.devices()
        for dev in cpu.devices():
            name = dev.name()
            w = SelectButton(name)
            w.setCheckable(True)
            if name in devices:
                w.setChecked(True)
            w.clicked.connect(self._on_device_changed)
            self._devices_layout.addWidget(w)

    def _on_console_changed(self, index):
        if self._guestcell is None:
            return

        name = self._ui.combobox_console.currentText()
        if name == self.not_use:
            self._guestcell.set_console('')
        else:
            self._guestcell.set_console(name)

    def _on_device_changed(self):
        if self._guestcell is None:
            return
        devices = list()
        for i in range(self._devices_layout.count()):
            w: QtWidgets.QPushButton = self._devices_layout.itemAt(i).widget()
            if w.isChecked():
                devices.append(w.text())
        self._guestcell.set_devices(devices)

    def _on_reset_addr_changed(self):
        if self._guestcell is None:
            return
        addr = from_human_num(self._ui.lineedit_reset_addr.text())
        if addr is None:
            self._ui.lineedit_reset_addr.setText(to_human_addr(self._guestcell.reset_addr()))
            return
        self._ui.lineedit_reset_addr.setText(to_human_addr(addr))
        if self._guestcell.reset_addr() != addr:
            self._guestcell.set_reset_addr(addr)

    def _update_pci_devices(self, guestcell: ResourceGuestCell):
        pci_devices: ResourcePCIDeviceList = guestcell.find(ResourcePCIDeviceList)
        clean_layout(self._pci_devices_layout)

        devices = guestcell.pci_deivces()
        for idx in range(pci_devices.device_count()):
            dev = pci_devices.device_at(idx)
            if dev is None:
                break
            name = dev.path()
            w = SelectButton(name)
            w.setCheckable(True)
            if name in devices:
                w.setChecked(True)
            w.clicked.connect(self._on_pci_device_changed)
            self._pci_devices_layout.addWidget(w)

    def _on_pci_device_changed(self):
        if self._guestcell is None:
            return
        devices = list()
        for i in range(self._pci_devices_layout.count()):
            w: QtWidgets.QPushButton = self._pci_devices_layout.itemAt(i).widget()
            if w.isChecked():
                devices.append(w.text())
        self._guestcell.set_pci_devices(devices)

    def _on_sysmem_changed(self):
        if self._guestcell is None:
            return
        mmaps = self._sysmem_widget.get_value()
        self.logger.debug(f"set system memory: {mmaps}")
        self._guestcell.set_system_mem(mmaps)

    def _on_memmaps_changed(self):
        if self._guestcell is None:
            return
        mmaps = self._mmaps_widget.get_value()
        self.logger.debug(f"set memmaps: {mmaps}")
        self._guestcell.set_memmaps(mmaps)

    def _on_name_edit_finished(self):
        if self._guestcell is None:
            return

        new_name = self._ui.linedit_name.text().strip()
        if new_name == self._guestcell.name():
            return

        self._ui.linedit_name.blockSignals(True)

        if ResourceGuestCell.check_name(new_name):
            self._guestcell.set_name(new_name)
            # 内容清空，重新设置内容
            self._ui.linedit_name.setText(self._guestcell.name())
            set_lineedit_status(self._ui.linedit_name, True)

        self._ui.linedit_name.blockSignals(False)

    def _on_name_changed(self, text):
        if self._guestcell is None:
            return
        set_lineedit_status(self._ui.linedit_name, ResourceGuestCell.check_name(text))

    def _on_arch_change(self):
        if self._guestcell is None:
            return
        if self._ui.radiobtn_aarch32.isChecked():
            self._guestcell.set_arch(ARMArch.AArch32)
        if self._ui.radiobtn_aarch64.isChecked():
            self._guestcell.set_arch(ARMArch.AArch64)

    def _on_virt_console_changed(self):
        if self._guestcell is None:
            return
        self._guestcell.set_virt_console_enable(
            self._ui.btn_virtual_console.isChecked())

    def _on_virt_cpuid_changed(self):
        if self._guestcell is None:
            return
        self._guestcell.set_virt_cpuid_enable(
            self._ui.btn_use_virt_cpuid.isChecked())

    def _on_ivshmem_addr_changed(self):
        if self._guestcell is None:
            return

        value = from_human_num(self._ui.lineedit_ivshmem_virt_addr.text())
        if value is None:
            # 输入内容有误，还原值
            self._ui.lineedit_ivshmem_virt_addr.setText(
                to_human_addr(self._guestcell.ivshmem_virt_addr()))
            return
        self._guestcell.set_ivshmem_virt_addr(value)

    def _on_comm_region_changed(self):
        if self._guestcell is None:
            return
        value = from_human_num(self._ui.lineedit_comm_region.text())
        if value is None:
            # 输入内容有误，还原值
            self._ui.lineedit_comm_region.setText(
                to_human_addr(self._guestcell.comm_region()))
            return
        self._guestcell.set_comm_region(value)

    def _on_cpus_changed(self):
        if self._guestcell is None:
            return
        selected_cpus = self._cpu_editor.get_cpus()
        self._guestcell.set_cpus(selected_cpus)
        self._on_cpus_updated(selected_cpus)  # 触发JSON更新和RPC发送

    def _on_cpus_updated(self, selected_cpus):
        """当CPU配置变化时更新JSON文件并发送到RPC服务器"""
        if not selected_cpus:
            return
            
        try:
            # 1. 加载JSON模板
            json_config = JSONConfigUpdater.load_json_template(self._json_template_path)
            
            # 2. 更新cpus字段
            updated_config = JSONConfigUpdater.update_cpu_field(json_config, selected_cpus)
            
            # 3. 保存更新后的JSON
            if JSONConfigUpdater.save_updated_json(updated_config, self._output_json_path):
                # 4. 发送到RPC服务器
                self._send_json_to_rpc(self._output_json_path)
        except Exception as e:
            self.logger.error(f"CPU配置更新失败: {str(e)}")
            QtWidgets.QMessageBox.warning(self, "配置错误", f"更新CPU配置失败: {str(e)}")

    def _send_json_to_rpc(self, file_path):
        """将JSON文件发送到RPC服务器"""
        try:
            # 读取文件内容
            with open(file_path, 'r') as f:
                config_content = f.read()
            
            # 创建RPC客户端并发送
            client = RPCClient(self._rpc_server_addr)
            result = client.call("save_config", config_content)
            
            if result.get("success", False):
                self.logger.info("JSON配置已成功发送到RPC服务器")
                QtWidgets.QMessageBox.information(self, "成功", "CPU配置已更新并发送到目标板")
            else:
                self.logger.error(f"RPC服务器返回错误: {result.get('error', '未知错误')}")
                QtWidgets.QMessageBox.warning(self, "失败", f"发送配置失败: {result.get('error', '未知错误')}")
                
        except Exception as e:
            self.logger.error(f"发送JSON到RPC服务器失败: {str(e)}")
            QtWidgets.QMessageBox.warning(self, "错误", f"连接RPC服务器失败: {str(e)}")
