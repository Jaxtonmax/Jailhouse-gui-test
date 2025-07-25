import os
import logging
from hashlib import md5

from PySide2 import QtWidgets, QtCore
from forms.ui_remote_widget import Ui_RemoteWidget
from forms.ui_acoreOs_source_config import Ui_Form_acoreOS
from forms.ui_root_cell_config import Ui_Form_root

from rpc_server.rpc_client import RPCClient
from generator import RootCellGenerator, GuestCellGenerator
from jh_resource import Resource, ResourceGuestCellList, ResourceGuestCell
from jh_resource import ResourceMgr, ResourceSignals
from utils import from_human_num, Profile
from config_convert import ConfigConverter

class RemoteACoreWidget(QtWidgets.QWidget):
    # 配置文件项目，用于保存ACore相关设置
    profile_msl_run_addr = Profile.Item('acore_msl_run_addr', 0)
    profile_os_run_addr = Profile.Item('acore_os_run_addr', 0x80000000)
    profile_app_run_addr = Profile.Item('acore_run_app_addr', 0x82000000)
    profile_msl_enable = Profile.Item('acore_msl_enable', False)
    profile_os_enable = Profile.Item('acore_os_enable', False)
    profile_app_enable = Profile.Item('acore_run_enable', False)
    profile_msl_fn = Profile.Item('acore_msl_fn', "")
    profile_os_fn = Profile.Item('acore_os_fn', "")
    profile_app_fn = Profile.Item('acore_run_fn', "")

    logger = logging.getLogger("RemoteACoreWidget")
    def __init__(self, parent=None):
        """
        初始化ACore配置界面。
        
        创建ACore操作系统相关配置的界面组件，并连接相关信号与槽。
        
        Args:
            parent: 父窗口部件，默认为None。
        """
        # 初始化ACore配置界面
        super().__init__(parent)
        self._ui = Ui_Form_acoreOS()
        self._ui.setupUi(self)

        self._client: RPCClient = RPCClient.get_instance()

        # 连接信号和事件处理
        ResourceSignals.current_rsc.connect(self._on_current_rsc_changed)
        self._ui.comboBox_cell_name.installEventFilter(self)

        self._ui.pushButton_start.clicked.connect(self._on_guest_cell_start_connect)
        self._ui.pushButton_stop.clicked.connect(self._on_guest_cell_stop_connect)

        self._ui.btn_select_file_1.clicked.connect(self.select_msl_file)
        self._ui.btn_select_file_2.clicked.connect(self.select_os_file)
        self._ui.btn_select_file_3.clicked.connect(self.select_app_file)

        self._ui.checkBox_msl.clicked.connect(self._on_checkbox_msl_connect)
        self._ui.checkBox_os.clicked.connect(self._on_checkbox_os_connect)
        self._ui.checkBox_app.clicked.connect(self._on_checkbox_app_connect)

        # 初始化界面显示
        self._ui.lineEdit_msl_run_addr.setText(hex(self.profile_msl_run_addr.get()))
        self._ui.lineEdit_os_run_addr.setText(hex(self.profile_os_run_addr.get()))
        self._ui.lineEdit_app_run_addr.setText(hex(self.profile_app_run_addr.get()))
        self._ui.lineEdit_select_msl_file.setText(self.profile_msl_fn.get())
        self._ui.lineEdit_select_os_file.setText(self.profile_os_fn.get())
        self._ui.lineEdit_select_app_file.setText(self.profile_app_fn.get())
        self._ui.checkBox_msl.setChecked(self.profile_msl_enable.get())
        self._ui.checkBox_os.setChecked(self.profile_os_enable.get())
        self._ui.checkBox_app.setChecked(self.profile_app_enable.get())

    def eventFilter(self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool:
        """
        事件过滤器，用于处理特定组件的事件。
        
        当鼠标点击下拉菜单时更新单元格列表。
        
        Args:
            watched: 被监视的对象。
            event: 发生的事件。
            
        Returns:
            bool: 如果事件被处理则返回True，否则返回False。
        """
        # 事件过滤器，处理鼠标点击事件时更新单元格列表
        if event.type() == QtCore.QEvent.MouseButtonPress:
            rsc = ResourceMgr.get_instance().get_current()
            if rsc is None:
                return False
            self._update_cell_list(rsc)
        return False

    def _on_checkbox_msl_connect(self):
        """
        处理MSL复选框状态变化。
        
        当用户点击MSL复选框时，更新相应的配置项。
        """
        # 处理MSL复选框状态变化
        self.profile_msl_enable.set(self._ui.checkBox_msl.isChecked())

    def _on_checkbox_os_connect(self):
        """
        处理OS复选框状态变化。
        
        当用户点击OS复选框时，更新相应的配置项。
        """
        # 处理OS复选框状态变化
        self.profile_os_enable.set(self._ui.checkBox_os.isChecked())

    def _on_checkbox_app_connect(self):
        """
        处理APP复选框状态变化。
        
        当用户点击APP复选框时，更新相应的配置项。
        """
        # 处理APP复选框状态变化
        self.profile_app_enable.set(self._ui.checkBox_app.isChecked())

    def select_msl_file(self):
        """
        选择MSL文件。
        
        打开文件选择对话框，让用户选择MSL二进制文件，并更新界面和配置。
        """
        # 选择MSL文件的对话框
        file_name = QtWidgets.QFileDialog.getOpenFileName(None, "打开文件", "", "*.bin")[0]
        self._ui.lineEdit_select_msl_file.setText(file_name)
        self.profile_msl_fn.set(file_name)

    def select_os_file(self):
        """
        选择OS文件。
        
        打开文件选择对话框，让用户选择OS二进制文件，并更新界面和配置。
        """
        # 选择OS文件的对话框
        file_name = QtWidgets.QFileDialog.getOpenFileName(None, "打开文件", "", "*.bin")[0]
        self._ui.lineEdit_select_os_file.setText(file_name)
        self.profile_os_fn.set(file_name)

    def select_app_file(self):
        """
        选择APP文件。
        
        打开文件选择对话框，让用户选择APP二进制文件，并更新界面和配置。
        """
        # 选择APP文件的对话框
        file_name = QtWidgets.QFileDialog.getOpenFileName(None, "打开文件", "", "*.bin")[0]
        self._ui.lineEdit_select_app_file.setText(file_name)
        self.profile_app_fn.set(file_name)

    def _on_guest_cell_start_connect(self):
        """
        启动客户单元格。
        
        根据用户配置，生成客户单元格配置，加载固件，并启动单元格。
        此过程包括检查固件配置、生成单元格配置、创建单元格、加载固件和启动单元格。
        """
        # 启动客户单元格
        self.logger.debug("start guest cell ")
        rscmgr = ResourceMgr.get_instance()
        rsc = rscmgr.get_current()
        if rsc is None:
            return

        # 获取当前选中的单元格
        celllist: ResourceGuestCellList = rsc.find(ResourceGuestCellList)
        cellname = self._ui.comboBox_cell_name.currentText()
        cell = celllist.find_cell(cellname)
        if cell is None:
            self.logger.error(f"cell {cellname} not found")
            return

        # 准备固件配置
        firmwares = {
            "msl": {
                "enable": self._ui.checkBox_msl.isCheckable(),
                "addr"  : from_human_num(self._ui.lineEdit_msl_run_addr.text().strip()),
                "file"  : self._ui.lineEdit_select_msl_file.text().strip(),
            },
            "os": {
                "enable": self._ui.checkBox_os.isCheckable(),
                "addr"  : from_human_num(self._ui.lineEdit_os_run_addr.text().strip()),
                "file"  : self._ui.lineEdit_select_os_file.text().strip(),
            },
            "app":{
                "enable": self._ui.checkBox_app.isCheckable(),
                "addr"  : from_human_num(self._ui.lineEdit_app_run_addr.text().strip()),
                "file"  : self._ui.lineEdit_select_app_file.text().strip(),
            }
        }

        # 验证固件配置
        for name, fw in firmwares.items():
            if fw['enable'] and (fw['addr'] is None or not os.path.exists(fw['file'])):
                self.logger.error(f"[{name}] invalid addr or filename")
                return

        # 生成当前guest cell的配置
        self.logger.info(f"generate cell({cellname}) config")
        guest_cell_bin = GuestCellGenerator.gen_config_bin(cell)
        if guest_cell_bin is None:
            self.logger.error(f"generate cell config failed")
            return

        try:
            guest_config = ConfigConverter.convert_guest_cell(rsc, cell)
            save_path = ConfigConverter.save_config(
                guest_config, 
                f"guest_cell_{guest_config['zone_id']}_{cellname}.json"
            )
            self.logger.info(f"客户单元格配置文件已生成: {save_path}")
        except Exception as e:
            self.logger.warning(f"生成客户单元格配置文件失败: {str(e)}")

        # 创建之前先查询列表，有无此cell,若有就销毁
        cell_exist = False
        result = self._client.list_cell()
        if result is None or not result.result:
            self.logger.error("get cell list failed")
            return
        self.logger.debug("jailhouse cll list: " + str(result.result))
        for cell in result.result:
            if cell['name'] == cellname:
                cell_exist = True
                break
        if cell_exist:
            self.logger.info(f"destroy cell({cellname})")
            if not self._client.destroy_cell(cellname):
                self.logger.debug(f"destroy cell({cellname}) failed")
                return

        # 创建guest cell
        self.logger.info(f'create cell({cellname})')
        result = self._client.create_cell(guest_cell_bin)
        if not result.status:
            self.logger.error(f"create guest cell failed {result.message}")
            return

        # 加载每个固件
        for name, fw in firmwares.items():
            if not fw['enable']:
                continue

            self.logger.info(f"load firmware {name} for cell({cellname}) @{hex(fw['addr'])}")
            try:
                with open(fw['file'], 'rb') as f:
                    fw_bin = f.read()
            except:
                self.logger.error(f"read {fw['file']} failed.")
                return

            self.logger.info(f"md5: {md5(fw_bin).hexdigest()}")
            result = self._client.load_cell(cellname, fw['addr'], fw_bin )
            if result is None or not result.status:
                self.logger.error(f"load failed")
                return

        # 启动单元格
        self.logger.info(f"start cell({cellname})")
        result = self._client.start_cell(cellname)
        if result is None or not result.status:
            self.logger.error(f"start cell({cellname}) failed")
            return

        self.logger.info(f"run cell{cellname} success.")

    def _on_guest_cell_stop_connect(self):
        """
        停止客户单元格。
        
        停止并销毁当前选中的客户单元格。
        此过程包括获取单元格列表，查找目标单元格，并调用销毁操作。
        """
        # 停止客户单元格
        # 获取当前的comboBox选中的值
        current_text = self._ui.comboBox_cell_name.currentText()
        # 查询列表
        result = self._client.list_cell()
        if result is None:
            self.logger.debug("get guest cell list failed")
            return
        if not result.status:
            self.logger.debug("get guest cell list failed")
            return
        # 查找guest cell
        for cell in result.result:
            if cell['name'] == current_text:
                self.logger.debug(f"destroy {current_text}...")
                if not self._client.destroy_cell(current_text):
                    self.logger.debug(f"destroy {current_text} failed")
                    return
        # 销毁
        self._client.destroy_cell(current_text)
        self.logger.debug(f"destroy {current_text} success")

    def _on_current_rsc_changed(self, sender, **kwargs):
        """
        处理当前资源改变事件。
        
        当资源发生变化时，更新单元格列表。
        
        Args:
            sender: 信号发送者。
            **kwargs: 包含资源信息的关键字参数。
        """
        # 资源改变时更新单元格列表
        rsc = kwargs.get('rsc')
        self._update_cell_list(rsc)

    def _update_cell_list(self, rsc: Resource):
        """
        更新单元格列表。
        
        根据当前资源更新下拉列表中的单元格选项。
        
        Args:
            rsc: 资源对象，包含单元格列表信息。
        """
        # 更新单元格列表
        if rsc is None:
            return

        current = self._ui.comboBox_cell_name.currentText()
        self._ui.comboBox_cell_name.clear()
        cell_list: ResourceGuestCellList = rsc.find(ResourceGuestCellList)
        for i in range(cell_list.cell_count()):
            cell: ResourceGuestCell = cell_list.cell_at(i)
            cell_name = cell.name()
            self._ui.comboBox_cell_name.addItem(cell_name)
            if current == cell_name:
                self._ui.comboBox_cell_name.setCurrentIndex(i)


class RemoteRootWidget(QtWidgets.QWidget):
    # 根单元格配置界面
    logger = logging.getLogger("RemoteRootWidget")
    def __init__(self, parent=None):
        """
        初始化根单元格配置界面。
        
        创建用于配置和管理根单元格的界面组件。
        
        Args:
            parent: 父窗口部件，默认为None。
        """
        super().__init__(parent)
        self._ui = Ui_Form_root()
        self._ui.setupUi(self)

        self._client: RPCClient = RPCClient.get_instance()

        self._ui.pushButton_start.clicked.connect(self._on_root_cell_start_connect)
        self._ui.pushButton_stop.clicked.connect(self._on_root_cell_destory_connect)

    def _on_root_cell_start_connect(self):
        """
        启动根单元格。
        
        生成根单元格配置，并启用Jailhouse虚拟化系统。
        此过程包括获取资源，生成配置，检查现有单元格，以及启用Jailhouse。
        """
        # 启动根单元格
        # 获取root cell的资源
        rscmgr = ResourceMgr.get_instance()
        rsc = rscmgr.get_current()
        if rsc is None:
            self.logger.error("ResourceMgr failed")
            return

        # 生成配置
        root_cell_bin = RootCellGenerator.gen_config_bin(rsc)
        if root_cell_bin is None:
            self.logger.error("root_cell_bin is None")
            return

        # 每次创建前先销毁
        result = self._client.list_cell()
        if result is None or not result.status:
            self.logger.error("get root cell list failed")
            return
        for cell in result.result:
            if cell['id'] == 0:
                self.logger.debug(f"jailhouse disable")
                result = self._client.jailhouse_disable()
                if not result.status:
                    self.logger.debug("disable failed")
                    return
                break

        # 创建root cell
        result = self._client.jailhouse_enable(root_cell_bin)
        if not result.status:
            self.logger.error("jailhouse_enable failed")
            self.logger.error(f"{result.message}")
            return
        self.logger.info("jailhouse root cell enable success")

    def _on_root_cell_destory_connect(self):
        """
        销毁根单元格。
        
        禁用Jailhouse虚拟化系统，从而销毁根单元格。
        此过程包括获取单元格列表和禁用Jailhouse。
        """
        # 销毁根单元格
        # 先获取列表
        result = self._client.list_cell()
        if not result.status or result is None:
            self.logger.error("get root cell list failed")
            return
        result = self._client.jailhouse_disable()
        if not result.status:
            self.logger.error("get root cell list failed")
            return
        self.logger.debug("root cell disable success")

class RemoteWidget(QtWidgets.QWidget):
    # 远程控制主界面
    logger = logging.getLogger("RemoteWidget")

    profile_addr = Profile.Item('remote_addr', 'tcp://127.0.0.1:4240')

    def __init__(self, parent=None):
        """
        初始化远程控制主界面。
        
        创建远程控制界面，包含连接服务器的功能和不同的单元格管理标签页。
        
        Args:
            parent: 父窗口部件，默认为None。
        """
        super().__init__(parent)
        self._ui = Ui_RemoteWidget()
        self._ui.setupUi(self)

        self._ui.lineedit_addr.setText(self.profile_addr.get())

        self._client: RPCClient = RPCClient.get_instance()

        # 创建子页面
        self.table_root = RemoteRootWidget(self)
        self.table_acoreos = RemoteACoreWidget(self)

        # 添加标签页
        self._ui.tabWidget.addTab(self.table_root, "Root Cell")
        self._ui.tabWidget.addTab(self.table_acoreos, "AcoreOs")

        # 连接信号
        self._client.state_changed.connect(self._on_state_changed)

        self._ui.lineedit_addr.editingFinished.connect(self._on_addr_edit_finished)
        self._ui.btn_connect.clicked.connect(self._on_connect)

    def _on_addr_edit_finished(self):
        """
        处理地址编辑完成事件。
        
        当用户编辑服务器地址完成时，保存地址到配置。
        """
        # 地址编辑完成时保存地址
        self.profile_addr.set(self._ui.lineedit_addr.text().strip())

    def _on_state_changed(self, sender):
        """
        处理连接状态变化事件。
        
        当RPC客户端连接状态改变时，更新界面显示。
        
        Args:
            sender: 信号发送者，应为RPC客户端实例。
        """
        # 连接状态改变时更新界面
        if sender is not self._client:
            return

        if self._client.is_connected():
            self._ui.btn_connect.setChecked(True)
            self._ui.btn_connect.setText("断开")
        else:
            self._ui.btn_connect.setChecked(False)
            self._ui.btn_connect.setText("连接")

    def _on_connect(self):
        """
        处理连接按钮点击事件。
        
        根据当前连接状态，连接到或断开与远程服务器的连接。
        """
        # 连接或断开服务器
        if not self._client.is_connected():
            if not self._client.connect(self._ui.lineedit_addr.text().strip()):
                self.logger.error("连接失败")
        else:
            self._client.close()

