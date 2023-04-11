# coding=utf-8
# 开发者：xxx
# 开发时间： 12:23 
# "Stay hungry，stay foolish."

# !/usr/bin/env python
# -*- coding:utf-8 -*-

import HW_button
import os, sys


try:
    from tkinter import *
except ImportError:  # Python 2.x
    PythonVersion = 2
    from Tkinter import *
    from tkFont import Font
    from ttk import *
    # Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
    from tkMessageBox import *
    # Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
    # import tkFileDialog
    # import tkSimpleDialog
else:  # Python 3.x
    PythonVersion = 3
    from tkinter.font import Font
    from tkinter.ttk import *
    from tkinter.messagebox import *
    # import tkinter.filedialog as tkFileDialog
    # import tkinter.simpledialog as tkSimpleDialog    #askstring()


class Application_ui(Frame):
    # 这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None, **kw):
        Frame.__init__(self, master)
        super().__init__(master, **kw)
        self.master.title('登录界面')
        self.master.geometry('393x235')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        # 标题
        self.style.configure('登录.TLabel', anchor='w', font=('宋体', 12))
        self.登录 = Label(self.top, text='登录', style='登录.TLabel')
        self.登录.place(relx=0.346, rely=0.136, relwidth=0.328, relheight=0.106)

        # 文本框1
        self.userVar = StringVar(value='user')
        self.user = Entry(self.top, text='Text1', textvariable=self.userVar, font=('宋体', 9))
        self.user.place(relx=0.346, rely=0.306, relwidth=0.369, relheight=0.106)

        # 文本框2
        self.pwdVar = StringVar(value='pwd')
        self.pwd = Entry(self.top, text='Text1', textvariable=self.pwdVar, font=('宋体', 9))
        self.pwd.place(relx=0.346, rely=0.477, relwidth=0.369, relheight=0.106)

        # 文本框前的文字
        self.style.configure('账户.TLabel', anchor='w', font=('宋体', 9))
        self.username = Label(self.top, text='账户', style='账户.TLabel')
        self.username.place(relx=0.122, rely=0.306, relwidth=0.165, relheight=0.106)

        # 文本框前的文字
        self.style.configure('密码.TLabel', anchor='w', font=('宋体', 9))
        self.pwdname = Label(self.top, text='密码', style='密码.TLabel')
        self.pwdname.place(relx=0.122, rely=0.477, relwidth=0.165, relheight=0.106)

        self.style.configure('but1.TButton', font=('宋体', 9))
        self.but1 = Button(self.top, text='提交', command=self.but1_Cmd, style='but1.TButton')
        self.but1.place(relx=0.326, rely=0.749, relwidth=0.267, relheight=0.106)


class Application(Application_ui):
    # 这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def but1_Cmd(self, event=None):
        # TODO, Please finish the function here!
        pwd = self.pwdVar.get()
        user = self.userVar.get()
        print(pwd, "   ", user)
        Tk().destroy()
        HW_button.Applicationbut(Tk()).mainloop()
        return user, pwd
        pass


if __name__ == "__main__":
    # top = Tk()
    Application(Tk()).mainloop()
    # try:
    #     top.destroy()
    # except:
    #     pass
