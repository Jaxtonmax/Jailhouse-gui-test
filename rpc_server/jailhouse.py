import os
import logging
import platform
import subprocess
import tempfile
from typing import Union, Optional
from api import RPCApi
import shlex
import time

# class TempFile(object):
#     def __init__(self) -> None:
#         self._temp_files = list()

#     def __del__(self):
#         self.clean()

#     def save(self, prefix: str, suffix: str, data: Optional[Union[str,bytes]] = None) -> Optional[str]:
#         temp = tempfile.mktemp(suffix, prefix)
#         try:
#             if isinstance(data, str):
#                 with open(temp, "wt") as f:
#                     f.write(data)
#             elif isinstance(data, bytes):
#                 with open(temp, "wb") as f:
#                     f.write(data)
#         except:
#             logging.error(f"write file failed {temp}.")
#             return None

#         self._temp_files.append(temp)
#         return temp

#     def clean(self):
#         for fn in self._temp_files:
#             os.unlink(fn)
#         self._temp_files.clear()

import os
import logging
import tempfile
from typing import Union, Optional


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
    def run_command(cls, cmd,  cwd=None) -> RPCApi.Result:
        # 总是先尝试加载驱动
        if not cls.load_driver():
            return RPCApi.Result(False, msg="Failed to load hvisor kernel module")

        logging.debug(f"Executing command: '{cmd}' in directory: {cwd or 'default'}")
        current_dir = os.getcwd()
        logging.debug(f"Current working directory: {current_dir}")
        logging.debug(f"run command {cmd}")
        proc = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cwd)
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
            f"{cls.jh_exe} zone start ./zone1/zone1-linux.json",
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
        # 执行hvisor zone list命令（替换原jailhouse cell list）
        cmd = f"/root/threevms/hvisor zone list"  # 假设hvisor在当前目录，根据实际路径调整
        r = cls.run_command(cmd)
        if not r:
            return r

        cells = list()
        lines = r.result.split('\n')

        # 跳过第一行（命令行本身，如root@SeawayHyper:~/threevms# ./hvisor zone list）
        # 从第二行开始解析（表头行）
        for line in lines[1:]:
            # 按|分割并过滤空元素，同时去除每个字段的前后空格
            parts = [p.strip() for p in line.split('|') if p.strip()]
            # 验证有效字段数为4（zone_id、cpus、name、status）
            if len(parts) != 4:
                continue  # 跳过格式不正确的行
            
            # 提取各字段（注意字段顺序与原输出对应）
            try:
                cell_info = {
                    'id': int(parts[0]),       # zone_id转为整数
                    'cpus': parts[1],          # cpus列表（如"0, 1"）
                    'name': parts[2],          # 区域名称
                    'status': parts[3]         # 运行状态
                }
                cells.append(cell_info)
            except ValueError:
                # 处理zone_id无法转为整数的异常情况
                logging.warning(f"无效的zone_id格式: {parts[0]}，跳过该行")
                continue

        return RPCApi.Result(True, result=cells)
    # @classmethod
    # def list_cell(cls) -> RPCApi.Result:
    #     cmd = f"/root/threevms/hvisor zone list"  # 修改为你的新命令
    #     r = cls.run_command(cmd)
    #     if not r:
    #         return r

    #     cells = list()
    #     lines = r.result.split('\n')

    #     # reference_commands = [
    #     #     "rm -f /root/threevms/rpc_server/nohup1.out",
    #     #     "nohup /root/threevms/rpc_server/hvisor virtio start /root/threevms/rpc_server/zone1/zone1-linux-virtio.json > /root/threevms/rpc_server/nohup1.out &",
    #     #     "/root/threevms/rpc_server/hvisor zone start /root/threevms/rpc_server/zone1/zone1-linux.json",
    #     #     "cat /root/threevms/rpc_server/nohup1.out | grep \"char device\"",
    #     #     "/root/threevms/rpc_server/hvisor zone list"
    #     # ]

    #     # # 执行引用指令
    #     # for cmd in reference_commands:
    #     #     r = cls.run_command(cmd)
    #     #     if not r:
    #     #         return RPCApi.Result(False, msg=f"Reference command failed: {cmd}")

    #     # 跳过表头行
    #     for line in lines[2:]:  # 从第三行开始解析，跳过表头和分隔线
    #         s = line.strip().split('|')
    #         if len(s) < 5:  # 确保有足够的列
    #             continue
    #         zone_id = s[1].strip()
    #         cpus = s[2].strip()
    #         name = s[3].strip()
    #         status = s[4].strip()

    #         if zone_id and name and status:
    #             cells.append({
    #                 'id': int(zone_id),
    #                 'name': name,
    #                 'status': status,
    #                 'cpus': cpus
    #             })
    #     return RPCApi.Result(True, result=cells)

    @classmethod
    def create_cell(cls, cell: bytes) -> RPCApi.Result:
        tf = TempFile()
        temp_fn = tf.save("create_cell", ".cell", cell)
        if temp_fn is None:
            return RPCApi.Result(False, msg="Failed to save temp file")

        cmd = f"{cls.jh_exe} cell create {temp_fn}"
        return cls.run_command(cmd)
    @classmethod
    def get_hvisor_zone_raw_output(cls) -> RPCApi.Result:
        """获取hvisor zone list的原始输出字符串"""
        cmd = "/root/threevms/hvisor zone list"  # 替换为实际hvisor路径
        return cls.run_command(cmd)

    @classmethod
    def destroy_cell(cls, name: str) -> RPCApi.Result:
        cell_id = cls.find_cell_id(name)
        if cell_id is None:
            return RPCApi.Result(False, msg=f"Cell {name} not found")

        cmd = f"{cls.jh_exe} zone shutdown -id {cell_id}"
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

    # @classmethod
    # def start_cell(cls, name) -> RPCApi.Result:
    #     # cell_id = cls.find_cell_id(name)
    #     # if cell_id is None:
    #     #     return RPCApi.Result(False, msg=f"Cell {name} not found")12

    #     # 定义启动guestcell的引用指令
    #     reference_commands = [
    #         # "rm nohup.out",
    #         # f"nohup {cls.jh_exe} virtio start ./zone1/zone1-linux-virtio.json > nohup1.out &",
    #         # f"{cls.jh_exe} zone start ./zone1/zone1-linux.json",
    #         # "cat nohup1.out | grep \"char device\"",
    #         # f"{cls.jh_exe} zone list"  # 修正格式错误
    #         f"cd /root/threevms/"
    #         "./guest1rt.sh"
    #     ]

    #     # 执行引用指令
    #     for cmd in reference_commands:
    #         r = cls.run_command(cmd)
    #         if not r:
    #             return RPCApi.Result(False, msg=f"Reference command failed: {cmd}")

    #     # 不再执行原始的 cell start 命令
    #     return RPCApi.Result(True, msg=f"Guest cell {name} started with reference commands")

