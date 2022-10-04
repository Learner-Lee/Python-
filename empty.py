import turtle
from turtle import *
print(dir(turtle))
setup(800,333)# 画布大小
fillcolor("pink")#填充
begin_fill()#填充开始
penup()#抬笔
pendown()#落笔
pencolor("red")
pensize(24)
fd(78)
seth(60)
circle(90,500)# 半径，角度
end_fill()#填充结束