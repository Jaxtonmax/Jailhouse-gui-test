import logging
from typing import Optional
import time
import json
import math

from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtCharts import QtCharts
from forms.ui_vm_manager import Ui_VMManageWidget
from forms.ui_vm_state_item import Ui_VMStateItemWidget
from forms.ui_meminfo import Ui_MemInfoWidget
from forms.ui_cpuload import Ui_CPULoadWidget

from rpc_server.rpc_client import RPCClient
from generator import RootCellGenerator
from jh_resource import Resource, ResourceGuestCellList, ResourceGuestCell, ResourceCPU
from jh_resource import LinuxRunInfo, ACoreRunInfo, CommonOSRunInfo
from utils import Profile

from commonos_runinfo import OSRunInfoWidget, CommonOSRunInfoWidget
from linux_runinfo import LinuxRunInfoWidget
from acore_runinfo import ACoreRunInfoWidget


class CellStateItemWidget(QtWidgets.QWidget):
    """
    单元格状态项部件。
    
    用于在列表中显示单元格的名称和运行状态。
    
    Attributes:
        _ui: 用户界面对象。
    """
    def __init__(self, name, parent=None):
        """
        初始化单元格状态项部件。
        
        Args:
            name: 单元格名称。
            parent: 父窗口部件，默认为None。
        """
        super().__init__(parent)

        self.setFixedHeight(40)
        self._ui = Ui_VMStateItemWidget()
        self._ui.setupUi(self)
        self._ui.label_name.setText(name)
        self._ui.label_state.setText('未知状态')

    def name(self):
        """
        获取单元格名称。
        
        Returns:
            str: 单元格名称。
        """
        return self._ui.label_name.text()

    def set_status(self, status: str):
        """
        设置单元格状态。
        
        Args:
            status: 单元格状态文本。
        """
        self._ui.label_state.setText(status)


class CPULoadWidget(QtWidgets.QWidget):
    """
    CPU负载显示部件。
    
    显示CPU负载的曲线图和当前负载值。
    
    Attributes:
        _ui: 用户界面对象。
        _layout: 图表布局。
        _axis_time: 时间轴。
        _axis_load: 负载轴。
        _chart: 图表对象。
        _series: 数据系列。
        _chartview: 图表视图。
    """
    def __init__(self, parent=None):
        """
        初始化CPU负载显示部件。
        
        创建图表、坐标轴和数据系列。
        
        Args:
            parent: 父窗口部件，默认为None。
        """
        super().__init__(parent)
        self._ui = Ui_CPULoadWidget()
        self._ui.setupUi(self)

        self._layout = self._ui.frame_chart.layout()
        if self._layout is None:
            self._layout = QtWidgets.QHBoxLayout(self._ui.frame_chart)

        self._axis_time = QtCharts.QDateTimeAxis()
        self._axis_time.setFormat("mm:ss")
        self._axis_time.setTitleText("Time")
        self._axis_time.setRange(QtCore.QDateTime.currentDateTime(), QtCore.QDateTime().currentDateTime().addSecs(10))
        self._axis_load = QtCharts.QValueAxis()
        self._axis_load.setTitleText("Load")
        self._axis_load.setRange(0, 1)

        self._chart = QtCharts.QChart()
        self._chart.addAxis(self._axis_time, QtCore.Qt.AlignBottom)
        self._chart.addAxis(self._axis_load, QtCore.Qt.AlignLeft)
        self._chart.setTitle("CPU负载")
        # self._chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

        self._series = QtCharts.QSplineSeries()
        self._chart.addSeries(self._series)
        self._series.setPointsVisible(True)
        a = self._series.attachAxis(self._axis_time)
        b = self._series.attachAxis(self._axis_load)

        self._chartview = QtCharts.QChartView(self._chart)
        self._chartview.setRenderHint(QtGui.QPainter.Antialiasing)
        self._layout.addWidget(self._chartview)

        self.setMinimumHeight(400)
        self._chart.setTheme(QtCharts.QChart.ChartTheme.ChartThemeBlueCerulean)

    def add_data(self, now_sec, load):
        """
        添加负载数据点。
        
        添加一个时间点的CPU负载数据，更新图表显示。
        
        Args:
            now_sec: 当前时间戳(秒)。
            load: CPU负载值(0-1之间的浮点数)。
        """
        now = QtCore.QDateTime.fromMSecsSinceEpoch(int(now_sec*1000))
        self._ui.label_load.setText(f"{load*100:.1f} %")
        self._series.append(now_sec*1000, load)
        if self._series.count() > 200:
            print(self._series.count())
            self._series.removePoints(0, self._series.count()-40)
        self._axis_time.setRange(now.addSecs(-30), now)
        self._chartview.update()

    def set_cpucount(self, count):
        """
        设置CPU核心数。
        
        更新显示的CPU核心数。
        
        Args:
            count: CPU核心数。
        """
        self._ui.label_count.setText(f"{count}")

    def reset(self):
        """
        重置图表。
        
        清空所有数据点。
        """
        self._series.clear()


