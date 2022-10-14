import math

a = eval(input("a="))
b = eval(input("b="))
c = eval(input("c="))
m = (a + b + c) / 2
s = math.sqrt(m * (m - a) * (m - b) * (m - c))#求平方根
print("面积为{:.2f}".format(s))#结果保留两位
