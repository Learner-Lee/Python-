# coding=utf-8
# 开发者：xxx
# 开发时间： 11:06 
# "Stay hungry，stay foolish."


class Student:  # Student为类的名称（类名）由一个或多个单词组成，每个单词的首字母大写，其余小写
    native_pace = "中国"  # 直接写在类里的变量，称为类属性

    def __init__(self, name, age):
        self.name = name  # self.name 称为实体属性，进行了一个赋值的操作，将局部变量的name的值赋值给实体属性
        self.age = age

    # 实例方法
    def eat(self):
        print('同学正在吃饭。。。')

    # 静态方法
    @staticmethod
    def method():
        print("我使用了staticmethod进行修饰，所以我是静态方法")

    # 类方法
    @classmethod
    def cm(cls):
        print('我是类方法，因为我使用了classmethod进行修饰')


# 类属性的使用方式
# print(Student.native_pace)
stu1 = Student('tom', 20)
stu2 = Student('jerry', 19)
print(stu1.native_pace)
print(stu2.native_pace)
Student.native_pace = 'China'
print(stu1.native_pace)
print(stu2.native_pace)
print("----------------类方法的使用方式------------------")
Student.cm()
print("----------------静态方法的使用方式------------------")
Student.method()
