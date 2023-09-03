from PyQt6.QtWidgets import *


class Warningbox:
    def __init__(self, wtype):
        self.wcode = wtype
        self.messbox = QMessageBox()

    @classmethod
    def popWin(cls, mainwindow, mes, messbox):
        messbox.information(mainwindow, 'Warning', mes,
                            QMessageBox.StandardButton.Ok,
                            QMessageBox.StandardButton.Cancel)

    def jugmess(self, mainwindow):
        if self.wcode[0] == 1:
            pass
        elif self.wcode[0] == 0:
            if self.wcode[1] == 2:
                self.popWin(mainwindow, "已登录", self.messbox)
            elif self.wcode[1] == 1:
                self.popWin(mainwindow, "请检查学号或者密码是否错误！", self.messbox)
            else:
                self.popWin(mainwindow, "未知问题，请联系开发者修补问题！", self.messbox)
        elif self.wcode[0] == 3:
            self.popWin(mainwindow, "无互联网连接", self.messbox)
        else:
            self.popWin(mainwindow, "未知问题，请联系开发者修补问题！", self.messbox)
