from PyQt6 import QtGui, QtCore
from PyQt6.QtCore import QCoreApplication
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import *
import sys

import loginin


def createsis(mainwindow, userid, pas, operator):
    # 创建会话类
    logina = loginin.Loginof(userid, pas, operator)
    logina.on_login()
    mainwindow.showMinimized()
    mainwindow.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)


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

        self.subbutton = QPushButton("submit")

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

        # 整体布局
        vboxall = QVBoxLayout()
        vboxall.addLayout(hbox)
        vboxall.addWidget(self.subbutton)

        self.setWindowTitle("LoginSetting")
        self.setLayout(vboxall)
        self.setFixedSize(257, 125)
        self.show()


def quitwin():
    QCoreApplication.exit(0)


class systray(QSystemTrayIcon):
    def __init__(self, mainwindow, parent=None):
        super(QSystemTrayIcon, self).__init__(parent)
        self.menu = None
        self.actionset = QAction("Setting", self)
        self.actionquit = QAction("Quit", self)
        self.actionset.triggered.connect(self.showui)
        self.actionquit.triggered.connect(quitwin)
        self.mainwindow = mainwindow
        self.creatMenu()
        # 提交按钮
        mainwindow.subbutton.clicked.connect(lambda: createsis(mainwindow, mainwindow.enter_userid.text(),
                                                               mainwindow.enter_pas.text(),
                                                               mainwindow.op_cbb.currentText()))

    def creatMenu(self):
        self.menu = QMenu()
        self.menu.addAction(self.actionset)
        self.menu.addAction(self.actionquit)
        self.setContextMenu(self.menu)

        self.setIcon(QtGui.QIcon("C:\\Users\\13598\\Desktop\\res\\connect.ico"))
        self.mainwindow.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)

    def showui(self):
        self.mainwindow.showNormal()
        self.mainwindow.activateWindow()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainui = Mainwindow()
    mainui.initui()
    tray = systray(mainui)
    tray.show()

    sys.exit(app.exec())
