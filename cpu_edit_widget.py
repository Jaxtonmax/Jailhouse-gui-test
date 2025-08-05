"""
CPU核心选择编辑界面模块。

本模块提供了用于选择和编辑CPU核心分配的图形界面组件。主要功能包括：
- 显示可用的CPU核心列表
- 支持多选CPU核心
- 动态调整CPU核心数量
- 可编辑状态控制
- 自动生成CPU配置JSON并通过TCP发送

主要类:
- CPUEditWidget: CPU核心选择编辑界面组件
"""

import os
from json_config_updater import JSONConfigUpdater
from PySide2 import QtWidgets, QtCore
from typing import Set, List, Dict
import json
from forms.ui_cpu_edit_widget import Ui_CPUEditWidget
from flowlayout import FlowLayout
from common_widget import SelectButton, clean_layout
from rpc_server.rpc_client import RPCClient
import logging
logger = logging.getLogger("cpu_edit_widget")  # 定义 logger

class CPUEditWidget(QtWidgets.QWidget):
    """
    CPU核心选择编辑界面组件。
    
    提供图形化的CPU核心选择界面，使用流式布局展示CPU核心按钮。
    每个CPU核心都可以独立选择或取消选择，并自动同步配置到目标板。
    
    信号:
        cpus_changed: 当CPU核心选择发生变化时发出
    
    属性:
        _editable: 是否可编辑
        _items: CPU核心选择按钮列表
        _cpu_count: CPU核心总数
        _json_template: CPU配置JSON模板
    """
    
    cpus_changed = QtCore.Signal(set)

    def __init__(self, parent=None):
        """
        初始化CPU核心选择编辑界面。
        
        Args:
            parent: 父窗口部件，默认为None
        """
        super().__init__(parent)
        self.logger = logger  # 新增这一行，关联模块级别的logger
        self.logger.debug("CPUEditWidget 开始初始化")
        try:
            # 只初始化一次UI
            self._ui = Ui_CPUEditWidget()
            self._ui.setupUi(self)
            self._ui.frame_ops.hide()  # 隐藏操作框
            
            # 处理frame_cpus布局，避免重复创建
            frame_layout = self._ui.frame_cpus.layout()
            clean_layout(frame_layout)  # 清理现有布局中的控件
            
            # 复用现有布局或创建新布局（只执行一次）
            if self._ui.frame_cpus.layout() is None:
                self._layout = FlowLayout(self._ui.frame_cpus)
            else:
                self._layout = self._ui.frame_cpus.layout()
            
            # 初始化属性
            self._editable = True
            self._items: List[SelectButton] = []
            self._cpu_count = 0
            
            # 初始化JSON配置模板
            # 关键修改：加载完整的template.json作为模板
            # 请替换为你的template.json实际路径（建议使用项目相对路径）
            template_path = os.path.join(os.path.dirname(__file__), "/home/wzm/work/Jailhouse-gui/template.json")
            # self._json_template = JSONConfigUpdater.load_json_template(template_path)
            # # 验证模板是否加载成功（可选）
            # if not self._json_template:
            #     logger.error("未加载到完整模板，使用默认备份模板")
            #     # 若加载失败，可在这里放一份完整的备份模板（与template.json内容一致）
            #     self._json_template = {
            #         {
            #             "arch": "arm64",
            #             "name": "rtthread",
            #             "zone_id": 1,
            #             "cpus": [2,3],
            #             "memory_regions": [
            #                 {
            #                     "type": "ram",
            #                     "physical_start": "0x40008000",
            #                     "virtual_start":  "0x40008000",
            #                     "size": "0x10000000"
            #                 },
            #                 {
            #                     "type": "io",
            #                     "physical_start": "0xFD5F8000",
            #                     "virtual_start":  "0xFD5F8000",
            #                     "size": "0x1000"
            #                 },
            #                 {
            #                     "type": "io",
            #                     "physical_start": "0xfeb50000",
            #                     "virtual_start":  "0xfeb50000",
            #                     "size": "0x10000"
            #                 },
            #                 {
            #                     "type": "io",
            #                     "physical_start": "0xfeb60000",
            #                     "virtual_start":  "0xfeb60000",
            #                     "size": "0x10000"
            #                 },
            #                 {
            #                     "type": "io",
            #                     "physical_start": "0xfeba0000",
            #                     "virtual_start":  "0xfeba0000",
            #                     "size": "0x10000"
            #                 },
            #                 {
            #                     "type": "io",
            #                     "physical_start": "0xFD7C0000",
            #                     "virtual_start":  "0xFD7C0000",
            #                     "size": "0x10000"
            #                 },
            #                 {
            #                     "type": "io",
            #                     "physical_start": "0xfe660000",
            #                     "virtual_start":  "0xfe660000",
            #                     "size": "0x20000"
            #                 },
            #                 {
            #                     "type": "io",
            #                     "physical_start": "0xfeae0000",
            #                     "virtual_start":  "0xfeae0000",
            #                     "size": "0x1000"
            #                 },
            #                 {
            #                     "type": "io",
            #                     "physical_start": "0xfea70000",
            #                     "virtual_start":  "0xfea70000",
            #                     "size": "0x10000"
            #                 },
            #                 {
            #                     "type": "io",
            #                     "physical_start": "0xfd5fa000",
            #                     "virtual_start":  "0xfd5fa000",
            #                     "size": "0x4000"
            #                 },
            #                 {
            #                     "type": "virtio",
            #                     "physical_start": "0xff9e0000",
            #                     "virtual_start":  "0xff9e0000",
            #                     "size": "0x1000"
            #                 },
            #                 {
            #                     "type": "io",
            #                     "physical_start": "0xFD890000",
            #                     "virtual_start":  "0xFD890000",
            #                     "size": "0x10000"
            #                 }
            #             ],
            #             "interrupts": [366, 326, 80, 375, 363],
            #             "ivc_configs": [],
            #             "kernel_filepath": "./zone1rt/rtthread.bin",
            #             "dtb_filepath": "./zone1rt/zone1-linux.dtb",
            #             "kernel_load_paddr": "0x40008000",
            #             "dtb_load_paddr":   "0x40000000",
            #             "entry_point":      "0x40008000",
            #             "arch_config": {
            #                 "gic_version": "v3",
            #                 "gicd_base": "0xfe600000",
            #                 "gicd_size": "0x10000",
            #                 "gicr_base": "0xfe680000",
            #                 "gicr_size": "0x10000"
            #             }
            #         }



            #     }
            
            logger.debug("CPUEditWidget 初始化成功")
        except Exception as e:
            logger.error(f"CPUEditWidget 初始化失败: {str(e)}")
            raise

    def set_config(self, config_data: dict):
        """
        从外部接收完整的配置字典，并更新CPU显示。
        """
        if not config_data or 'cpus' not in config_data:
            self.logger.warning("传入的配置无效或缺少'cpus'字段")
            return
        
        # 从配置中获取cpus并更新UI
        cpus_to_set = set(config_data.get('cpus', []))
        self.set_cpus(cpus_to_set)

    # set_cpu_count, set_editable, get_cpus, set_cpus 方法保持不变

    def set_cpu_count(self, count):
        """
        设置CPU核心数量。
        
        根据指定的数量创建对应数量的选择按钮。
        
        Args:
            count: CPU核心数量
        """
        self._cpu_count = count
        clean_layout(self._layout)  # 清理现有按钮
        self._items.clear()

        for i in range(count):
            item = SelectButton(str(i), self._ui.frame_cpus)
            self._layout.addWidget(item)
            item.clicked.connect(self._on_item_changed)
            self._items.append(item)

    def set_editable(self, editable: bool):
        """
        设置是否可编辑。
        
        控制所有CPU核心选择按钮的可用状态。
        
        Args:
            editable: 是否允许编辑
        """
        self._editable = editable
        for item in self._items:
            item.setEnabled(editable)

    def set_cpus(self, cpus: Set[int]):
        """
        设置选中的CPU核心。
        
        根据提供的CPU核心集合更新选择状态。
        
        Args:
            cpus: 要选中的CPU核心索引集合
        """
        for idx, item in enumerate(self._items):
            item.setChecked(idx in cpus)

    def get_cpus(self) -> Set[int]:
        """
        获取当前选中的CPU核心。
        
        Returns:
            Set[int]: 当前选中的CPU核心索引集合
        """
        cpus = set()
        for idx, item in enumerate(self._items):
            if item.isChecked():
                cpus.add(idx)
        return cpus

    def _get_tcp_communicator(self):
        """从父组件获取TCP通信实例并验证连接"""
        try:
            # 从父组件（GuestCellWidget）获取通信实例
            parent = self.parent()
            while parent:
                if hasattr(parent, '_tcp_communicator'):
                    tcp_comm = parent._tcp_communicator
                    # 检查实例是否有效且已连接
                    if tcp_comm and tcp_comm.is_connected():
                        return tcp_comm
                    else:
                        self.logger.error("父组件的TCP通信实例未连接")
                        return None
                parent = parent.parent()
            
            # 如果未找到父组件的通信实例，尝试直接获取RPCClient单例（降级方案）
            from rpc_server.rpc_client import RPCClient  # 局部导入避免循环依赖
            tcp_comm = RPCClient.get_instance()
            if tcp_comm.is_connected():
                return tcp_comm
            else:
                self.logger.error("RPCClient单例未连接")
                return None
        except Exception as e:
            self.logger.error(f"获取TCP通信实例失败: {str(e)}")
            return None

    def _generate_cpu_config(self) -> str:
        """生成CPU配置JSON字符串"""
        selected_cpus = sorted(self.get_cpus())
        self._json_template["cpus"] = selected_cpus
        return json.dumps(self._json_template, indent=4, ensure_ascii=False)

    def _on_item_changed(self):
        """处理CPU核心选择变化事件"""
        selected_cpus = self.get_cpus()  # 获取当前选中的CPU核心集合
        self.cpus_changed.emit(selected_cpus)  # 传递参数，与信号定义匹配
        
        tcp_comm = self._get_tcp_communicator()
        if not tcp_comm:
            logger.error("未获取到TCP通信实例")
            return
        
        # 确认连接状态
        if not tcp_comm.is_connected():
            logger.error("TCP通信实例未连接到服务器")
            return
        
        try:
            config_json = self._generate_cpu_config()
            if hasattr(tcp_comm, 'update_cpu_config'):
                result = tcp_comm.update_cpu_config(config_json)
                if result and result.status:
                    logger.debug(f"CPU配置发送成功: {config_json}")
                else:
                    logger.error(f"CPU配置发送失败: {result.message if result else '未知错误'}")
            else:
                logger.error("TCP通信器不支持update_cpu_config方法")
        except Exception as e:
            logger.error(f"发送CPU配置时出错: {str(e)}")


if __name__ == '__main__':
    """主程序入口，用于测试CPU核心选择编辑界面。"""
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = CPUEditWidget()
    w.set_cpu_count(4)
    w.show()
    app.exec_()
