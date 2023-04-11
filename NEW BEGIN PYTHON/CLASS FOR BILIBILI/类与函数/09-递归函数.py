def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n - 1)


print(fac(6))


# 实例：斐波那契数列
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# 斐波那契数列第六位上的数字
print(fib(6))
print("=" * 60)
# 输出这个数列的前六位上的数
for i in range(1, 7):
    print(fib(i))
