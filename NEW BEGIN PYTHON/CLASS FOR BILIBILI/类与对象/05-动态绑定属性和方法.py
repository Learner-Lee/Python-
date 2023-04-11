# coding=utf-8
# 开发者：xxx
# 开发时间： 11:37 
# "Stay hungry，stay foolish."


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + '正在吃饭')


stu1 = Student('tom', 20)
stu2 = Student('jerry', 30)
print(id(stu1))
print(id(stu2))
print('---------------为stu1动态绑定性别属性-----------------')
stu1.gender = 'female'
print(stu1.name, stu1.age, stu1.gender)
print(stu2.name, stu2.age)
print("---------------为stu2动态绑定函数-----------------")
stu1.eat()
stu2.eat()


def show():
    print('定义在类之外的，称为函数')


stu1.show = show
stu1.show()
