import turtle as t
t.screensize(800,600,"green")
t.pencolor("pink")
t.pensize(20)
# t.speed(10.5)
t.fd(100)
t.circle(90,900)
for i in range(5):
    t.stamp() # 画出小乌龟
    t.forward(100)
    t.left(50)

t.fillcolor('yellow')
t.begin_fill()
t.penup()
t.goto(-200,-200)
t.pendown()
t.circle(50)
t.end_fill()

t.hideturtle()

t.done()