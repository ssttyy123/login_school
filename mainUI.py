import win32api
import winreg
import win32con
from PyQt6 import QtGui, QtCore
from PyQt6.QtCore import QCoreApplication
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import *

import sys
import os

import loginin
import logindata


def createsis(mainwindow, userid, pas, operator):
    # 创建会话类
    logina = loginin.Loginof(userid, pas, operator)
    rt = logina.on_login()
    # 1 IP终端已经在线
    # 2 验证失败
    # 3 登录成功
    return rt


def auto_start(situ):
    # (0,1,2)存在键，不存在键，权限不足
    reg_path = r'Software\Microsoft\Windows\CurrentVersion\Run'
    execpath = os.path.realpath(sys.argv[0])
    key = winreg.OpenKey(win32con.HKEY_CURRENT_USER, reg_path, 0, win32con.KEY_ALL_ACCESS)
    try:
        rt = winreg.QueryValueEx(key, 'login_school')[1]
        # 存在键
        if situ == "close":
            if rt == 1:
                win32api.RegDeleteValue(key, "login_school")
                win32api.RegCloseKey(key)
    except FileNotFoundError as e:
        # 不存在键
        if situ == "open":
            win32api.RegSetValueEx(key, "login_school", 0, win32con.REG_SZ, execpath)
            win32api.RegCloseKey(key)


class Mainwindow(QWidget):
    def __init__(self):
        super(Mainwindow, self).__init__()
        # 学号输入
        self.text_userid = QLabel('Student number:')
        self.enter_userid = QLineEdit()

        # 密码输入
        self.text_pas = QLabel('Password:')
        self.enter_pas = QLineEdit()
        self.enter_pas.setEchoMode(QLineEdit.EchoMode.Password)

        # 运营商选择
        self.text_oper = QLabel('Select operator:')
        self.op_cbb = QComboBox()
        self.op_cbb.addItem("cmcc")
        self.op_cbb.addItem("chinanet")

        # 提交按钮
        self.subbutton = QPushButton("submit")

        # 开机自启选择框
        self.text_sta = QLabel('auto-start:')
        self.startCheckbox = QCheckBox()

        # 用户历史数据
        '''{"id": "templateUser",
                 "pas": "123456",
                 "ope": 0}'''
        self.database = logindata.usersdata()
        self.enter_userid.setText(self.database.rutdefaultuesr()['id'])
        self.enter_pas.setText(self.database.rutdefaultuesr()['pas'])
        self.op_cbb.setCurrentIndex(self.database.rutdefaultuesr()['ope'])
        self.startCheckbox.setChecked(self.database.rutdefaultuesr()['auto_start'])

    def initui(self):
        # 标签列
        vboxl = QVBoxLayout()
        vboxl.addWidget(self.text_userid)
        vboxl.addWidget(self.text_pas)
        vboxl.addWidget(self.text_oper)

        # 输入组件列
        vboxaction = QVBoxLayout()
        vboxaction.addWidget(self.enter_userid)
        vboxaction.addWidget(self.enter_pas)
        vboxaction.addWidget(self.op_cbb)

        # 表单填写组
        hbox = QHBoxLayout()
        hbox.addLayout(vboxl)
        hbox.addLayout(vboxaction)

        # 提交按钮，开机自启选项行
        ablehbox = QHBoxLayout()
        ablehbox.addWidget(self.text_sta)
        ablehbox.addWidget(self.startCheckbox)
        ablehbox.addStretch(1)
        ablehbox.addWidget(self.subbutton)

        # 整体布局
        vboxall = QVBoxLayout()
        vboxall.addLayout(hbox)
        vboxall.addLayout(ablehbox)

        self.setWindowTitle("LoginSetting")
        self.setLayout(vboxall)
        # self.setFixedSize(257, 125)
        self.show()


def quitwin():
    QCoreApplication.exit(0)


class systray(QSystemTrayIcon):
    def __init__(self, mainwindow, parent=None):
        super(QSystemTrayIcon, self).__init__(parent)
        self.menu = None
        self.autoflag = 1
        self.actionset = QAction("Setting", self)
        self.actionquit = QAction("Quit", self)
        self.actionset.triggered.connect(self.showui)
        self.actionquit.triggered.connect(quitwin)
        self.mainwindow = mainwindow
        self.creatMenu()
        # 提交按钮
        mainwindow.subbutton.clicked.connect(lambda: self.onclicksub())

    def onclicksub(self):
        createsis(self.mainwindow, self.mainwindow.enter_userid.text(),
                  self.mainwindow.enter_pas.text(),
                  self.mainwindow.op_cbb.currentText())
        if self.mainwindow.startCheckbox.isChecked():
            auto_start("open")
            self.autoflag = 1
        elif not self.mainwindow.startCheckbox.isChecked():
            auto_start("close")
            self.autoflag = 0
        self.mainwindow.database.changefault(self.mainwindow.enter_userid.text(),
                                             self.mainwindow.enter_pas.text(),
                                             self.mainwindow.op_cbb.currentIndex(),
                                             self.autoflag)
        self.mainwindow.showMinimized()
        self.mainwindow.setWindowFlags(QtCore.Qt.WindowType.SplashScreen | QtCore.Qt.WindowType.FramelessWindowHint)

    def creatMenu(self):
        self.menu = QMenu()
        self.menu.addAction(self.actionset)
        self.menu.addAction(self.actionquit)
        self.setContextMenu(self.menu)

        self.setIcon(QtGui.QIcon(r".\res\connect.ico"))
        self.mainwindow.setWindowFlags(QtCore.Qt.WindowType.SplashScreen | QtCore.Qt.WindowType.FramelessWindowHint)

    def showui(self):
        self.mainwindow.showNormal()
        self.mainwindow.activateWindow()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainui = Mainwindow()
    mainui.initui()
    mainui.setWindowFlags(QtCore.Qt.WindowType.SplashScreen | QtCore.Qt.WindowType.FramelessWindowHint)
    tray = systray(mainui)
    tray.onclicksub()
    tray.show()

    sys.exit(app.exec())
