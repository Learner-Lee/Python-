# coding=utf-8
# 开发者：xxx
# 开发时间： 12:24 
# "Stay hungry，stay foolish."

import HW_loding
import os, sys
try:
    from tkinter import *
except ImportError:  #Python 2.x
    PythonVersion = 2
    from Tkinter import *
    from tkFont import Font
    from ttk import *
    #Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
    from tkMessageBox import *
    #Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
    #import tkFileDialog
    #import tkSimpleDialog
else:  #Python 3.x
    PythonVersion = 3
    from tkinter.font import Font
    from tkinter.ttk import *
    from tkinter.messagebox import *
    #import tkinter.filedialog as tkFileDialog
    #import tkinter.simpledialog as tkSimpleDialog    #askstring()

class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('Form1')
        self.master.geometry('417x259')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.style.configure('Command1.TButton',font=('宋体',9))
        self.but1 = Button(self.top, text='1', command=self.but1_Cmd, style='Command1.TButton')
        self.but1.place(relx=0.100, rely=0.150, relwidth=0.350, relheight=0.170)

        self.style.configure('Command4.TButton',font=('宋体',9))
        self.but2 = Button(self.top, text='2', command=self.but2_Cmd, style='Command4.TButton')
        self.but2.place(relx=0.500, rely=0.150, relwidth=0.350, relheight=0.170)

        self.style.configure('Command5.TButton',font=('宋体',9))
        self.but3 = Button(self.top, text='3', command=self.but3_Cmd, style='Command5.TButton')
        self.but3.place(relx=0.100, rely=0.400, relwidth=0.350, relheight=0.170)

        self.style.configure('Command3.TButton',font=('宋体',9))
        self.but4 = Button(self.top, text='4', command=self.but4_Cmd, style='Command3.TButton')
        self.but4.place(relx=0.500, rely=0.400, relwidth=0.350, relheight=0.170)

        self.style.configure('Command2.TButton',font=('宋体',9))
        self.but5 = Button(self.top, text='返回', command=self.but5_Cmd, style='Command2.TButton')
        self.but5.place(relx=0.633, rely=0.772, relwidth=0.350, relheight=0.170)


class Applicationbut(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def but1_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def but2_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def but3_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def but4_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def but5_Cmd(self, event=None):
        #TODO, Please finish the function here!

        Tk().destroy()
        HW_loding.Application(Tk()).mainloop()

        pass



if __name__ == "__main__":
    # top = Tk()
    Applicationbut(Tk()).mainloop()
    # try: top.destroy()
    # except: pass
