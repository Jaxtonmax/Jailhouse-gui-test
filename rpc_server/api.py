from typing import Any
import abc
from unittest import result

class RPCApi(metaclass=abc.ABCMeta):
    class Result(object):
        def __init__(self, status: bool = False, msg: str = "", result: Any = None):
            super().__init__
            self.status = status
            self.message = msg
            self.result = result

        def to_dict(self):
            return {
                'status' : self.status,
                'message': self.message,
                'result' : self.result
            }

        @classmethod
        def from_dict(cls, value):
            result = cls()
            result.status  = value['status']
            result.message = value['message']
            result.result  = value['result']
            return result

        @classmethod
        def error(cls, msg):
            return cls(False, msg=msg)

        @classmethod
        def success(cls, result):
            return cls(True, result=result)

        def __bool__(self):
            return self.status

        def __repr__(self) -> str:
            return f"status: {self.status}, message: {self.message} result: {self.result}"

    def __init__(self):
        super().__init__()
        pass

    @abc.abstractmethod
    def hello(self, msg: str) -> dict:
        return None

    @abc.abstractmethod
    def pci_devices(self) -> dict:
        """ 获取PCI列表
        Returns:
        """
        return None

    @abc.abstractmethod
    def compile_cell(self, source: str) -> dict:
        """ 编译cell
        Args:
            source (str): 源代码文本内容
        Returns:
            bytes: 编译生成的二进制文件
        """
        return None

    @abc.abstractmethod
    def jailhouse_enable(self, rootcell: bytes) -> dict:
        """使能jailhouse
        """
        return None

    @abc.abstractmethod
    def jailhouse_disable(self) -> dict:
        """关闭jailhouse
        """
        return None

    @abc.abstractmethod
    def list_cell(self) -> dict:
        """获取cell列表
        """
        return None

    @abc.abstractmethod
    def create_cell(self, cell: bytes) -> dict:
        """ 创建cell
        Args:
            cell (bytes): cell二进制内容
        """
        return None

    @abc.abstractmethod
    def destroy_cell(self, name: str) -> dict:
        """ 创建cell
        """
        return None

    @abc.abstractmethod
    def load_cell(self, name: str, addr: int, data: bytes) -> dict:
        """ 加载cell
        Args:
            name (_type_): cell名称
            images (dict): [ { addr:<addr>, data:<data>} ... ]
        """
        return None

    @abc.abstractmethod
    def start_cell(self, name) -> dict:
        """ 启动cell
        Args:
            name (_type_): cell名称
        """
        return None

    @abc.abstractmethod
    def stop_cell(self, name) -> dict:
        """ 停止cell
        """
        return None

    @abc.abstractmethod
    def get_status(self) -> dict:
        """获取状态
        Returns:
            {
                timestamp: time.time()
                rootcell: {
                    meminfo = psutils.virtual_memory(),
                    cputimes = psutil.cpu_times(),
                    cpuload = psutil.cpu_percent(),
                    cpucount: <count>,
                }
                guestcells: {
                    'name': {'id', 'name', 'status'} ... ],
                }
            }
        """
        return None

    @abc.abstractmethod
    def get_guest_status(self, idx) -> dict:
        """
        {
            online   :  是否在线
            mem_total:  总内存 单位字节
            mem_used :  已使用内存 单位字节
            cpu_load :  CPU负载
        }
        """
        return None


    @abc.abstractmethod
    def run_linux(self, cell: bytes, kernel: bytes, dtb: bytes, ramdisk: bytes, bootargs: str) -> dict:
        return None

    @abc.abstractmethod
    def start_uart_server( self, config: str ) -> dict:
        """
        启动串口服务
        config: JHR配置文件
        """
        return None

    @abc.abstractmethod
    def stop_uart_server( self ) -> dict:
        """
        停止串口服务
        """
        return None

    @abc.abstractmethod
    def update_cpu_config(self, json_str: str) -> dict:
        """
        更新CPU配置（接收JSON字符串）
        Args:
            json_str: 包含CPU配置的JSON字符串（例如{"cpus": [0,1,2], "zone_id": 1}）
        Returns:
            处理结果（成功/失败信息）
        """
        return None