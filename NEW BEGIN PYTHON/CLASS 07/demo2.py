import turtle as t
t.screensize(800,600,"green")
t.pencolor("pink")
t.pensize(20)
for i in range(4):
    # t.stamp() # 画出小乌龟
    t.forward(50)
    t.penup()
    t.forward(50)
    t.pendown()
    t.forward(50)
    t.left(90)

t.done()