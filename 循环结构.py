# for循环
for c in "python":
    print(c, end="")
print()
print("-----------------------------------------------------------")

# 和
s = 0
for i in range(1, 101, 2):
    s += i
print(s)
print("-----------------------------------------------------------")

# 阶乘
# N = eval(input("数为="))
# f = 1
# for i in range(1, N + 1):
#     f *= i
# print(f)
print("-----------------------------------------------------------")

# 三位数内的水仙花数
for i in range(100, 1000):
    a = i // 100
    b = i // 10 % 10
    c = i % 10
    if a ** 3 + b ** 3 + c ** 3 == i:
        print(i)
