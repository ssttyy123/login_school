import ctypes
import json
import sys
import os

# exe于命令台运行，
'''
    :param --程序路径
    :param --进程名
'''


def writinpath():
    """
    json

    """
    datext = {'path': 'EOF',
              'name': 'None'}
    execpath = ' '
    exename = ' '
    if os.path.exists(r".\tempdata.json"):
        dataf = open(r".\tempdata.json")
        datext = json.load(dataf)
        execpath = datext['path']
        exename = datext['name']
        dataf.close()
        os.remove(r".\tempdata.json")
    else:
        datext['path'] = sys.argv[1]
        datext['name'] = sys.argv[2]
        dataf = open(r".\tempdata.json", 'w')
        json.dump(datext, dataf)
        dataf.close()

    if is_admin():
        start_path = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup'
        # 首参数（文件路径）
        # 盘操作符
        rootflag = execpath[0]
        tbat = rootflag + ':\ncd ' + execpath + '\nstart ' + exename
        fp = open(start_path + r"\login_school.bat", 'w')
        fp.write(tbat)
        fp.close()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if __name__ == '__main__':
    writinpath()
    print(type(sys.argv[1]), type("aa"))
