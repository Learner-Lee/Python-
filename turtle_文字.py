from turtle import *
fillcolor("pink")
begin_fill()

pencolor("red")
pensize(12)
fd(200)

seth(90)
pencolor("yellow")
fd(200)

seth(180)
pencolor("blue")
fd(200)

seth(270)
pencolor("purple")
fd(200)

end_fill()

#写字
up()#提笔
goto(50,250)
write("perfect",font=("隶书",20,"normal"))
