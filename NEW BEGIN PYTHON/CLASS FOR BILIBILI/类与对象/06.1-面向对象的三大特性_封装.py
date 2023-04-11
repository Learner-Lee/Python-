# coding=utf-8
# 开发者：xxx
# 开发时间： 16:02 
# "Stay hungry，stay foolish."


# 封装的概念
class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print('汽车已启动。。。')


car = Car('五菱宏光')
car.start()
print(car.brand)
print('=' * 60)


# 封装

class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 年龄不希望在类的被外部访问，所以加上两个“_”

    def show(self):
        print(self.name, self.__age)


stu = Student('alen', 20)
stu.show()  # 可以输出
# 在类的外部使用name与age
print(stu.name)
# print(stu.__age)  # 不能使用，报错

# 查询可以使用的方法
print(dir(stu))
print(stu._Student__age)    # 在类的外部可以通过，_Student__age 强行进行访问

