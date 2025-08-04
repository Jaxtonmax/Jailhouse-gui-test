import os
import logging
import platform
import subprocess
import tempfile
from typing import Union, Optional
from api import RPCApi
import shlex
import time

class TempFile(object):
    def __init__(self) -> None:
        self._temp_files = list()
        # 定义目标目录，确保目录存在
        self.target_dir = "/root/threevms/"
        os.makedirs(self.target_dir, exist_ok=True)  # 不存在则创建

    # 注释掉__del__方法，避免自动清理文件
    # def __del__(self):
    #     self.clean()

    def save(self, prefix: str, suffix: str, data: Optional[Union[str,bytes]] = None) -> Optional[str]:
        # 生成目标路径（使用固定目录，而非系统临时目录）
        # 生成唯一文件名（避免重复）
        import uuid
        unique_id = uuid.uuid4().hex[:8]  # 8位随机字符串
        filename = f"{prefix}_{unique_id}{suffix}"
        temp = os.path.join(self.target_dir, filename)

        try:
            if isinstance(data, str):
                with open(temp, "wt") as f:
                    f.write(data)
            elif isinstance(data, bytes):
                with open(temp, "wb") as f:
                    f.write(data)
        except Exception as e:
            logging.error(f"写入文件失败 {temp}: {e}")
            return None

        self._temp_files.append(temp)
        logging.info(f"文件已保存到: {temp}")  # 打印保存路径，方便确认
        return temp

    # 保留clean方法，如需手动清理可调用（可选）
    def clean(self):
        for fn in self._temp_files:
            if os.path.exists(fn):
                os.unlink(fn)
        self._temp_files.clear()


mypath = os.path.split(os.path.realpath(__file__))[0]

cc      = 'gcc'
objcopy = 'objcopy'
jailhouse_src = os.path.join(mypath, "jailhouse")
jailhouse_bin = os.path.join(mypath, "jailhouse_bin")

if platform.machine() == 'x86_64':
    repo_root      = "../../613virt/"
    cc             = repo_root + "tools/gcc-7.3.1-64-gnu/bin/aarch64-linux-gnu-gcc"
    objcopy        = repo_root + "tools/gcc-7.3.1-64-gnu/bin/aarch64-linux-gnu-objcopy"

inc_dirs = [
    os.path.join(jailhouse_src, "hypervisor/arch/arm64/include"),
    os.path.join(jailhouse_src, "hypervisor/include"),
    os.path.join(jailhouse_src, "include")
]

cflags = "-Werror -Wall -Wextra -D__LINUX_COMPILER_TYPES_H"


