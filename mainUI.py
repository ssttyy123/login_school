from PyQt6.QtWidgets import *
import sys
import loginin


def createsis(userid, pas, operator):
    # 创建会话类enter_userid.get(), enter_pas.get(), operator_ddl.get()
    logina = loginin.Loginof(userid, pas, operator)
    logina.on_login()


class Mainwindow(QWidget):
    def __init__(self):
        super(Mainwindow, self).__init__()

    def initui(self):
        # 学号输入
        text_userid = QLabel('Student number:')
        enter_userid = QLineEdit()

        # 密码输入
        text_pas = QLabel('Password:')
        enter_pas = QLineEdit()
        # enter_pas.setEchoMode(QLineEdit.Password)

        # 运营商选择
        text_oper = QLabel('Select operator:')
        op_cbb = QComboBox()
        op_cbb.addItem("cmcc")
        op_cbb.addItem("chinanet")

        # 提交按钮
        subbutton = QPushButton("submit")

        # 标签列
        vboxl = QVBoxLayout()
        vboxl.addWidget(text_userid)
        vboxl.addWidget(text_pas)
        vboxl.addWidget(text_oper)

        # 输入组件列
        vboxaction = QVBoxLayout()
        vboxaction.addWidget(enter_userid)
        vboxaction.addWidget(enter_pas)
        vboxaction.addWidget(op_cbb)

        # 表单填写组
        hbox = QHBoxLayout()
        hbox.addLayout(vboxl)
        hbox.addLayout(vboxaction)

        # 整体布局
        vboxall = QVBoxLayout()
        vboxall.addLayout(hbox)
        vboxall.addWidget(subbutton)

        self.setWindowTitle("LoginSetting")
        self.setLayout(vboxall)
        self.setFixedSize(257, 125)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainui = Mainwindow()
    mainui.initui()

    sys.exit(app.exec())
