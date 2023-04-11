# coding=utf-8
# 开发者：xxx
# 开发时间： 22:22 
# "Stay hungry，stay foolish."


class Student:
    # 父类为 object类
    '''
    object类是所有类的父类，因此所有类都有object类的属性和方法
    '''

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 方法重写
    def __str__(self):
        return '我的名字是{}，今年{}岁'.format(self.name, self.age)


stu = Student('alen', 20)
print(dir(stu))  # 内置函数dir()可以查看指定对象所有属性
print(stu)  # 默认调用__str__()方法
"""object有一个__str__()方法，用于返回一个对于“对象的描述”，
对应于内置函数str()经常用于print()方法，帮我们查看对象的信息，
所以我们经常会对__str__()进行重写"""
print(type(stu))
