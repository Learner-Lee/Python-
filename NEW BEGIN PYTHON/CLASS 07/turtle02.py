# #coding=utf-8
# import turtle
# import time
# # 同时设置pencolor=color1, fillcolor=color2
# turtle.color("red", "yellow")
# turtle.begin_fill()
# for _ in range(50):
#     turtle.forward(200)
#     turtle.left(170)
#     turtle.end_fill()
# # turtle.mainloop()
# turtle.end_fill()
# turtle.done()


# !/usr/bin/env python
import turtle

aj = turtle.Pen()
y = 0
aj.speed(11)
# turtle.screensize(200,800)
turtle.bgcolor("black")


# aj.shape("turtle")
def head():
    aj.color("green")
    aj.fd(160)
    x = aj.xcor()
    aj.seth(90)
    aj.begin_fill()
    # aj.color("green")
    aj.circle(x / 2, 180)
    aj.end_fill()
    aj.penup()
    aj.goto(33, 37)
    aj.pendown()
    aj.dot(13, "black")
    aj.penup()
    aj.goto(126, 37)
    aj.pendown()
    aj.dot(13, "black")
    aj.penup()
    aj.home()
    aj.pendown()
    aj.hideturtle()
    aj.fd(160)
    aj.seth(90)
    aj.circle(x / 2, 60)
    aj.right(90)
    aj.pensize(5)
    aj.fd(30)

    aj.penup()
    aj.home()
    # aj.pendown()
    aj.hideturtle()
    aj.fd(160)
    aj.seth(90)
    aj.circle(x / 2, 120)
    aj.right(90)
    aj.pensize(5)
    aj.pendown()
    aj.fd(30)
    aj.penup()
    aj.home()
    aj.penup()


def body():
    aj.pensize(0)

    aj.home()
    aj.showturtle()
    aj.goto(0, -7)
    aj.pendown()
    aj.begin_fill()
    aj.fd(160)
    aj.right(90)
    aj.fd(120)
    aj.right(90)
    aj.fd(160)
    y = aj.ycor()
    aj.right(90)
    aj.fd(120)
    aj.end_fill()


def legs():
    aj.penup()
    # turtle.color("red")
    aj.goto(33, -169)
    aj.pendown()
    aj.pensize(32)
    aj.fd(43)
    aj.penup()
    aj.goto(130, -169)
    aj.pendown()
    aj.fd(43)
    aj.penup()


def hands():
    aj.home()
    aj.pensize(30)
    aj.goto(-18, -77)
    aj.pendown()
    aj.left(90)
    aj.fd(65)
    aj.penup()
    aj.goto(179, -77)
    aj.pendown()
    aj.fd(65)
    aj.penup()
    # aj.hideturtle
    aj.fd(100)
    aj.hideturtle()
    aj.circle(100)
    aj.circle(100, 360, 59)
    # aj.reset()
    # turtle.bgcolor("black")
    # turtle.pencolor("green")
    # turtle.hideturtle()
    # turtle.goto(-300, 0)
    # aj.hideturtle
    # turtle.write("Thank you for watching....", font=("Bodoni MT Black", 28, "bold"))
    # turtle.penup()
    # turtle.goto(-40, -170)
    # turtle.pendown()
    # turtle.pencolor("yellow")
    # turtle.write("Developed by 一个超会写Bug的安太狼", font=("Palatino Linotype", 22, "bold"))


head()
body()
legs()
hands()
turtle.done()
