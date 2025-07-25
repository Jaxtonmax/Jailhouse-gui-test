import logging
from generator import RootCellGenerator, GuestCellGenerator
from jh_resource import Resource, ResourceGuestCell, ResourceRootCell  # 假设这些类在 jh_resource 模块中

# 配置日志
logging.basicConfig(level=logging.DEBUG)

# 实例化 Resource 对象，提供必要的参数
# 这里的 name 和 parent 可以根据实际情况进行调整
parent = None  # 假设没有父对象
name = "test_resource"
rsc = Resource(name, parent)

# 生成根单元格配置源码和二进制文件
root_cell_source = RootCellGenerator.gen_config_source(rsc)
root_cell_bin = RootCellGenerator.gen_config_bin(rsc)

if root_cell_source:
    print("Root Cell Config Source:")
    print(root_cell_source)
if root_cell_bin:
    print("Root Cell Config Binary:")
    print(root_cell_bin)

# 假设已经有了 ResourceGuestCell 对象
# 同样需要提供必要的参数来实例化 ResourceGuestCell
guest_cell_name = "test_guest_cell"
guest_cell = ResourceGuestCell(guest_cell_name, rsc)  # 假设父对象是 rsc

# 生成客户单元格配置源码和二进制文件
# 这里只是示例，实际的 GuestCellGenerator 可能需要调整以支持生成源码
guest_cell_bin = GuestCellGenerator.gen_config_bin(guest_cell)  # 假设存在此方法

if guest_cell_bin:
    print("Guest Cell Config Binary:")
    print(guest_cell_bin)