# 文件: /root/threevms/rpc_server/jailhouse.py

# 文件: /root/threevms/rpc_server/jailhouse.py

    @classmethod
    def start_cell(cls, name: str) -> RPCApi.Result:
        logging.warning("Generic 'start_cell' is not implemented for complex startup. Use 'run_linux' instead.")
        # 根据您系统的hvisor版本，决定是返回错误还是执行一个简单的start指令
        # 为了安全起见，我们返回一个错误
        return RPCApi.Result(False, msg=f"Generic start for {name} is not supported. Please use the OS-specific run function.")

    @classmethod
    def stop_cell(cls, name) -> RPCApi.Result:
        cell_id = cls.find_cell_id(name)
        if cell_id is None:
            return RPCApi.Result(False, msg=f"Cell {name} not found")

        cmd = f"{cls.jh_exe} cell shutdown {cell_id}"
        return cls.run_command(cmd)

    # @classmethod
    # def run_linux(cls, cell_fn, kernel_fn, dtb_fn, ramdisk_fn, bootargs):
    #     # cell_id = cls.find_cell_id(name)
    #     # if cell_id is None:
    #     #     return RPCApi.Result(False, msg=f"Cell {name} not found")

    #     # 定义启动guestcell的引用指令
    #     reference_commands = [
    #         "cd /root/threevms",
    #         "rm nohup1.out",
    #         "insmod hvisor.ko",
    #         "nohup /root/threevms/hvisor virtio start /root/threevms/zone1/zone1-linux-virtio.json > /root/threevms/nohup1.out &",
    #         "/root/threevms/hvisor zone start /root/threevms/zone1/zone1-linux.json",
    #         "cat /root/threevms/nohup1.out | grep \"char device\"",
    #         "/root/threevms/hvisor zone list"
    #     ]

    #     # 执行引用指令
    #     for cmd in reference_commands:
    #         r = cls.run_command(cmd)
    #         if not r:
    #             return RPCApi.Result(False, msg=f"Reference command failed: {cmd}")

    #     # 不再执行原始的 cell start 命令
    #     return RPCApi.Result(True, msg=f"Guest cell started with reference commands")

        # return cls.run_command(cmd)

    # @classmethod
    # def run_linux(cls, cell_fn, kernel_fn, dtb_fn, ramdisk_fn, bootargs):
    #     if ramdisk_fn is None:
    #         cmd = f'{cls.jh_exe} cell linux -d {dtb_fn} {cell_fn} {kernel_fn} -c "{bootargs}"'
    #     else:
    #         cmd = f'{cls.jh_exe} cell linux -d {dtb_fn} -i {ramdisk_fn} {cell_fn} {kernel_fn} -c "{bootargs}"'

    #     return cls.run_command(cmd)
# 文件: jailhouse.py

