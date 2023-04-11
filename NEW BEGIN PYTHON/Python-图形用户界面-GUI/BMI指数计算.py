from tkinter import *

top = Tk()  # 创建窗口

# 变量及事件处理函数
ABC = StringVar()  # 与Entry关联的变量，StringVar是Tk库内部定义的字符串变量类型
ABC2 = StringVar()  # 与Entry关联的变量，StringVar是Tk库内部定义的字符串变量类型


def calculate():  # 按钮按下后要执行的函数

    height = int(ABC.get())  # 获取输入框中的值
    weight = int(ABC2.get())  # 获取输入框中的值
    bmi = weight / (height * height)
    print("bmi=", bmi)
    if bmi < 18.5:
        result = f"f:.5{bmi}=bmi,偏瘦"
    elif bmi > 23.9:
        result = f"f:.5{bmi}=bmi,偏胖"
    else:
        result = f"f:.5{bmi}=bmi,正常"

    label.config(text=result)  # 显示到标签上


top.title("计算BMI：")  # 设置窗口标题
top.geometry("400x220")

entry = Entry(top, textvariable=ABC, width=20)  # 创建输入框组件
entry.place(x=100, y=50)  # 显示Entry组件

entry = Entry(top, textvariable=ABC2, width=20)  # 创建输入框组件
entry.place(x=100, y=70)  # 显示Entry组件

button = Button(top, text="进行转换", command=calculate, width=20)  # 创建按钮组件
button.place(x=100, y=100)  # 显示按钮组件
# 按钮
button = Button(top, text="进行转换", command=calculate, width=20)  # 创建按钮组件
button.place(x=100, y=100)  # 显示按钮组件
# 标签
label = Label(top, text="计算结果", width=20)
# 创建按钮组件
label.place(x=100, y=150)  # 显示标签组件
# 初始化变量
ABC.set('170')  # 设置变量的初始值
ABC2.set('60')  # 设置变量的初始值
# 显示主窗口
top.mainloop()
