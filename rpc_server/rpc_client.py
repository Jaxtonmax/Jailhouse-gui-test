import logging
import threading
import traceback
from typing import Optional
import zerorpc
if __name__ == '__main__':
    from api import RPCApi
else:
    from .api import RPCApi
import click
import blinker


def rpc_call(func):
    def run(*args):
        client = args[0]
        if client._client is None:
            return RPCApi.Result(False, msg="unconnected")

        with client._lock:
            try:
                if len(args) == 1:
                    result = client._client.__call__( func.__name__)
                else:
                    result = client._client.__call__( func.__name__, *args[1:])

                if not isinstance(result, dict):
                    print(f"rpc server return type error: {type(result)} {result}")
                    return RPCApi.Result(False, msg='rpc server return type error')
                return RPCApi.Result.from_dict(result)
            except Exception as e:
                traceback.print_exc()
                print(f"call rpc except {e}")
                client.close()
                return RPCApi.Result(False, msg=f'call rpc except {e}')
    return run


class RPCClient(RPCApi):
    logger = logging.getLogger("RPCClient")
    state_changed = blinker.Signal()

    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = RPCClient()
        return cls._instance

    def __init__(self):
        super().__init__()
        self._client: Optional[zerorpc.Client] = None
        self._semaphore = threading.Semaphore(0)
        self._heartbeat = None
        self._lock = threading.Lock()

    def connect(self, addr: str, timeout=3):
        if self._client is not None:
            return False

        c = zerorpc.Client(timeout=timeout)
        c.connect(addr)
        try:
            c.hello("hello")
        except:
            self.logger.error("call hello failed.")
            return False
        self._client = c

        # 在线程中执行会出问题
        # self._heartbeat = threading.Thread(target=self._heartbeat_threadfun)
        # self._heartbeat.start()
        self.state_changed.send(self)
        return True

    def is_connected(self) -> bool:
        return self._client is not None

    def close(self):
        if self._client is not None:
            self._client.close()
            self._client = None
            try:
                self._semaphore.release()
            except TypeError:
                self._semaphore.release(1)

            self.state_changed.send(self)

    def _heartbeat_threadfun(self):
        while self._client:
            if self._semaphore.acquire(timeout=2):
                continue
            try:
                self.hello("hello")
            except:
                print("==============")
                traceback.print_exc()
                print("==============")
                break

        if self._client:
            self._client.close()
            self._client = None
        self._heartbeat = None
        self.logger.error("rpc heartbeat thread exit.")
        self.state_changed.send(self)

    @rpc_call
    def hello(self, msg: str) -> Optional[RPCApi.Result]:
        return None

    @rpc_call
    def compile_cell(self, source: str) -> Optional[RPCApi.Result]:
        return None

    @rpc_call
    def jailhouse_enable(self, rootcell) -> Optional[RPCApi.Result]:
        return None

    @rpc_call
    def jailhouse_disable(self) -> dict:
        return None

    @rpc_call
    def pci_devices(self) -> Optional[RPCApi.Result]:
        return None

    @rpc_call
    def list_cell(self) -> Optional[RPCApi.Result]:
        return None

    @rpc_call
    def create_cell(self, cell: bytes) -> Optional[RPCApi.Result]:
        return None

    @rpc_call
    def destroy_cell(self, name: str) -> Optional[RPCApi.Result]:
        return None

    @rpc_call
    def load_cell(self, name, addr: int, data: bytes) -> Optional[RPCApi.Result]:
        return None

    @rpc_call
    def start_cell(self, name) -> Optional[RPCApi.Result]:
        return None

    @rpc_call
    def stop_cell(self, name) -> Optional[RPCApi.Result]:
        return None

    @rpc_call
    def get_status(self) -> Optional[RPCApi.Result]:
        return None

    @rpc_call
    def run_linux(self, cell: bytes, kernel: bytes, dtb: bytes, ramdisk: bytes, bootargs: str) -> Optional[RPCApi.Result]:
        return None

    @rpc_call
    def get_guest_status(self, idx: int) -> Optional[RPCApi.Result]:
        return None

    @rpc_call
    def start_uart_server(self, config: str) -> Optional[RPCApi.Result]:
        return None

    @rpc_call
    def stop_uart_server(self) -> Optional[RPCApi.Result]:
        return None

    @rpc_call
    def update_cpu_config(self, json_str: str) -> Optional[RPCApi.Result]:
        """发送CPU配置JSON到服务端"""
        return None


@click.group()
@click.option("--addr", type=str, default='')
@click.pass_context
def cli(ctx, addr):
    ctx.ensure_object(dict)
    ctx.obj['addr'] = addr
    ctx.obj['client'] = None

    if len(addr) > 0:
        client = RPCClient()
        if not client.connect(addr):
            print("connect failed")
            clinet = None
        ctx.obj['client'] = client

@cli.command("hello")
@click.pass_context
def cmd_hello(ctx):
    client = ctx.obj['client']
    if client is None:
        print("not connect.")
        return False

    result = client.hello("hello")
    if result is None or not result.status:
        print("failed.", result)
        return False
    print("Reply:", result.result)
    return True

