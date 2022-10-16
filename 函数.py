# lambda函数
x = lambda a, b: a * b
print(x(3, 4))
print(type(x(3, 4)))

y = lambda i,j,k:i*10+j*5+k
print(y(2,3,5))

ls=[(lambda a:a**2),(lambda a:a**3),(lambda a:a**4)]
print(ls[0](10),ls[1](20),ls[2](30))
print("----------------------------------------------")


def ff(a='bb', b=3):
    s = a * b
    print(s)


ff(3, 4)
print("----------------------------------------------")


def coffee(*n):
    print("我喜欢的咖啡有：")
    for i in n:
        print(i)


coffee('a', 'b', 'c')
print("----------------------------------------------")
