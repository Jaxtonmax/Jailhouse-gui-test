import zerorpc
from typing import Optional
from api import RPCApi
import psutil


class RPCServer(object):
    def __init__(self, addr: str, api: RPCApi):
        self._addr = addr # 服务器绑定的网络地址（如 "tcp://0.0.0.0:4240"）
        self._api = api# 实现了RPCApi接口的实例，用于处理具体请求
        self._server: Optional[zerorpc.Server] = None# 内部维护的zerorpc服务器实例，初始为None

    def run(self) -> bool:
        if self._server is not None:# 若服务器已启动，则直接返回False（启动失败）
            return False
        self._server = zerorpc.Server(self._api)# 创建zerorpc服务器，关联API实现
        self._server.bind(self._addr)# 绑定到指定网络地址
        self._server.run()# 启动服务器，进入监听循环（阻塞当前线程）
        return True

    def stop(self):
        if self._server is None: # 若服务器未启动，则直接返回
            return
        self._server.stop()  # 停止zerorpc服务器
        self._server = None  # 清空服务器实例


class TestAPI(RPCApi):
    def hello(self, msg: str):
        # 接收客户端消息，返回成功结果（包含原消息）
        return RPCApi.Result(True, result
        
        # 以下方法均返回失败状态和 "unimplement" 消息，仅作为占位符：
    def compile_cell(self, src_txt: str) -> dict:
        return RPCApi.Result(False, msg="unimplement").to_dict()

    def pci_devices(self) -> dict:
        return RPCApi.Result(False, msg="unimplement").to_dict()

    def jailhouse_enable(self, rootcell: bytes) -> dict:
        return RPCApi.Result(False, msg="unimplement").to_dict()

    def jailhouse_disable(self) -> dict:
        return RPCApi.Result(False, msg="unimplement").to_dict()

    def list_cell(self) -> dict:
        return RPCApi.Result(False, msg="unimplement").to_dict()

    def create_cell(self, cell: bytes) -> dict:
        return RPCApi.Result(False, msg="unimplement").to_dict()

    def destroy_cell(self, name: str) -> dict:
        return RPCApi.Result(False, msg="unimplement").to_dict()

    def load_cell(self, name, addr, data) -> dict:
        return RPCApi.Result(False, msg="unimplement").to_dict()

    def start_cell(self, name) -> dict:
        return RPCApi.Result(False, msg="unimplement").to_dict()

    def stop_cell(self, name) -> dict:
        return RPCApi.Result(False, msg="unimplement").to_dict()

    def get_status(self) -> dict:
        status = dict()  # 存储整体状态的字典
        rootcell = dict() # 存储root cell状态的字典

        # 通过psutil获取系统内存信息（转换为字典）
        rootcell['meminfo'] = psutil.virtual_memory()._asdict()
        # 获取CPU时间信息（转换为字典）
        rootcell['cputimes'] = psutil.cpu_times()._asdict()
        # 获取CPU负载百分比
        rootcell['cpuload'] = psutil.cpu_percent()

         # 将root cell状态存入整体状态
        status['rootcell'] = rootcell
        # 返回成功结果，包含状态数据
        return RPCApi.Result(True, result=status).to_dict()


if __name__ == "__main__":
    s = RPCServer("tcp://0.0.0.0:4240", TestAPI())
    s.run()