class MemInfoWidget(QtWidgets.QWidget):
    """
    内存信息显示部件。
    
    显示内存使用情况的曲线图和当前内存使用值。
    
    Attributes:
        _ui: 用户界面对象。
        _layout: 图表布局。
        _axis_time: 时间轴。
        _axis_load: 内存使用率轴。
        _chart: 图表对象。
        _series: 数据系列。
        _chartview: 图表视图。
    """
    def __init__(self, parent=None):
        """
        初始化内存信息显示部件。
        
        创建图表、坐标轴和数据系列。
        
        Args:
            parent: 父窗口部件，默认为None。
        """
        super().__init__(parent)

        self._ui = Ui_MemInfoWidget()
        self._ui.setupUi(self)

        self._layout = self._ui.frame_chart.layout()
        if self._layout is None:
            self._layout = QtWidgets.QHBoxLayout(self._ui.frame_chart)

        self._axis_time = QtCharts.QDateTimeAxis()
        self._axis_time.setFormat("mm:ss")
        self._axis_time.setTitleText("Time")
        self._axis_load = QtCharts.QValueAxis()
        self._axis_load.setTitleText("Memory")
        self._axis_load.setRange(0, 1)

        self._chart = QtCharts.QChart()
        self._chart.addAxis(self._axis_time, QtCore.Qt.AlignBottom)
        self._chart.addAxis(self._axis_load, QtCore.Qt.AlignLeft)
        self._chart.setTitle("内存负载")
        # self._chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

        self._series = QtCharts.QSplineSeries()
        self._chart.addSeries(self._series)
        self._series.setPointsVisible(True)
        a = self._series.attachAxis(self._axis_time)
        b = self._series.attachAxis(self._axis_load)

        self._chartview = QtCharts.QChartView(self._chart)
        self._chartview.setRenderHint(QtGui.QPainter.Antialiasing)
        self._layout.addWidget(self._chartview)

        self.setMinimumHeight(400)
        self._chart.setTheme(QtCharts.QChart.ChartTheme.ChartThemeBlueCerulean)

    def add_data(self, now_sec, total, free):
        """
        添加内存数据点。
        
        添加一个时间点的内存使用数据，更新图表显示。
        
        Args:
            now_sec: 当前时间戳(秒)。
            total: 总内存大小(字节)。
            free: 可用内存大小(字节)。
        """
        def size_to_str(size):
            if size < 1024*1024:
                return f'{size/1024:.03f} KB'
            if size < 1024*1024*1024:
                return f'{size/1024/1024:.02f} MB'
            return f'{size/1024/1024/1024:.02f} GB'

        self._ui.label_total.setText(size_to_str(total))
        self._ui.label_free.setText(size_to_str(free))
        self._ui.label_load.setText(f'{(total-free)/total*100:.0f}%')

        now = QtCore.QDateTime.fromMSecsSinceEpoch(int(now_sec*1000))
        self._series.append(now_sec*1000, (total-free)/total)
        if self._series.count() > 200:
            print(self._series.count())
            self._series.removePoints(0, self._series.count()-40)
        self._axis_time.setRange(now.addSecs(-30), now)
        self._chartview.update()


