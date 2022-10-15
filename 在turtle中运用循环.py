#  矩形
# import turtle
# for i in range(10):
#     turtle.forward(100+10*i)
#     turtle.right(90)
###############################
#  五角星
# from turtle import *
# color("red")
# begin_fill()
# for i in range(5):
#     forward(150)
#     right(144)
# end_fill()
###############################
#  花型
# from turtle import *
# pencolor("pink")
# for i in range(4):
#     right(90)
#     circle(50,180)
###############################
#  樱花型
from turtle import *
color("pink")
begin_fill()
penup()
goto(100, 100)
pendown()
for i in range(3):
    right(60)
    fd(-40)
    right(120)
    fd(-40)
    left(120)
    circle(-100, -180)
    right(60)
    fd(40)
    right(120)
    fd(40)
    left(120)
    circle(100, 180)
end_fill()
