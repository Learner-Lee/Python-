from turtle import *
fillcolor("pink")#填充
begin_fill()#填充开始
penup()#抬笔
pendown()#落笔
pencolor("red")
pensize(24)
fd(78)

seth(60)
pencolor("green")
pensize(27)
fd(120)

pencolor("gold")#弧
circle(90,500)# 半径，角度

seth(-100)
pencolor("purple")
pensize(23)
fd(-67)
end_fill()#填充结束
