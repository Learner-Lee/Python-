# 随机数
from random import *

print(random())  # 随机小数
seed(5)  # 种子
print(random())
print(random())
seed()  # 系统时间作为种子
print(random())
print("////////////////////////")
for i in range(4):
    print(randint(2, 10))  # a,b之间的随机整数
print("////////////////////////")
for i in range(10):
    print(randrange(1, 10, 2), end="   ")  # 随机奇数
print()
print("////////////////////////")
print(uniform(2, 5))  # a,b之间的随机小数
print("////////////////////////")
s = "peizheng"
print(choice(s))
print("////////////////////////")
s1 = list(s)
print(s1)
print(shuffle(s1))
print(shuffle(s1))
