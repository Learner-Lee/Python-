def gree_user():
    """ 包装 """
    s = " hello python "
    print(s.title())
gree_user()
print("-----------------------------------------------")


def happy():
    print(" happy python")

def happyB(name):
    happy()
    happy()
    print("happy {}!".format(name))
    happy()

happyB("java")
print("-----------------------------------------------")


def add(x,y):
    s = x+y
    print(s)
def sub(x,y):
    s = x-y
    print(s)

add(2,3)
print("-----------------------------------------------")



def greet_user(username):
    """显示简单的问候语"""
    print("Hello, " + username.title() + "!")
greet_user('jesse')


def mathmanu(x,y):

    while (True):
        s = int(input("""
        请输入：
        1.加
        2.减
        3.乘
        4.除
        0.退出
        """))
        if s == 1:
            res = x+y
            print("结果为：",res)
        elif s == 2:
            res = x-y
            print("结果为：",res)
        elif s == 3:
            res = x*y
            print("结果为：",res)
        elif s == 4:
            res = x/y
            print("结果为：",res)
        elif s == 0:
            print("已退出~~")
            break;
        else:
            print("程序错误")

mathmanu(2,3)




