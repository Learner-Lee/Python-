# coding=utf-8
# 开发者：xxx
# 开发时间： 9:40 
# "Stay hungry，stay foolish."


# print(dir(object))  # 它返回任何对象的属性和方法列表

class A:
    pass


class B:
    pass


class C(A, B):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class D(A):
    pass


# 创建C类的对象
x = C('jack', 20)  # x是C类型的一个实例对象
print(dir(x))   # 它返回任何对象的属性和方法列表
print(x.__dict__)   # 实例对象的属性字典
print(C.__dict__)
print('------------------')
print(x.__class__)  # <class '__main__.C'> 输出了对象所属的类
print(C.__bases__)  # 查询C的父类
print(C.__base__)   # 类的基类
print(C.__mro__)    # 类的层次结构
print(A.__subclasses__())   # 查询子类