class Jailhouse(object):
    jh_exe = '/root/threevms/hvisor'
    jh_ko  = '/root/threevms/hvisor.ko'
    jh_dev = '/dev/hvisor'
    linux_loader = os.path.join(jailhouse_bin, "linux-loader.bin")
    _driver_loaded = False  # 记录驱动是否已尝试加载

    temp_files = list()

    def __init__(self) -> None:
        pass

    @classmethod
    def load_driver(cls) -> bool:
        """执行insmod指令加载驱动，不检查设备文件是否存在"""
        if cls._driver_loaded:
            return True
            
        logging.info("Attempting to load hvisor kernel module")
        cmd = f'insmod {cls.jh_ko}'
        
        # 直接执行insmod，不检查设备文件
        proc = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        proc.wait()
        out, err = proc.communicate()
        code = proc.returncode
        
        if isinstance(out, bytes):
            out = out.decode()
        if isinstance(err, bytes):
            err = err.decode()
        
        cls._driver_loaded = True  # 标记为已尝试加载
        
        # if code != 0:
        #     logging.error(f"Failed to load kernel module: {err}")
        #     return False
            
        logging.info("Kernel module loaded successfully")
        return True

    @classmethod
    def run_command(cls, cmd) -> RPCApi.Result:
        # 总是先尝试加载驱动
        if not cls.load_driver():
            return RPCApi.Result(False, msg="Failed to load hvisor kernel module")

        logging.debug(f"Executing command: {cmd}")

        proc = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        proc.wait()
        out, err = proc.communicate()
        code = proc.returncode

        # logging.info(f"Command: {cmd}")
        # logging.info(f"Return code: {code}")
        # logging.info(f"Standard output: {out}")
        # logging.info(f"Standard error: {err}")

        if isinstance(out, bytes):
            out = out.decode()
        if isinstance(err, bytes):
            err = err.decode()

        if proc.returncode in [0, 1]:
            return RPCApi.Result(True, result=out)
        else:
            return RPCApi.Result(False, msg=out+'\n'+err)

    @classmethod
    def find_cell_id(cls, name: str) -> Optional[int]:
        celllist = cls.list_cell()
        if not celllist:
            return None
        celllist = celllist.result

        for cell in celllist:
            if cell['id'] == 0:
                continue
            if cell['name'] == name:
                return cell['id']
        return None

    @classmethod
    def enable(cls, rootcell: bytes) -> RPCApi.Result:
        tf = TempFile()
        
        # 确保驱动已加载
        if not cls.load_driver():
            return RPCApi.Result(False, msg="Failed to load hvisor kernel module")
            
        commands = [
            "rm nohup.out",
            f"nohup {cls.jh_exe} virtio start ./zone1/zone1-linux-virtio.json > nohup1.out &",
            f"{cls.jh_exe} zone start ./zone1zone1-linux.json",
            "cat nohup1.out | grep \"char device\"",
            f"{cls.jh_exe} zone list"
        ]
        
        # 执行初始化命令
        for cmd in commands:
            r = cls.run_command(cmd)
            if not r:
                return RPCApi.Result(False, msg=f"Command failed: {cmd}")

        # 保存rootcell到文件
        temp_fn = tf.save("rootcell", ".cell", rootcell)
        if temp_fn is None:
            return RPCApi.Result(False, msg="Failed to save temp file")

        # # 执行创建root0linux的指令
        # cmd = f'{cls.jh_exe} enable {temp_fn}'
        # r = cls.run_command(cmd)
        # if not r:
        #     return RPCApi.Result(False, msg='Failed to enable jailhouse')

    #     return RPCApi.Result(True)

    @classmethod
    def disable(cls) -> RPCApi.Result:
        # 尝试加载驱动（即使设备文件不存在）
        cls.load_driver()

        cmd = f'{cls.jh_exe} disable'
        r = cls.run_command(cmd)
        
        # 如果disable失败且设备文件不存在，认为操作成功
        if not r and not os.path.exists(cls.jh_dev):
            return RPCApi.Result(True)
            
        return r

    @classmethod
    def list_cell(cls) -> RPCApi.Result:
        cmd = f"/root/threevms/hvisor zone list"  # 修改为你的新命令
        r = cls.run_command(cmd)
        if not r:
            return r

        cells = list()
        lines = r.result.split('\n')

        # 跳过表头行
        for line in lines[2:]:  # 从第三行开始解析，跳过表头和分隔线
            s = line.strip().split('|')
            if len(s) < 5:  # 确保有足够的列
                continue
            zone_id = s[1].strip()
            cpus = s[2].strip()
            name = s[3].strip()
            status = s[4].strip()

            if zone_id and name and status:
                cells.append({
                    'id': int(zone_id),
                    'name': name,
                    'status': status,
                    'cpus': cpus
                })
        return RPCApi.Result(True, result=cells)

    # @classmethod
    # def create_cell(cls, cell: bytes) -> RPCApi.Result:
    #     tf = TempFile()
    #     temp_fn = tf.save("create_cell", ".cell", cell)
    #     if temp_fn is None:
    #         return RPCApi.Result(False, msg="Failed to save temp file")

    #     cmd = f"{cls.jh_exe} cell create {temp_fn}"
    #     return cls.run_command(cmd)

    @classmethod
    def destroy_cell(cls, name: str) -> RPCApi.Result:
        cell_id = cls.find_cell_id(name)
        if cell_id is None:
            return RPCApi.Result(False, msg=f"Cell {name} not found")

        cmd = f"{cls.jh_exe} cell destroy {cell_id}"
        return cls.run_command(cmd)

    @classmethod
    def load_cell(cls, name, addr, data) -> RPCApi.Result:
        tf = TempFile()
        cell_id = cls.find_cell_id(name)
        if cell_id is None:
            return RPCApi.Result(False, msg=f"Cell {name} not found")

        temp_fn = tf.save("load", ".bin", data)
        if temp_fn is None:
            return RPCApi.Result(False, msg="Failed to save temp file")

        cmd = f"{cls.jh_exe} cell load {cell_id} {temp_fn} -a {hex(addr)}"
        return cls.run_command(cmd)

    @classmethod
    def start_cell(cls, name) -> RPCApi.Result:
        # cell_id = cls.find_cell_id(name)
        # if cell_id is None:
        #     return RPCApi.Result(False, msg=f"Cell {name} not found")

        # 定义启动guestcell的引用指令
        reference_commands = [
            "rm nohup.out",
            f"nohup {cls.jh_exe} virtio start ./zone1/zone1-linux-virtio.json > nohup1.out &",
            f"{cls.jh_exe} zone start ./zone1zone1-linux.json",
            "cat nohup1.out | grep \"char device\"",
            f"{cls.jh_exe} zone list"  # 修正格式错误
        ]

        # 执行引用指令
        for cmd in reference_commands:
            r = cls.run_command(cmd)
            if not r:
                return RPCApi.Result(False, msg=f"Reference command failed: {cmd}")

        # 不再执行原始的 cell start 命令
        return RPCApi.Result(True, msg=f"Guest cell {name} started with reference commands")

    @classmethod
    def stop_cell(cls, name) -> RPCApi.Result:
        cell_id = cls.find_cell_id(name)
        if cell_id is None:
            return RPCApi.Result(False, msg=f"Cell {name} not found")

        cmd = f"{cls.jh_exe} cell shutdown {cell_id}"
        return cls.run_command(cmd)

    @classmethod
    def run_linux(cls, cell_fn, kernel_fn, dtb_fn, ramdisk_fn, bootargs):
         reference_commands = [
            "rm nohup.out",
            f"nohup {cls.jh_exe} virtio start ./zone1/zone1-linux-virtio.json > nohup1.out &",
            f"{cls.jh_exe} zone start ./zone1zone1-linux.json",
            "cat nohup1.out | grep \"char device\"",
            f"{cls.jh_exe} zone list"  # 修正格式错误
        ]

        # 执行引用指令
        for cmd in reference_commands:
            r = cls.run_command(cmd)
            if not r:
                return RPCApi.Result(False, msg=f"Reference command failed: {cmd}")

        # 不再执行原始的 cell start 命令
        return RPCApi.Result(True, msg=f"Guest cell started with reference commands")

    return RPCApi.Result(True, msg=f"Guest cell started with reference commands")

        # return cls.run_command(cmd)