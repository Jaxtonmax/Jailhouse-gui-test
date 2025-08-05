import logging
import os 
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
# 修正RPC客户端导入（根据项目实际情况调整）
# from rpc_client import RPCClient  # 假设RPCClient位于rpc_client模块
from rpc_server import rpc_client
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
        self._rpc_server_addr = "tcp://192.168.1.27:4240"            # 替换为实际RPC地址

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
        # --- 在这个方法中实现模板加载 ---
        if self._guestcells is None:
            return
        guestcell = self._guestcells.cell_at(row)
        if guestcell is None:
            return
            
        # --- 现有逻辑保持 ---
        self._ui.label_guestcell_name.setText(guestcell.name())
        self._ui.btn_remove_cell.setEnabled(True)
        self._ui.frame_guestcell_content.show()
        
        # +++ 新增：加载模板的逻辑 +++
        cell_name = guestcell.name().lower() # 转为小写以匹配
        template_key = None
        
        # 根据cell名称或其他标识符来决定加载哪个模板
        if "linux" in cell_name:
            template_key = "linux"
        elif "rtthread" in cell_name:
            template_key = "rtthread"
        elif "acore" in cell_name:
            template_key = "acore"
            
        if template_key:
            template_path = self._config_template_map.get(template_key)
            if template_path and os.path.exists(template_path):
                try:
                    with open(template_path, 'r') as f:
                        self._active_config_data = json.load(f)
                    self.logger.info(f"已成功加载模板: {template_path}")
                    # 将加载的配置数据传递给子组件以更新UI
                    self._guestcell_widget.set_config_data(self._active_config_data)
                except Exception as e:
                    self.logger.error(f"加载配置文件 {template_path} 失败: {e}")
                    self._active_config_data = None
            else:
                self.logger.warning(f"未找到模板文件: {template_path}")
                self._active_config_data = None
        else:
            self.logger.warning(f"无法根据cell名称 '{cell_name}' 确定要加载的配置模板。")
            self._active_config_data = None

    # +++ 新增槽函数，用于接收子组件的更新 +++
    @QtCore.Slot(dict)
    def _on_guest_config_changed(self, updated_config: dict):
        """
        当子组件发出配置更改信号时，更新内存中的主配置。
        """
        self.logger.info("接收到子组件的配置更新...")
        self._active_config_data = updated_config

    # +++ 新增部署方法，替代旧的启动逻辑 +++
    def deploy_and_run_config(self):
        """
        将当前内存中的配置发送到目标板并执行启动命令。
        """
        if not self._active_config_data:
            QtWidgets.QMessageBox.critical(self, "错误", "没有活动的配置可以部署！")
            return
            
        self.logger.info(f"准备部署配置: {self._active_config_data.get('name')}")
        
        # 1. 将配置字典转换为JSON字符串
        final_config_str = json.dumps(self._active_config_data, indent=4)
        
        # 2. 通过RPC将字符串发送到目标板
        #    这需要你在RPC服务器端有一个可以接收文件内容的方法
        rpc_client = RPCClient.get_instance()
        if not rpc_client.is_connected():
            QtWidgets.QMessageBox.warning(self, "警告", "RPC未连接，无法部署！")
            return
            
        # 假设服务器端有一个叫 `upload_config_file` 的方法
        # 它接收两个参数：文件内容和要保存的远程路径
        remote_path = "/root/threevms/config.json"
        result = rpc_client.call('upload_config_file', final_config_str, remote_path)
        
        if not result or not result.status:
            msg = result.message if result else "RPC调用失败"
            QtWidgets.QMessageBox.critical(self, "部署失败", f"上传配置文件失败: {msg}")
            return
            
        self.logger.info(f"配置文件已成功上传到: {remote_path}")
        
        # 3. 执行启动命令
        #    现在启动命令非常简单，因为它总是使用同一个配置文件
        self.logger.info("正在执行启动命令...")
        # 假设启动方法在RPC客户端中叫 `start_vm_from_config`
        start_result = rpc_client.call('start_vm_from_config', remote_path)
        if not start_result or not start_result.status:
             msg = start_result.message if start_result else "RPC调用失败"
             QtWidgets.QMessageBox.critical(self, "启动失败", f"启动虚拟机失败: {msg}")
        else:
             QtWidgets.QMessageBox.information(self, "成功", "虚拟机已成功启动！")

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
    config_changed = QtCore.Signal(dict)

    def __init__(self, parent=None):
        super().__init__(parent)
        # 初始化UI布局框架（只执行一次）
        self._ui = Ui_GuestCellWidget()
        self._ui.setupUi(self)
        
        # +++ 新增属性 +++
        self._active_config_data = None  # 用于保存当前加载的配置字典
        
        # 定义OS类型和模板文件的映射关系
        # 你需要根据你的UI来决定如何获取当前选择的OS类型
        # 这里我们假设有一个下拉列表或者通过cell的名称来判断
        self._config_template_map = {
            "linux": "configs/linux_guest_config.json",
            "rtthread": "configs/rtthread_guest_config.json",
            "acore": "configs/acore_guest_config.json"
        }

        # 连接子组件的信号到新的处理槽
        self._guestcell_widget.config_changed.connect(self._on_guest_config_changed)

        # 优先初始化其他组件（确保基础属性被初始化）
        self._init_other_components()  # 移到此处
        if self._cpu_editor:
            self._cpu_editor.cpus_changed.connect(self._on_cpus_changed)
        # 初始化_cpu_editor（现在在其他组件之后）
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
        
        # 绑定信号（确保在_cpu_editor初始化后）
        self._cpu_editor.cpus_changed.connect(self._on_cpus_changed)
        self.logger.debug("GuestCellWidget初始化完成")

    def _init_tcp_communicator(self):
        """初始化TCP通信实例（RPCClient）并连接服务器"""
        try:
            # 获取RPCClient单例
            self._tcp_communicator = RPCClient.get_instance()
            
            # 检查是否已连接，未连接则使用已定义的服务器地址连接
            if not self._tcp_communicator.is_connected():
                if not self._rpc_server_addr:
                    self.logger.error("RPC服务器地址未配置")
                    return False
                
                # 连接服务器（确保RPCClient的connect方法实现正确）
                connect_result = self._tcp_communicator.connect(self._rpc_server_addr)
                if connect_result:
                    self.logger.debug(f"已连接到RPC服务器: {self._rpc_server_addr}")
                else:
                    self.logger.error(f"连接RPC服务器失败: {self._rpc_server_addr}")
                    self._tcp_communicator = None  # 连接失败则清空实例
                    return False
            return True
        except Exception as e:
            self.logger.error(f"初始化TCP通信实例失败: {str(e)}")
            self._tcp_communicator = None
            return False

    def _init_other_components(self):
        """初始化其他组件（与CPU编辑器无关的部分）"""
        self._ui.combobox_console.setView(QtWidgets.QListView())

        # 初始化属性（优先定义RPC地址，确保连接时可用）
        self._guestcell: Optional[ResourceGuestCell] = None
        self._json_template_path = "/home/wzm/work/Jailhouse-gui/template.json"
        self._output_json_path = "/home/wzm/work/Jailhouse-gui/dist/config.json"
        self._rpc_server_addr = "tcp://192.168.1.27:4240"  # RPC服务器地址（提前定义，确保连接时已赋值）

        # 初始化TCP通信实例（使用RPCClient单例，与VMManageWidget保持一致）
        try:
            # 修正导入路径：根据项目结构，RPCClient应直接来自rpc_client模块（参考VMManageWidget的导入方式）
            from rpc_server.rpc_client import RPCClient  
            self._tcp_communicator = RPCClient.get_instance()
            self.logger.debug("成功获取RPCClient单例实例")
        except ImportError as e:
            self.logger.error(f"导入RPCClient失败: {str(e)}，请检查模块路径是否正确")
            self._tcp_communicator = None
            # 此处不抛出异常，避免阻断其他组件初始化，但需记录严重错误
            QtWidgets.QMessageBox.critical(self, "模块错误", f"无法导入RPC客户端模块: {str(e)}")
            return
        except Exception as e:
            self.logger.error(f"初始化RPCClient实例失败: {str(e)}")
            self._tcp_communicator = None
            return

        # 尝试连接RPC服务器（使用已提前定义的地址）
        if self._tcp_communicator and not self._tcp_communicator.is_connected():
            try:
                # 连接前检查地址有效性
                if not self._rpc_server_addr.startswith(("tcp://", "ipc://")):
                    raise ValueError(f"无效的RPC地址格式: {self._rpc_server_addr}，应为tcp://或ipc://开头")
                
                connect_result = self._tcp_communicator.connect(self._rpc_server_addr)
                if connect_result:  # 假设connect()返回布尔值表示成功与否
                    self.logger.debug(f"成功连接到RPC服务器: {self._rpc_server_addr}")
                else:
                    self.logger.warning(f"连接RPC服务器返回失败（无具体异常）: {self._rpc_server_addr}")
            except Exception as e:
                self.logger.error(f"连接RPC服务器[{self._rpc_server_addr}]失败: {str(e)}")
                # 不阻断初始化，但提示用户
                QtWidgets.QMessageBox.warning(self, "连接提示", f"RPC服务器连接失败: {str(e)}")

        # 监听连接状态变化（与RemoteWidget保持一致的状态同步逻辑）
        if self._tcp_communicator:
            self._tcp_communicator.state_changed.connect(self._on_tcp_state_changed)

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
        TipMgr.add(self._ui.frame_pci_devices, tip_pci)

    def _on_tcp_state_changed(self, sender):
        """处理TCP连接状态变化的回调（与RemoteWidget逻辑一致）"""
        if sender is not self._tcp_communicator:
            return
        if self._tcp_communicator.is_connected():
            self.logger.info(f"RPC服务器连接已建立: {self._rpc_server_addr}")
        else:
            self.logger.warning(f"RPC服务器连接已断开: {self._rpc_server_addr}")

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

    # +++ 新增一个方法，用于从父组件接收配置字典 +++
    def set_config_data(self, config_data: dict):
        """
        从一个配置字典加载数据并更新所有UI控件。
        """
        if not config_data:
            self.logger.warning("接收到空的配置数据，无法更新UI")
            return
            
        self._current_config = config_data  # 在内存中保存当前配置

        # 更新UI控件
        self._ui.linedit_name.setText(config_data.get("name", ""))
        
        arch = config_data.get("arch", "arm64")
        self._ui.radiobtn_aarch64.setChecked(arch == "arm64")
        self._ui.radiobtn_aarch32.setChecked(arch == "aarch32")
        
        # 更新CPU编辑器
        if self._cpu_editor:
            rsc_cpu: ResourceCPU = self._guestcell.find(ResourceCPU) # 假设还能获取到CPU总数
            self._cpu_editor.set_cpu_count(rsc_cpu.cpu_count())
            self._cpu_editor.set_cpus(set(config_data.get("cpus", [])))
            
        # ... 更新其他UI控件，如内存、设备等 ...
        # self._sysmem_widget.set_mmaps(...)
        self.logger.info(f"UI已根据配置 '{config_data.get('name')}' 更新。")

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

    # def _on_cpus_changed(self):
    #     """处理CPU选择变化的回调方法（更新并保存配置文件）"""
    #     if self._guestcell is None:
    #         return
        
    #     # 获取当前选中的CPU
    #     selected_cpus = self._cpu_editor.get_cpus()
    #     self.logger.debug(f"CPU配置变化: {selected_cpus}")
        
    #     # 1. 更新guestcell的CPU配置
    #     self._guestcell.set_cpus(selected_cpus)
        
    #     # 2. 生成并保存配置文件
    #     try:
    #         # 加载模板并更新CPU配置
    #         json_template = JSONConfigUpdater.load_json_template(self._json_template_path)
    #         updated_config = JSONConfigUpdater.update_cpu_field(json_template, list(selected_cpus))
            
    #         # 保存到输出路径
    #         save_success = JSONConfigUpdater.save_updated_json(updated_config, self._output_json_path)
    #         if not save_success:
    #             self.logger.error("保存CPU配置文件失败，终止后续操作")
    #             return
    #         self.logger.info(f"CPU配置已保存到 {self._output_json_path}")
            
    #         # 3. 通过TCP通信实例发送配置（复用现有连接）
    #         if not self._tcp_communicator:
    #             self.logger.error("未初始化TCP通信实例，无法发送配置")
    #             return
            
    #         # 检查TCP连接状态（假设RPCClient实现了is_connected方法）
    #         if not self._tcp_communicator.is_connected():
    #             self.logger.error("TCP通信实例未连接，无法发送配置")
    #             return
            
    #         # 读取配置文件内容并发送
    #         with open(self._output_json_path, 'r') as f:
    #             config_content = f.read()
            
    #         # 调用RPC方法（返回Result对象，通过属性访问结果）
    #         result = self._tcp_communicator.update_cpu_config(config_content)
    #         if result and result.status:  # 直接访问Result的status属性
    #             self.logger.info("CPU配置已成功发送到目标板")
    #         else:
    #             # 访问Result的message属性获取错误信息
    #             self.logger.error(f"发送CPU配置失败: {result.message if result else '未知错误'}")
                
    #     except Exception as e:
    #         self.logger.error(f"处理CPU配置时出错: {str(e)}", exc_info=True)
        def _on_cpus_changed(self, selected_cpus: set):
        """
        当CPU选择变化时，只更新内存中的配置，并发出信号。
        """
        if hasattr(self, '_current_config') and self._current_config:
            self.logger.debug(f"CPU选择变化为: {selected_cpus}")
            # 更新内存中的字典
            self._current_config['cpus'] = sorted(list(selected_cpus))
            # 发出信号，将整个更新后的配置字典传递给父组件
            self.config_changed.emit(self._current_config)
        else:
            self.logger.warning("CPU发生变化，但没有当前配置可更新。")