@cli.command("compile-cell")
@click.argument("input")
@click.argument("output")
@click.pass_context
def cmd_compile_cell(ctx, input, output):
    client = ctx.obj['client']
    source = None
    if client is None:
        print("not connect.")
        return False

    try:
        with open(input, 'rt') as f:
            source = f.read()
    except:
        print("read input file failed")
        return False

    result = client.compile_cell(source)
    if not result.status:
        print("compile failed")
        print(result.message)
        return False

    try:
        with open(output, "wb") as f:
            f.write(result.result)
    except:
        print("save output failed.")

    return True

@cli.command("pci-devices")
@click.pass_context
def cmd_pci_devices(ctx):
    client = ctx.obj['client']
    if client is None:
        print("not connect.")
        return False

    result = client.pci_devices()
    if not result.status:
        print("get pci device failed.")
        print(result.message)
        return False

    print(result.result)
    return True

@cli.command("enable")
@click.argument("rootcell")
@click.pass_context
def enable(ctx, rootcell):
    client: RPCClient = ctx.obj['client']
    if client is None:
        print("not connect.")
        return False

    try:
        cell_bin = open(rootcell, 'rb').read()
    except:
        print("read cell failed.")
        return False

    result = client.jailhouse_enable(cell_bin)
    print(result)
    return True

@cli.command("disable")
@click.pass_context
def disable(ctx):
    client: RPCClient = ctx.obj['client']
    if client is None:
        print("not connect.")
        return False

    result = client.jailhouse_disable()
    print(result)
    return True


@cli.command("list-cell")
@click.pass_context
def cmd_list_cell(ctx):
    client: RPCClient = ctx.obj['client']
    if client is None:
        print("not connect.")
        return False

    result = client.list_cell()
    if not result.status:
        print(result.message)
        return False

    for status in result.result:
        print(status)
    return True

@cli.command("create-cell")
@click.argument("cell")
@click.pass_context
def cmd_create_cell(ctx, cell):
    client: RPCClient = ctx.obj['client']
    if client is None:
        print("not connect.")
        return False

    try:
        cell_bin = open(cell, 'rb').read()
    except:
        print("read cell failed.")
        return False

    result = client.create_cell(cell_bin)
    if not result.status:
        print(result.message)
        return False
    print(result)
    return True

@cli.command("destroy-cell")
@click.argument("name")
@click.pass_context
def cmd_destroy_cell(ctx, name):
    client: RPCClient = ctx.obj['client']
    if client is None:
        print("not connect.")
        return False

    result = client.destroy_cell(name)
    if not result.status:
        print(result.message)
        return False
    print(result)
    return True

def hexint(s):
    return int(s,0)

@cli.command("load-cell")
@click.argument("name", type=str)
@click.argument("addr", type=hexint)
@click.argument('file', type=str)
@click.pass_context
def cmd_load_cell(ctx, name, addr, file):
    client: RPCClient = ctx.obj['client']
    if client is None:
        print("not connect.")
        return False

    try:
        data = open(file, 'rb').read()
    except:
        print("open file failed.")
        return False

    result = client.load_cell(name, addr, data)
    if not result.status:
        print(result.message)
        return False
    print(result)
    return True

@cli.command("start-cell")
@click.argument("name", type=str)
@click.pass_context
def cmd_start_cell(ctx, name):
    client: RPCClient = ctx.obj['client']
    if client is None:
        print("not connect.")
        return False

    result = client.start_cell(name)
    if not result.status:
        print(result.message)
        return False
    print(result)
    return True

@cli.command("stop-cell")
@click.argument("name", type=str)
@click.pass_context
def cmd_stop_cell(ctx, name):
    client: RPCClient = ctx.obj['client']
    if client is None:
        print("not connect.")
        return False

    result = client.stop_cell(name)
    if not result.status:
        print(result.message)
        return False
    print(result)
    return True

@cli.command("status")
@click.pass_context
def get_status(ctx):
    client: RPCClient = ctx.obj['client']
    if client is None:
        print("not connect.")
        return False

    result = client.get_status()
    if not result.status:
        print(result.message)
        return False
    print(result.result)
    return True

@cli.command("guest-status")
@click.pass_context
@click.argument("index", type=int)
def get_status(ctx, index):
    client: RPCClient = ctx.obj['client']
    if client is None:
        print("not connect.")
        return False

    result = client.get_guest_status(index)
    if not result.status:
        print(result.message)
        return False
    print(result.result)
    return True

@cli.command("start-uart")
@click.pass_context
@click.argument("jhr", type=str)
def start_uart(ctx, jhr):
    client: RPCClient = ctx.obj['client']
    if client is None:
        print("not connect.")
        return False
    config = None
    try:
        with open(jhr, "rt") as f:
            config = f.read()
    except:
        print(f"open {jhr} failed.")
        return False

    result = client.start_uart_server(config)
    if not result:
        print("start uart server failed.")
        print(result.message)

@cli.command("stop-uart")
@click.pass_context
def stop_uart(ctx):
    client: RPCClient = ctx.obj['client']
    if client is None:
        print("not connect.")
        return False
    result = client.stop_uart_server()
    if not result:
        print("stop uart server failed.")
        print(result.message)


if __name__ == "__main__":
    cli()
