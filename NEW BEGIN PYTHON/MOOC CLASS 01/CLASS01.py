# import math
# R = int(input("圆的半径："))
# area = math.pi * R * R
# print("结果为：",area)
# print("结果为：{:.2f}".format(area)) # 确定小数点保留位数


# import turtle
# turtle.pensize(2)
# turtle.circle(10)
# turtle.circle(40)
# turtle.circle(80)
# turtle.circle(120)
# turtle.circle(160)
# turtle.done()


# from turtle import *
# color("red","red")
# begin_fill()
# for i in range(5):
#     fd(200)
#     rt(144)
# end_fill()
# done()



""" 温度转换 """
TempStr = input("请输入带有符号的温度值：")
if TempStr[-1] in ['F','f']:
    C = (eval(TempStr[0:-1]) - 32)/1.8
    print("转换后的温度是{:.2f}".format(C))
elif TempStr[-1] in ['C','c']:
    F = 1.8*eval(TempStr[0:-1]) + 32
    print("转换后的温度是{:.2f}".format(F))
else:
    print("输入格式错误！")