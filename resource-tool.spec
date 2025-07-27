# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['mainui.py'],
    pathex=['.'],  # 确保项目根目录在搜索路径
    binaries=[],
    datas=[
        # 直接包含vm_manage_widget.py文件（关键！）
        ('vm_manage_widget.py', '.'),  # 第一个参数是源文件路径，第二个是打包后的路径（当前目录）
        ('platform', 'platform'),
        ('demos', 'demos'),
        ('assets/template', 'template'),
        ('tools', 'tools'),
        ('forms/ui_vm_manager.py', 'forms'),
        ('forms/ui_vm_state_item.py', 'forms'),
        ('forms/ui_meminfo.py', 'forms'),
        ('forms/ui_cpuload.py', 'forms'),
        ('forms/ui_*.py', 'forms'),
        ('config_convert.py','.'),
    ],
    hiddenimports=[
        'vm_manage_widget',  # 双重保险：声明为隐藏导入
        'config_convert',
        'commonos_runinfo',
        'linux_runinfo',
        'acore_runinfo',
        'rpc_server.rpc_client',
        'generator',
        'jh_resource',
        'utils',
        'rpc_server',
        'rpc_server.rpc_client',
        'rpc_server.api',
        'cpu_edit_widget',  # 显式声明 CPUEditWidget 模块
        'forms.ui_cpu_edit_widget',  # 显式声明 UI 模块
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='resource-tool-nonversion',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,  # 保持控制台输出，便于查看详细日志
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='assets/images/logo_0.ico'
)