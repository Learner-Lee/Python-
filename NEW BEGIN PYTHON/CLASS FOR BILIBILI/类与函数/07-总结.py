def fun(a, b, c):  # a,b,c 在函数的定义处，所以是形式参数
    print('a=', a)
    print('b=', b)
    print('c=', c)


# 函数的调用
fun(10, 20, 30)  # 函数调用时的参数传递，称为位置传参
lst = [11, 22, 33]
fun(*lst)  # 在函数调用时，将列表中的每一个元素都转换为位置实参传入
print('=' * 30)
fun(a=100, b=200, c=300)  # 函数的调用，所以对是关键字实参
dic = {'a': 111, 'b': 222, 'c': 333}
fun(**dic)  # 在函数调用时，将字典中的键值对都转换为关键字实参传入


def fun(a, b=10):  # b是在函数的定义处，所以b是形参，而且进行了赋值，所以b称为默认值形参
    print('a=', a)
    print('b=', b)


def fun2(*args):  # 个数可变的位置参数
    print(args)


def fun3(**args):  # 个数可变的关键字参数
    print(args)


fun2(10, 20, 30, 40)
fun3(a=100, b=200, c=300)


def fun4(a, b, *, c, d):  # 从*之后的参数，在函数调用时，只能采用关键字参数传递
    print('a=', a)
    print('b=', b)
    print('c=', c)
    print('d=', d)


# 调用fun4函数
# fun4(10,20,30,40)     # 位置实参传递
fun4(a=10, b=20, c=30, d=40)  # 关键字实参传递
fun4(10, 20, c=30, d=40)  # 前两个参数，采用的是位置实参传递，而c,d采用的是关键字实参传递
''' 需求，c,d只能采用关键字实参传递 '''

''' 函数定义时的参数的顺序问题 '''


def fun5(a, b, *, c, d, **args):
    pass


def fun6(*args, **args2):
    pass


def fun7(a, b=10, *args, **args2):
    pass
