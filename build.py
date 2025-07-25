import os.path
from glob import glob
import datetime

uic = "pyside2-uic"
rcc = "pyside2-rcc"


def build_uic():
    ui_files = glob("forms/*.ui")
    count = 0
    for file in ui_files:
        path = os.path.dirname(file)
        name = os.path.splitext(os.path.basename(file))[0]
        output = os.path.join(path, f"ui_{name}.py")
        if not os.path.exists(output) or os.path.getmtime(file) > os.path.getmtime(output):
            cmd = f'{uic} -o {output} {file}'
            print(cmd)
            os.system(cmd)
            count = count + 1
    return count


def build_rcc():

    qrc_files = glob("assets/*.qrc", recursive=True)
    update = False

    for qrc in qrc_files:
        path = os.path.dirname(qrc)
        name = os.path.splitext(os.path.basename(qrc))[0]
        qrc_output = os.path.join(path, f"qr_{name}.py")
        if not os.path.exists(qrc_output):
            update = True
            break

        for file in glob("assets/**", recursive=True):
            if '__pycache__' in file:
                continue
            if os.path.getmtime(file) > os.path.getmtime(qrc_output):
                update = True
                break
        if update:
                break

    if not update:
        return 0

    for file in qrc_files:
        path = os.path.dirname(file)
        name = os.path.splitext(os.path.basename(file))[0]
        output = os.path.join(path, f"qr_{name}.py")

        cmd = f'{rcc} -o {output} {file}'
        os.system(cmd)

    return 1


def get_version():
    version = os.popen("git describe --tags --dirty=-dev").read()
    if len(version) == 0:
        version = "unknown"
    return version.strip()


def gen_version():
    version = get_version()

    now = datetime.datetime.now()
    with open("version.py", "wt") as f:
        f.write('# Generated, DO NOT MODIFY.\n\n')
        f.write(f"VERSION = '{version}'\n")
        f.write(f"BUILD_TIME = '{now}'\n")


def build_and_exit():
    gen_version()
    count = sum((0,
                 build_uic(),
                 build_rcc(),
                 ))
    if count > 0:
        print("Build file changed, try again.")
        exit()

def build():
    gen_version()
    count = sum((0,
                 build_uic(),
                 build_rcc(),
                 ))
    print("build:", count)
    return count


def deploy():
    version = get_version()

    exe = f'resource-tool-{version}'
    cmd = 'pyinstaller resource-tool.spec'
    if os.system(cmd) != 0:
        print("pyinstaller failed.")
        return None

    name_from = os.path.join("dist", "resource-tool-nonversion")
    name_to   = os.path.join("dist", exe)
    if os.path.exists(name_to):
        os.remove(name_to)
    os.rename(name_from, name_to)

    print("deploy finished", exe)
    return exe


def main():
    import sys
    if len(sys.argv) == 1:
        print("pre build.")
        build_uic()
        build_rcc()
        gen_version()
        print("pre build done.")
        return 0

    if sys.argv[1] == 'deploy':
        build_uic()
        build_rcc()
        gen_version()
        print("deploy.")
        exe = deploy()
        print(f"deploy done {exe}.")


if __name__ == '__main__':
    main()
