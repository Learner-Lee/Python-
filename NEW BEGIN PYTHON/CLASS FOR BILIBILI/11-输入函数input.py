# 输入函数 input
present = input('你想要什么礼物？')
print(present,type(present))

# 从键盘输入两个整数
a = input('请输入一个加数：')
print(type(a))
b = input('请输入另一个加数：')
print(type(b))
print(a + b)

# 优化方法一：
a = int(a)
b = int(b)
print(a + b)

# 优化方法二
a = int(input('请输入一个加数：'))
b = int(input('请输入另一个加数：'))
print(a + b)