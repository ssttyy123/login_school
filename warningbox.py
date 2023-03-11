from PyQt6.QtWidgets import *
import time

'''
0.You have successfully logged into our system.
1.IP already online
2.Failed to authenticate user
3.Please check the network configuration and confirm the account number and password is correct！ 
4.Account does not exist or not bind isp account.
20.unknowerr
'''


class Warningbox:
    def __init__(self, wtype):
        self.wcode = wtype
        self.messbox = QMessageBox()

    def jugmess(self, mainwindow):
        if self.wcode == 0:
            pass
        elif self.wcode == 1:
            self.messbox.information(mainwindow, 'Online', 'IP已经在线',
                                     QMessageBox.StandardButton.Ok,
                                     QMessageBox.StandardButton.Cancel)
        elif self.wcode == 2:
            self.messbox.information(mainwindow, 'Warning', '请检查学号或者密码是否错误！',
                                     QMessageBox.StandardButton.Ok,
                                     QMessageBox.StandardButton.Cancel)
        elif self.wcode == 3:
            self.messbox.information(mainwindow, 'Warning', '网络连接错误或者账号密码错误！',
                                     QMessageBox.StandardButton.Ok,
                                     QMessageBox.StandardButton.Cancel)
        elif self.wcode == 4:
            self.messbox.information(mainwindow, 'Warning', '运营商不存在该账户！',
                                     QMessageBox.StandardButton.Ok,
                                     QMessageBox.StandardButton.Cancel)
        else:
            self.messbox.information(mainwindow, 'Warning', '未知问题，请联系开发者修补问题！',
                                     QMessageBox.StandardButton.Ok,
                                     QMessageBox.StandardButton.Cancel)
