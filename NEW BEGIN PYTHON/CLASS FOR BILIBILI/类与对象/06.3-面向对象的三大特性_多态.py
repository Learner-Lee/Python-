# coding=utf-8
# 开发者：xxx
# 开发时间： 18:24 
# "Stay hungry，stay foolish."


class Animal(object):
    def eat(self):
        print('动物会吃')


class Cat(Animal):
    def eat(self):
        print('猫吃鱼')


class Dog(Animal):
    def eat(self):
        print('狗吃肉')


class Person(object):
    def eat(self):
        print('人吃***')


# 定义一个函数
def fun(obj):
    obj.eat()


# 开始调用函数
fun(Cat())
fun(Dog())
fun(Animal())
print('____________________')
fun(Person())
