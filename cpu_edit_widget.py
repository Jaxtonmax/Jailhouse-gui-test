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


from PySide2 import QtWidgets, QtCore
from typing import Set, List, Dict
import json
from forms.ui_cpu_edit_widget import Ui_CPUEditWidget
from flowlayout import FlowLayout
from common_widget import SelectButton, clean_layout

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
    
    cpus_changed = QtCore.Signal()

    def __init__(self, parent=None):
        """
        初始化CPU核心选择编辑界面。
        
        Args:
            parent: 父窗口部件，默认为None
        """
        super().__init__(parent)
        logger.debug("CPUEditWidget 开始初始化")
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
            self._json_template: Dict = {
                "arch": "arm64",
                "name": "linux2",
                "zone_id": 1,
                "cpus": [],  # 动态更新的CPU核心列表
                "memory_regions": [
                    {"type": "ram", "physical_start": "0x50000000", "virtual_start": "0x50000000", "size": "0x15000000"},
                    {"type": "ram", "physical_start": "0x0", "virtual_start": "0x0", "size": "0x200000"},
                    {"type": "virtio", "physical_start": "0xff9d0000", "virtual_start": "0xff9d0000", "size": "0x1000"},
                    {"type": "virtio", "physical_start": "0xff9e0000", "virtual_start": "0xff9e0000", "size": "0x1000"}
                ]
            }
            
            logger.debug("CPUEditWidget 初始化成功")
        except Exception as e:
            logger.error(f"CPUEditWidget 初始化失败: {str(e)}")
            raise  # 抛出异常供上层捕获

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
        """
        从父组件获取TCP通信实例
        
        从BoardWidget中获取TCP通信器，符合项目现有架构
        """
        parent = self.parent()
        while parent:
            if hasattr(parent, '_tcp_communicator'):
                return parent._tcp_communicator
            parent = parent.parent()
        return None

    def _generate_cpu_config(self) -> str:
        """生成CPU配置JSON字符串"""
        selected_cpus = sorted(self.get_cpus())
        self._json_template["cpus"] = selected_cpus
        return json.dumps(self._json_template, indent=4, ensure_ascii=False)

    def _on_item_changed(self):
        """处理CPU核心选择变化事件"""
        self.cpus_changed.emit()  # 发出信号
        
        tcp_comm = self._get_tcp_communicator()
        if not tcp_comm:
            return
        
        try:
            config_json = self._generate_cpu_config()
            # 发送配置（确保tcp_comm有update_cpu_config方法）
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