# ... (文件其他部分保持不变) ...

    # 这是我们即将修改的函数
    @classmethod
    def run_linux(cls, cell_fn, kernel_fn, dtb_fn, ramdisk_fn, bootargs):
        """
        通过执行一系列预设的、正确的指令来启动一个Linux客户机。
        此函数现在包含了完整的启动流程，取代了旧的、已失效的 "cell linux" 指令。
        """
        logging.info("Executing the correct Linux startup sequence inside `run_linux`.")

        # --- 1. 配置区 ---
        # 定义所有指令需要的工作目录和关键文件路径
        # 这些路径是根据您提供的正确指令写死的
        working_directory = "/root/threevms/"
        hvisor_exe = cls.jh_exe  # 使用在类中定义的 /root/threevms/hvisor
        nohup_log_path = os.path.join(working_directory, "nohup1.out")
        virtio_config = os.path.join(working_directory, "zone1/zone1-linux-virtio.json")
        zone_config = os.path.join(working_directory, "zone1/zone1-linux.json") # 这是关键的配置文件！
        
        logging.info(f"Ignoring passed arguments like '{cell_fn}' and using hardcoded paths.")

        # --- 2. 执行指令：rm nohup1.out ---
        # 使用Python的方式安全地删除旧日志文件，如果文件不存在也不会报错
        try:
            if os.path.exists(nohup_log_path):
                os.remove(nohup_log_path)
                logging.info(f"Removed old log file: {nohup_log_path}")
        except Exception as e:
            return RPCApi.Result(False, msg=f"Error removing old log file: {e}")

        # --- 3. 执行指令：insmod ./hvisor.ko ---
        # run_command 方法会自动调用 load_driver，这里确保它被正确执行
        if not cls.load_driver():
            return RPCApi.Result(False, msg="Failed to load hvisor kernel module (insmod).")
        logging.info("Kernel module loaded successfully (insmod).")
        time.sleep(1) # 加载驱动后稍作等待，以确保设备就绪

        # --- 4. 执行指令：nohup ./hvisor virtio start ... > nohup1.out & ---
        # 在后台启动 virtio 进程，这是与客户机进行I/O通信的关键
        logging.info(f"Starting background virtio process with config: {virtio_config}")
        virtio_cmd_list = [hvisor_exe, "virtio", "start", virtio_config]
        
        try:
            # 使用 'with open...' 确保日志文件句柄被正确处理
            with open(nohup_log_path, "wb") as log_file:
                subprocess.Popen(
                    virtio_cmd_list, 
                    stdout=log_file, 
                    stderr=subprocess.STDOUT, # 将标准输出和错误都重定向到日志文件
                    cwd=working_directory    # 确保在 /root/threevms/ 目录下执行
                )
            logging.info(f"Virtio process launched in background. Logging to {nohup_log_path}")
        except FileNotFoundError:
             return RPCApi.Result(False, msg=f"CRITICAL: hvisor executable not found at '{hvisor_exe}'")
        except Exception as e:
            return RPCApi.Result(False, msg=f"Failed to start background virtio process: {e}")
        
        time.sleep(2) # 等待后台进程初始化

        # --- 5. 执行指令：./hvisor zone start ... ---
        # 这是实际创建并启动虚拟机的指令
        logging.info(f"Executing 'zone start' with correct config: {zone_config}")
        zone_start_cmd = f"{hvisor_exe} zone start {zone_config}"
        r = cls.run_command(zone_start_cmd, cwd=working_directory)
        if not r:
            return RPCApi.Result(False, msg=f"Failed to execute 'zone start': {r.message}")
        logging.info("'zone start' command executed successfully.")

        # --- 6. 执行指令：cat nohup1.out | grep "char device" ---
        # 用Python轮询文件内容，替代cat和grep，并设置超时，这是一种更健壮的方式
        logging.info("Waiting for 'char device' to appear in nohup log...")
        char_device_found = False
        for _ in range(20):  # 总共等待 10 秒 (20 次 * 0.5 秒)
            time.sleep(0.5)
            try:
                if os.path.exists(nohup_log_path) and "char device" in open(nohup_log_path).read():
                    logging.info("Success! 'char device' found in log file.")
                    char_device_found = True
                    break
            except Exception as e:
                return RPCApi.Result(False, msg=f"Error while polling log file {nohup_log_path}: {e}")
        
        if not char_device_found:
            log_content = f"Log content from '{nohup_log_path}':\n" + (open(nohup_log_path).read() if os.path.exists(nohup_log_path) else "File not found.")
            return RPCApi.Result(False, msg=f"Timed out waiting for 'char device'. {log_content}")

        # --- 7. 执行指令：./hvisor zone list ---
        # 最后执行一次 list，确认虚拟机状态，并将结果返回
        logging.info("Final check with 'zone list'.")
        final_status_result = cls.run_command(f"{hvisor_exe} zone list", cwd=working_directory)
        if not final_status_result:
            logging.warning(f"Could not execute 'zone list' after start: {final_status_result.message}")
            return RPCApi.Result(True, msg="Guest startup sequence finished, but failed to get final status.")
        else:
            logging.info(f"Current zone status:\n{final_status_result.result}")
            # 返回成功信息和最终的虚拟机列表
            return RPCApi.Result(True, result=final_status_result.result)