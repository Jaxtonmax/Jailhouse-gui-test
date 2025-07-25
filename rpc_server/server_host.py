#! /usr/bin/env python3

from typing import Optional, Union
from server import RPCServer
from api import RPCApi
import os
import logging
from pci_device import PCIDevice
import psutil
import time
from jailhouse import Jailhouse, TempFile
import subprocess
# 获取当前脚本所在目录的绝对路径
mypath = os.path.split(os.path.realpath(__file__))[0]

# 定义编译工具路径和 Jailhouse 相关目录
cc      = 'gcc'
objcopy = 'objcopy'
jailhouse_src = os.path.join(mypath, "jailhouse")
jailhouse_bin = os.path.join(mypath, "jailhouse_bin")

inc_dirs = [
    os.path.join(jailhouse_src, "hypervisor/arch/arm64/include"),
    os.path.join(jailhouse_src, "hypervisor/include"),
    os.path.join(jailhouse_src, "include")
]

cflags = "-Werror -Wall -Wextra -D__LINUX_COMPILER_TYPES_H"


class HostApi(RPCApi):
    def __init__(self):
        super().__init__()
        self._uart_server: Optional[subprocess.Popen] = None

    def hello(self, msg: str):
        # 接收客户端消息并返回成功结果（包含原消息），用于测试通信连通性
        return RPCApi.Result(True, result=msg).to_dict()

    def compile_cell(self, src_txt: str) -> dict:
        # 保存到临时目录
        tf = TempFile()

        # 校验输入是否为字符串类型
        if not isinstance(src_txt, str):
            return RPCApi.Result.error("source type error").to_dict()

        # 创建临时文件路径（.c 源码、.o 目标文件、.cell 二进制输出）
        src = tf.save("compile", ".c")# 临时 C 源码文件
        obj = tf.save("compile", ".o") # 临时目标文件
        cell = tf.save("compile", ".cell")# 最终 cell 二进制文件

        # 将输入的源码文本写入临时 C 文件
        logging.info(f"save source to {src}")
        with open(src, "wt", encoding='utf8') as f:
            f.write(src_txt)

        # 构建编译命令（包含头文件目录和编译选项）
        logging.info("compile")
        cflags_list = [
            cflags,
            ' '.join(map(lambda x: f"-I{x}", inc_dirs))# 拼接头文件目录参数
        ]
        cmd = f"{cc} -c {' '.join(cflags_list)} {src} -o {obj}"
        print(cmd)
        result = Jailhouse.run_command(cmd)
        if not result:
            return result.to_dict()

        logging.info("objcopy")
        cmd = f"{objcopy} -O binary --remove-section=.note.gnu.property {obj} {cell}"
        result = Jailhouse.run_command(cmd)
        if not result:
            return result.to_dict()

        cell_data = None
        with open(cell, "rb") as f:
            cell_data = f.read()

        return RPCApi.Result(True, result=cell_data).to_dict()

    def pci_devices(self) -> dict:
        devices = list()
        pcis = PCIDevice.all_from_sysfs()
        for pci in pcis:
            devices.append(pci.to_dict())
        return RPCApi.Result(True, result=devices).to_dict()

    def jailhouse_enable(self, rootcell: bytes) -> dict:
        logging.info(f"jailhouse enable")
        return Jailhouse.enable(rootcell).to_dict()

    def jailhouse_disable(self) -> dict:
        logging.info(f"jailhouse disable")
        return Jailhouse.disable().to_dict()

    def list_cell(self) -> dict:
        logging.info(f"list cell")
        return Jailhouse.list_cell().to_dict()

    def create_cell(self, cell: bytes) -> dict:
        logging.info(f"create cell")
        return Jailhouse.create_cell(cell).to_dict()

    def destroy_cell(self, name: str) -> dict:
        logging.info(f"destroy cell {name}")
        return Jailhouse.destroy_cell(name).to_dict()

    def load_cell(self, name, addr, data) -> dict:
        logging.info(f"load cell {name} {hex(addr)}")
        return Jailhouse.load_cell(name, addr, data).to_dict()

    def start_cell(self, name) -> dict:
        logging.info(f"start cell {name}")
        return Jailhouse.start_cell(name).to_dict()

    def stop_cell(self, name) -> dict:
        logging.info(f"stop cell {name}")
        return Jailhouse.stop_cell(name).to_dict()

    def get_status(self) -> dict:
        status = dict()
        rootcell = dict()
        guestcells = dict()
        rootcell['meminfo'] = psutil.virtual_memory()._asdict()
        rootcell['cputimes'] = psutil.cpu_times()._asdict()
        rootcell['cpuload'] = psutil.cpu_percent()
        rootcell['cpucount'] = psutil.cpu_count()

        for cell in Jailhouse.list_cell().result:
            guestcells[cell['name']] = cell

        status['timestamp'] = time.time()
        status['rootcell'] = rootcell
        status['guestcells'] = guestcells
        return RPCApi.Result(True, result=status).to_dict()

    def run_linux(self, cell: bytes, kernel: bytes, dtb: bytes, ramdisk: bytes, bootargs: str) -> dict():
        tf = TempFile()

        if not isinstance(cell, bytes):
            return RPCApi.Result.error("cell type error").to_dict()
        if not isinstance(kernel, bytes):
            return RPCApi.Result.error("kernel type error").to_dict()
        if not isinstance(dtb, bytes):
            return RPCApi.Result.error("dtb type error").to_dict()
        if not isinstance(bootargs, str):
            return RPCApi.Result.error("bootargs type error").to_dict()

        cell_fn    = None
        kernel_fn  = None
        dtb_fn     = None
        ramdisk_fn = None

        logging.info(f"save cell {len(cell)} bytes.")
        cell_fn = tf.save("runlinux", ".cell", cell)
        if cell_fn is None:
            logging.error("save cell failed.")
            return RPCApi.Result.error("save cell failed.").to_dict()

        logging.info(f"save kernel {len(kernel)} bytes.")
        kernel_fn = tf.save("runlinux", ".kernel", kernel)
        if kernel_fn is None:
            logging.error("save kernel failed.")
            return RPCApi.Result.error("save kernel failed.").to_dict()

        logging.info(f"save devicetree {len(dtb)} bytes")
        dtb_fn = tf.save("runlinux", ".dtb", dtb)
        if dtb_fn is None:
            logging.error("save dtb failed.")
            return RPCApi.Result.error("save dtb failed.").to_dict()

        if ramdisk:
            ramdisk_fn = tf.save("runlinux", ".ramdisk", ramdisk)
            if ramdisk_fn is None:
                logging.error("save ramdisk failed.")
                return RPCApi.Result.error("save ramdisk failed.").to_dict()

        result = Jailhouse.run_linux(cell_fn, kernel_fn, dtb_fn, ramdisk_fn, bootargs)
        if not result:
            logging.error(f"run linux failed: {result.message}.")
        return result.to_dict()

    def get_guest_status(self, idx) -> dict:
        status = {
            "online": true,
            "mem_total": 50,
            "mem_used": 50,
            "cpu_load": 50 
        }
        return RPCApi.Result.success(status).to_dict()

    def start_uart_server(self, config: str) -> dict:
        if self._uart_server is not None:
            self._uart_server.terminate()
            try:
                self._uart_server.wait(1)
            except:
                pass
            self._uart_server = None

        uart_tool = f'{mypath}/ivsm-p2p-tool'
        if not os.path.isfile(uart_tool):
            print("{uart_tool} not exist.")
            return RPCApi.Result.error("{uart_tool} not exist.").to_dict()

        jhr_path = '/tmp/uart_server_config.jhr'
        try:
            with open(jhr_path, "wt") as f:
                f.write(config)
        except:
            msg = f"open config failed."
            print(msg)
            return RPCApi.Result.error(msg).to_dict()

        self._uart_server = subprocess.Popen((uart_tool, 'uart-server', '--jhr', jhr_path))
        # 睡眠一小段时间，检查命令是否异常退出
        time.sleep(0.1)
        if self._uart_server.poll() is not None:
            msg = f'run uart-server failed.'
            print(msg)
            self._uart_server = None
            return RPCApi.Result.error(msg).to_dict()

        return RPCApi.Result.success("success").to_dict()

    def stop_uart_server(self) -> dict:
        if self._uart_server:
            self._uart_server.terminate()
            self._uart_server = None
        return RPCApi.Result.success("success").to_dict()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    addr = "tcp://0.0.0.0:4240"
    s = RPCServer(addr, HostApi())
    logging.info(f"server running {addr}.")
    s.run()
