def first():
    print("我的第一个自定义函数")


first()
print(type(first()))  # 没有返回值为None语句
print(first())
print("----------------------------------------------")


def avgfunc(a, b, c):  # 形式参数
    d = (a + b + c) / 3
    return d


print(avgfunc(10, 20, 30))  # 实际参数
print("----------------------------------------------")


def small(x, y):
    if x < y:
        return x
    else:
        return y


print(small(2, 3))
print(type(small(2, 3)))
print("最小值为{}".format(small(2, 3)))
print(small('a', 'z'))
print(type(small('a', 'z')))
print("----------------------------------------------")


def sumfunc(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s


print(sumfunc(50))
print(sumfunc(100))
print("----------------------------------------------")


def mmfunc(lst):
    max = min = lst[0]
    n = len(lst)
    for i in range(1, n):
        if lst[i] > max:
            max = lst[i]
        if lst[i] < min:
            min = lst[i]
    return max, min


a = [12, 23, 4324, 234, 21, 1]
print(mmfunc(a))
print("----------------------------------------------")


def sumff(x, y):
    s = x ** 2 + y ** 2
    return s


print(sumff(3, 4))
print("----------------------------------------------")


def fact(n):
    f=1
    for i in range (1,n+1):
        f*=i
    return f


print(fact(10))
print(fact(20))
print("----------------------------------------------")

