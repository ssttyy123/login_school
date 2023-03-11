from PyQt6 import QtGui, QtCore
from PyQt6.QtCore import QCoreApplication
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import *

import sys
import os

import loginin
import logindata
import warningbox


def createsis(mainwindow, userid, pas, operator):
    # 创建会话类
    logina = loginin.Loginof(userid, pas, operator)
    rt = logina.on_login()
    wmess = warningbox.Warningbox(rt)
    wmess.jugmess(mainwindow)
    return rt


def quitwin():
    QCoreApplication.exit(0)


def writinpath(situ):
    start_path = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup'
    flag = os.path.exists(start_path + r"\login_school.bat")
    propath = os.path.abspath('.')
    if flag:
        if situ == "close":
            os.remove(start_path + r"\login_school.bat")
    else:
        if situ == "open":
            print("adminper.exe " + propath + ' ' + os.path.basename(sys.argv[0]))
            os.system("adminper.exe " + propath + ' ' + os.path.basename(sys.argv[0]))


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
        self.op_cbb.addItem("中国移动")
        self.op_cbb.addItem("中国联通")

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
        rt = createsis(self.mainwindow, self.mainwindow.enter_userid.text(),
                       self.mainwindow.enter_pas.text(),
                       self.mainwindow.op_cbb.currentText())
        if self.mainwindow.startCheckbox.isChecked():
            writinpath("open")
            self.autoflag = 1
        elif not self.mainwindow.startCheckbox.isChecked():
            writinpath("close")
            self.autoflag = 0
        if rt <= 1:
            self.mainwindow.database.changefault(self.mainwindow.enter_userid.text(),
                                                 self.mainwindow.enter_pas.text(),
                                                 self.mainwindow.op_cbb.currentIndex(),
                                                 self.autoflag)
            self.mainwindow.showMinimized()
            self.mainwindow.setWindowFlags(QtCore.Qt.WindowType.SplashScreen | QtCore.Qt.WindowType.FramelessWindowHint)
            self.mainwindow.hide()

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