class VMManageWidget(QtWidgets.QWidget):
    """
    虚拟机管理界面部件。
    
    提供虚拟机的监控和管理功能，包括启动/停止虚拟机、查看性能指标等。
    
    Attributes:
        _ui: 用户界面对象。
        _root_cpuload: CPU负载显示部件。
        _root_meminfo: 内存信息显示部件。
        _timer: 定时器，用于定期更新状态。
        _resource: 当前资源对象。
        _current_cell: 当前选中的客户单元格。
        _client: RPC客户端实例。
        _last_status: 上次获取的状态信息。
        _os_runinfo_desc: 操作系统运行信息描述列表。
        logger: 日志记录器。
        profile_addr: 远程地址配置项。
    """
    logger = logging.getLogger("VMManage")

    profile_addr = Profile.Item('remote_addr', 'tcp://127.0.0.1:4240')

    def __init__(self, parent=None):
        """
        初始化虚拟机管理界面部件。
        
        创建子部件、设置信号连接和初始化界面。
        
        Args:
            parent: 父窗口部件，默认为None。
        """
        super().__init__(parent)
        self._ui = Ui_VMManageWidget()
        self._ui.setupUi(self)
        self._ui.combobox_os_type.setView(QtWidgets.QListView())
        self._ui.frame_sd_img_content.hide()
        self._ui.frame_sd_img_title.hide()

        self._root_cpuload = CPULoadWidget()
        self._root_meminfo = MemInfoWidget()
        self._root_layout = QtWidgets.QVBoxLayout(self._ui.frame_rootcell_content)
        self._root_layout.addWidget(self._root_cpuload)
        self._root_layout.addWidget(self._root_meminfo)
        self._ui.frame_runcell.hide()

        self._timer = QtCore.QTimer()
        self._timer.setInterval(1000)
        self._timer.setSingleShot(False)

        self._ui.lineedit_addr.setText(self.profile_addr.get())
        self._commonos_runinfo = CommonOSRunInfoWidget(self)
        self._linux_runinfo = LinuxRunInfoWidget(self)
        self._acore_runinfo = ACoreRunInfoWidget(self)

        self._os_runinfo_desc = [
            {
                'name'   : 'CommonOS',
                'display': '通用系统',
                'class'  : CommonOSRunInfo,
                'widget' : self._commonos_runinfo,
            },
            {
                'name'   : 'Linux',
                'display': 'Linux',
                'class'  : LinuxRunInfo,
                'widget' : self._linux_runinfo,
            },
            {
                'name'   : 'Acore',
                'display': '天脉(单分区)',
                'class'  : ACoreRunInfo,
                'widget' : self._acore_runinfo,
            },
        ]

        for item in self._os_runinfo_desc:
            self._ui.stackedwidget_os_runinfo.addWidget(item['widget'])
            self._ui.combobox_os_type.addItem(item['display'])
            item['widget'].value_changed.connect(self._on_runinfo_value_changed)

        self._ui.stackedwidget_os_runinfo.setFixedHeight(0)

        self._resource: Optional[Resource] = None
        self._current_cell: Optional[ResourceGuestCell] = None
        self._client: RPCClient = RPCClient.get_instance()
        self._last_status = None

        self._client.state_changed.connect(self._on_state_changed)
        self._ui.lineedit_addr.editingFinished.connect(self._on_addr_edit_finished)
        self._ui.btn_connect.clicked.connect(self._on_connect)
        self._ui.combobox_os_type.currentIndexChanged.connect(self._on_os_type_changed)
        self._ui.listwidget_cells.currentRowChanged.connect(self._on_current_cell_changed)
        self._ui.btn_cell_run.clicked.connect(self._on_cell_run)
        self._ui.btn_cell_stop.clicked.connect(self._on_cell_stop)
        self._ui.btn_hyp_start.clicked.connect(self._on_hyp_start)
        self._ui.btn_hyp_stop.clicked.connect(self._on_hyp_stop)
        self._ui.btn_cell_flush.clicked.connect(self._on_cell_flush)

        self._timer.timeout.connect(self._on_timeout)

    def set_resource(self, rsc: Resource):
        """
        设置要管理的资源。
        
        更新虚拟机列表并显示资源信息。
        
        Args:
            rsc: 资源对象，如果为None则清空显示。
        """
        if self._resource is rsc:
            return
        self._resource = None
        self._current_cell = None

        self._ui.listwidget_cells.setCurrentRow(-1)
        self._update_vm_list(rsc)
        self._resource = rsc

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        """
        处理调整大小事件。
        
        当窗口大小改变时，调整操作系统运行信息部件的高度。
        
        Args:
            event: 调整大小事件对象。
        """
        super().resizeEvent(event)
        self._ui.stackedwidget_os_runinfo.setFixedHeight(self._ui.stackedwidget_os_runinfo.currentWidget().sizeHint().height())

    def showEvent(self, event: QtGui.QShowEvent) -> None:
        """
        处理显示事件。
        
        Args:
            event: 显示事件对象。
        """
        return super().showEvent(event)

    def hideEvent(self, event: QtGui.QHideEvent) -> None:
        """
        处理隐藏事件。
        
        Args:
            event: 隐藏事件对象。
        """
        return super().hideEvent(event)

    def _on_hyp_start(self):
        """
        处理启动虚拟机监控器事件。
        
        生成根单元格配置，启用Jailhouse，并启动UART服务器。
        """
        if self._resource is None:
            return

        # 生成源码
        root_cell_bin = RootCellGenerator.gen_config_bin(self._resource)
        if root_cell_bin is None:
            self.logger.error("root_cell_bin is None")
            return

        # 每次创建, 前先destroy
        result = self._client.list_cell()
        if result is None or not result.status:
            self.logger.error("get root cell list failed")
            return
        for cell in result.result:
            if cell['id'] == 0:
                self.logger.info(f"jailhouse disable")
                result = self._client.jailhouse_disable()
                if not result.status:
                    self.logger.error("disable failed")
                    return
                break

        # 开始创建root cell
        self.logger.info(f"jailhouse enable")
        result = self._client.jailhouse_enable(root_cell_bin)
        if not result.status:
            self.logger.error("jailhouse_enable failed")
            self.logger.error(f"{result.message}")
            return
        self.logger.info("jailhouse root cell enable success")

        jhr_obj = self._resource.to_dict()
        jhr_json = None
        if jhr_obj is not None:
            jhr_json = json.dumps(jhr_obj)
        if jhr_json is not None:
            result = self._client.start_uart_server(jhr_json)
            if not result:
                self.logger.warning(f"start uart server failed, {result.message}")
            else:
                self.logger.info("start uart server succes.")
        else:
            self.logger.warning(f"generate jhr json failed.")

    def _on_cell_flush(self):
        """
        处理刷新单元格列表事件。
        
        更新虚拟机列表显示。
        """
        if self._resource is None:
            return
        self._update_vm_list(self._resource)

    def _on_hyp_stop(self):
        """
        处理停止虚拟机监控器事件。
        
        禁用Jailhouse并停止UART服务器。
        """
        if self._resource is None:
            return

        result = self._client.list_cell()
        if not result.status or result is None:
            self.logger.error("get root cell list failed")
            return
        result = self._client.jailhouse_disable()
        if not result.status:
            self.logger.error("get root cell list failed")
            return
        self.logger.info("root cell disable success")

        result = self._client.stop_uart_server()
        if not result:
            self.logger.warning("stop uart server failed.")

    def _on_timeout(self):
        """
        处理定时器超时事件。
        
        定期从服务器获取状态信息，更新单元格状态和性能指标图表。
        """
        if self._resource is None:
            return
        if not self._client.is_connected():
            return

        result = self._client.get_status()
        if result:  # 只处理成功的结果
            status = result.result
            rootcell: dict = status.get('rootcell')
            guestcells = status.get('guestcells')
            timestamp = status.get('timestamp', time.time())

            if guestcells:
                for i in range(self._ui.listwidget_cells.count()):
                    item = self._ui.listwidget_cells.item(i)
                    item_widget: CellStateItemWidget = self._ui.listwidget_cells.itemWidget(item)
                    cell = guestcells.get(item_widget.name())
                    if cell is not None:
                        item_widget.set_status(cell['status'])
                    else:
                        item_widget.set_status("未创建")

            if rootcell:
                meminfo = rootcell.get('meminfo')
                cputimes = rootcell.get('cputimes')
                if meminfo is None:
                    return
                if cputimes is None:
                    return

                self._root_cpuload.set_cpucount(rootcell.get('cpucount', "?"))

            if self._last_status is not None:
                last_cputimes = self._last_status['rootcell']['cputimes']
                _user = last_cputimes['user'] - cputimes['user']
                _sys = last_cputimes['system'] - cputimes['system']
                _idle = last_cputimes['idle'] - cputimes['idle']
                # 确保分母不为零
                if _user + _sys + _idle != 0:
                    cpuload = (_user + _sys) / (_user + _sys + _idle)
                    self._root_cpuload.add_data(timestamp, cpuload)

            self._root_meminfo.add_data(timestamp, meminfo['total'], meminfo['available'])

        self._last_status = status

    def _on_cell_run(self):
        """
        处理运行单元格事件。
        
        根据当前选中单元格的操作系统类型，调用相应的运行方法。
        """
        if self._current_cell is None:
            return
        self._ui.btn_cell_run.setEnabled(False)
        os_runinfo = self._current_cell.runinfo().os_runinfo()
        if isinstance(os_runinfo, ACoreRunInfo):
            self._acore_runinfo.run(self._current_cell)
        elif isinstance(os_runinfo, LinuxRunInfo):
            self._linux_runinfo.run(self._current_cell)
        elif isinstance(os_runinfo, CommonOSRunInfo):
            self._commonos_runinfo.run(self._current_cell)
        else:
            self.logger.error(f'Unknown OS runinfo {type(os_runinfo)}')
        self._ui.btn_cell_run.setEnabled(True)

    def _on_cell_stop(self):
        """
        处理停止单元格事件。
        
        销毁当前选中的单元格。
        """
        if self._current_cell is None:
            return

        name = self._current_cell.name()
        self.logger.info(f"destroy cell {name}")
        self._client.destroy_cell(name)

    def _update_vm_list(self, rsc: Resource):
        """
        更新虚拟机列表。
        
        从资源中获取客户单元格列表，并更新列表显示。
        
        Args:
            rsc: 资源对象，如果为None则清空列表。
        """
        if rsc is None:
            self._ui.listwidget_cells.clear()
            return

        self._ui.listwidget_cells.clear()
        guestcells: ResourceGuestCellList = rsc.find(ResourceGuestCellList)
        for i in range(guestcells.cell_count()):
            cell = guestcells.cell_at(i)
            item = QtWidgets.QListWidgetItem()
            item.setData(QtCore.Qt.UserRole, cell.name())
            item_widget = CellStateItemWidget(cell.name())
            item.setSizeHint(item_widget.minimumSize())
            self._ui.listwidget_cells.addItem(item)
            self._ui.listwidget_cells.setItemWidget(item, item_widget)

        fixed_height = self._ui.listwidget_cells.sizeHintForRow(0) * self._ui.listwidget_cells.count()
        self._ui.listwidget_cells.setFixedHeight(fixed_height)

    def _update_current_cell(self, cell: ResourceGuestCell):
        """
        更新当前选中的单元格。
        
        显示选中单元格的配置信息和运行信息。
        
        Args:
            cell: 客户单元格对象，如果为None则隐藏单元格配置区域。
        """
        self._current_cell = None
        if cell is None:
            self._ui.frame_runcell.hide()
            return

        runinfo = cell.runinfo()
        os_runinfo = runinfo.os_runinfo()
        self._ui.frame_runcell.show()

        self._ui.combobox_os_type.setCurrentIndex(-1)
        for idx, item in enumerate(self._os_runinfo_desc):
            if isinstance(os_runinfo, item['class']):
                item['widget'].set_runinfo(os_runinfo)
                self._ui.combobox_os_type.setCurrentIndex(idx)

        self._ui.label_cellname.setText(cell.name())
        self._current_cell = cell

    def _on_runinfo_value_changed(self):
        """
        处理运行信息值变化事件。
        
        当操作系统运行信息改变时，更新单元格的运行信息并调整界面高度。
        """
        if self._current_cell is None:
            return
        widget: OSRunInfoWidget = self._ui.stackedwidget_os_runinfo.currentWidget()
        self._current_cell.runinfo().set_os_runinfo(widget.runinfo())
        self._ui.stackedwidget_os_runinfo.setFixedHeight(self._ui.stackedwidget_os_runinfo.currentWidget().sizeHint().height())

    def _on_current_cell_changed(self, arg):
        """
        处理当前单元格改变事件。
        
        当用户在列表中选择不同的单元格时，更新显示的单元格信息。
        
        Args:
            arg: 当前行索引。
        """
        item = self._ui.listwidget_cells.currentItem()
        if item is None:
            self._update_current_cell(None)
            return
        name = item.data(QtCore.Qt.UserRole)
        guestcells: ResourceGuestCellList = self._resource.find(ResourceGuestCellList)
        cell = guestcells.find_cell(name)
        if cell is None:
            self._update_current_cell(None)
            return
        self._update_current_cell(cell)

    def _on_os_type_changed(self, index):
        """
        处理操作系统类型改变事件。
        
        当用户选择不同的操作系统类型时，切换显示相应的配置界面。
        
        Args:
            index: 下拉列表的索引。
        """
        display  = self._ui.combobox_os_type.currentText()
        if display is None or len(display)==0:
            return

        found_item = None
        for item in self._os_runinfo_desc:
            if item['display'] == display:
                found_item = item
                break

        widget = found_item['widget']
        self._ui.stackedwidget_os_runinfo.setCurrentWidget(widget)
        fixed_height = self._ui.stackedwidget_os_runinfo.currentWidget().sizeHint().height()
        if fixed_height < 0:
            fixed_height = 0
        self._ui.stackedwidget_os_runinfo.setFixedHeight(fixed_height)

        if self._current_cell is not None:
            widget.reset()
            runinfo = self._current_cell.runinfo()
            runinfo.set_os_runinfo(widget.runinfo())

    def _on_addr_edit_finished(self):
        """
        处理地址编辑完成事件。
        
        保存用户输入的服务器地址到配置。
        """
        self.profile_addr.set(self._ui.lineedit_addr.text().strip())

    def _on_state_changed(self, sender):
        """
        处理连接状态变化事件。
        
        当RPC客户端连接状态改变时，更新界面显示。
        
        Args:
            sender: 信号发送者。
        """
        if sender is not self._client:
            return

        is_connected = self._client.is_connected()
        if is_connected:
            self._ui.btn_connect.setText("断开")
            self._timer.start()
        else:
            self._ui.btn_connect.setText("连接")
            self._ui.listwidget_cells.clearSelection()
            self._timer.stop()
            self._root_cpuload.reset()

        self._ui.btn_connect.setChecked(is_connected)
        self._ui.btn_hyp_start.setEnabled(is_connected)
        self._ui.btn_hyp_stop.setEnabled(is_connected)
        self._ui.frame_runcell.setVisible(is_connected)

    def _on_connect(self):
        """
        处理连接按钮点击事件。
        
        连接到或断开与远程服务器的连接。
        """
        if not self._client.is_connected():
            if not self._client.connect(self._ui.lineedit_addr.text().strip(), timeout=10):
                self.logger.error("连接失败")
        else:
            self._client.close()
