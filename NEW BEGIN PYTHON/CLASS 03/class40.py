# 1
def add(a, b):
    c = a + b
    return c


# 函数赋值给变量
c = add(3, 4)
print(c)
# 函数返回值作为其他函数的实际参数
print(add(3, 4))


def isGreater0(x):
    if x > 0:
        return True
    else:
        return False


print(isGreater0(5))
print(isGreater0(0))


def add(a, b):
    c = a + b
    return c


# 将函数的值赋值给一个变量c
c = add(4, 4)
print(c)


def sum1(*args):
    def sum2():
        x = 0
        for i in args:
            x = x + i
            print(x)
        return x

    return sum2


sum1(1, 2, 3)
a = sum1(1, 2, 3)
print(a())


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)  # 该方法将元素追加到列表的末尾。append()
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())

listv = [90, 80, 88, 77, 66]


# 分数计算return高分
def score(values):
    return max(values)


m = score(listv)  # 返回值给m
print(m)

listv = [90, 80, 88, 77, 66]


# 分数计算return高分
def score(values):
    return max(values), min(values), sum(values) / len(values)


m = score(listv)  # 返回值给m
print(m)


def m(x, y):
    if x > y:
        return x
    else:
        return y


print(m(2, 12))
print(m(12, 2))


def t(x):
    if x > 0:
        return x
    else:
        return 3


print(t(2))
print(t(-1))
print("---------------------------- ")


def fun():
    print(98)
    return 'ok'  # 执行到该return语句时，函数终止，后边的语句不再执行
    print(98)


def func():
    try:
        print(98)
        return 'ok'  # 函数得到了一个返回值
    finally:  # finally语句块中的语句依然会执行
        print(98)


print(fun())
print('----------')
print(func())
