# 循环N次
for i in range(3):
    print(i, end="    ")
else:
    print()
    print("循环正常结束")
print()
print("-------------------------------------------")

# 遍历文件的每一行
f = open("demofile2.txt", "r")
for line in f.read():
    print(line, end="")
print()
print("-------------------------------------------")

# 遍历字符串s
s = "asdfadfasdffadfasdfasdfadsfasdfhjklasdfa;djf"
for c in s:
    print(c, end="")
print()
print("-------------------------------------------")

# 遍历列表
ls = [1, 2, 4, 5, 6, "asdf"]
for item in ls:
    print(item, end=" ")
print()
print("-------------------------------------------")

# # 打开文件“demofile2.txt”并将内容附加到文件中：
#
# f = open("demofile2.txt", "a")
# f.write("Now the file has more content!")
# f.close()


f = open("demofile.txt", "w")
test = "如果不向太阳索取微笑，温暖仍在太阳那里，但我们会笑得更加自信从容；如果转过身去发现了自己的影子，适当的躲让，阳光便可穿越心灵，温暖每一处身后的角落；如果摊开的掌心不能点落蝴蝶，那就紧握成拳挥动臂膀，给予力量；如果我不能够微笑得灿烂，那就将脸投向灿烂的阳光，与阳光一起微笑，烂漫。"
f.write(test)
f.close()

f = open("demofile.txt", "r")
n = "阳"
a = 0
for de in f.read():
    if de == n:
        a += 1
    print(de, end="")
else:
    print()
    print(a)
    print("程序结束")
print()
print("-------------------------------------------")

f = open("abc.txt", "w")
f.write("""
The sun, not only from the sun, 
but also from our hearts. Have a heart of the sun, 
can see the bright side of the world; there is sunshine in the heart, 
with the wrong people heart to heart; the heart of sunshine, even in a sad day, 
will retain the warmth andenthusiasm; the heart of sunshine, can improve the quality of life. Self-confidence, 
tolerance, give, love, gratitude, let the heart of the sun, illuminate the little drops of life, the heart of the sun, 
the sun makes the fate.
""")
f.close()

import collections

# import os
with open('abc.txt') as file1:  # 打开文本文件
    str1 = file1.read().split(' ')  # 将文章按照空格划分开
print("原文本:\n %s" % str1)
print("\n各单词出现的次数:\n %s \n" % collections.Counter(str1))
print(collections.Counter(str1)['the'])  # 以字典的形式存储
print()
print("-------------------------------------------")



s, idx = "BIT", 0
while idx < len(s):
    print("循环进行中: " + s[idx])
    idx += 1
else:
    s = "循环正常结束"
print(s)
print()
print("-------------------------------------------")



for s in "BIT":
    for i in range(10):
        print(s, end="")
        if s=="I":
            break
print()
print("-------------------------------------------")



for s in "PYTHON":
    if s=="T":
        continue
    print(s, end="")
else:
    print("正常退出")
print()

for s in "PYTHON":
    if s=="T":
        break
    print(s, end="")
else:
    print("正常退出")

print()
print("-------------------------------------------")








# random.random()
# 功能：随即返回 0~1 之间的随机浮点数(使用非常的简单，看下方的演示demo)

import random
print('第一次', random.random())
print('第二次', random.random())
print('第三次', random.random())


# random.randint()
# 功能：产生一个 区间 的随机整数(演示 demo 如下：)

import random
print('第一次', random.randint(1, 10))
print('第二次', random.randint(1, 10))
print('第三次', random.randint(1, 10))



# random.randrange()
# 功能：获取区间内的一个随机数(演示 demo 如下：)
# 注意：randrange()函数的参数与range()相同，其功能相当于choice(range(start, stop, step))，但并不实际产生range对象，该函数返回值类型是int。
# 举例：从给定的范围中选择一个伪随机整数。它可以用一个、两个或三个参数，来确定一个范围，就像range函数一样。例如，randrange(1, 6)从范围[1,2,3,4,5]中返回某个数字，而randrangre(5,105,5)返回5~100之间的5的倍数（包括5和100，但不包括105。）

import random
print(random.randrange(0, 100, 3))
print(random.randrange(5, 55, 5))
print(random.choice(range(6, 48, 3)))

print()
print("-------------------------------------------")



import random
gifts = ['谢谢参与', '华为手环', 'iphone13', '小米电视', 'Mac Pro']
def chioce_gift():
    count = random.randrange(0, 100, 1)
    if 0 <= count <= 50:
        print(gifts[0])
    elif 50 < count <= 75:
        print('中奖了！你获得了：', gifts[1])
    elif 75 < count <= 90:
        print('中奖了！你获得了：', gifts[2])
    elif 90 < count <= 98:
        print('中奖了！你获得了：', gifts[3])
    else:
        print('中奖了！你获得了：', gifts[4])


if __name__ == '__main__':  #
    chioce_gift()
print()
print("-------------------------------------------")




# 双色球小案例
import random
def Lotto():
    red = []
    for red_temp in random.sample(range(1, 34), 6):
        red.append(str(red_temp))
    blue = str(random.randint(1, 17))
    return ' '.join(red) + '  ' + blue


if __name__ == '__main__':
    print('双色球的中奖号码为：', Lotto())



