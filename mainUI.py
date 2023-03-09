from tkinter import *
from tkinter import ttk
import ctypes
import loginin


def center_win(root, width, height):
    size = '%dx%d+%d+%d' % (width, height, (root.winfo_screenwidth() - width) / 2,
                            (root.winfo_screenheight() - height) / 2)
    root.geometry(size)
    root.update()
    root.resizable(0, 0)


def createsis(userid, pas, operator):
    # 创建会话类enter_userid.get(), enter_pas.get(), operator_ddl.get()
    logina = loginin.Loginof(userid, pas, operator)
    logina.on_login()


ctypes.windll.shcore.SetProcessDpiAwareness(1)
ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
mainwindow = Tk()
# 居中
# center_win(mainwindow, 410, 150)
mainwindow.title("LoginSetting")
mainwindow.tk.call('tk', 'scaling', ScaleFactor/75)
# 学号输入
text_userid = Label(mainwindow, text="Student number:")
text_userid.grid(row=0, column=0, padx=(10, 2), pady=10)
enter_userid = Entry(mainwindow, bd=5)
enter_userid.grid(row=0, column=1, padx=(0, 10), pady=(20, 10))
# 密码输入
text_pas = Label(mainwindow, text="Password:")
text_pas.grid(row=1, column=0, padx=(10, 2), pady=10)
enter_pas = Entry(mainwindow, bd=5)
enter_pas.config(show='*')
enter_pas.grid(row=1, column=1, padx=(0, 10), pady=10)
# 运营商选择
text_operator = Label(mainwindow, text="Select operator:")
text_operator.grid(row=3, column=0, padx=(10, 0), pady=5)
operator_ddl = ttk.Combobox(mainwindow, width=15)
operator_ddl.grid(row=3, column=1, padx=(0, 10), pady=5)
operator_ddl['value'] = ("cmcc", "chinanet")
operator_ddl.config(state='readonly')
operator_ddl.current(0)
# 提交按钮
sub_button = Button(mainwindow, text="submit", height=1,
                    command=lambda: createsis(enter_userid.get(), enter_pas.get(), operator_ddl.get()))
sub_button.grid(row=4, column=1, padx=(0, 10), pady=(5, 10))
mainwindow.mainloop()
