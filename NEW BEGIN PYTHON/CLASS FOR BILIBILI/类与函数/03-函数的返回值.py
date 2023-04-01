# bool类型测试
print(bool(0))  # 0的bool值为False
print(bool(8))  # 非0的bool值为True


def fun(num):
    odd = []  # 存奇数
    even = []  # 存偶数
    for i in num:
        if i % 2:
            odd.append(i)
        else:
            even.append(i)
    return odd, even


print(fun([12, 213, 134, 1234, 134, 132, 41234, 134, 87]))

'''
函数的返回值
（1）如果函数没有返回值[函数执行完毕之后，不需要给调用处提供数据] return可以省略不写
（2）函数的返回值，如果是1个，直接返回类型
（3）函数的返回值，如果是多个，返回的结果为元组
'''


def fun1():
    print('hello')


fun1()


def fun2():
    return 'hello'


res = fun2()
print(res,type(res))


def fun3():
    return 'hello', 'world'


print(fun3())
