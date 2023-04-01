# 函数定义时的 可变的位置参数
def fun(*args):
    print(args)
    # print(args[0])

fun(10)
fun(10,30)
fun(23,234,1,2314)