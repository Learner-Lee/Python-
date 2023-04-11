# coding=utf-8
# 开发者：xxx
# 开发时间： 17:39 
# "Stay hungry，stay foolish."


# 方法的继承与重写
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name, self.age)


class Student(Person):
    def __init__(self, name, age, stu_no):
        super().__init__(name, age)
        self.stu_no = stu_no

    def info(self):
        super().info()
        print(self.stu_no)


class Teacher(Person):
    def __init__(self, name, age, teachofyear):
        super().__init__(name, age)
        self.teachofyear = teachofyear

    def info(self):
        super().info()
        print(self.teachofyear)


stu = Student('alen', 20, '1001')
teacher = Teacher('rick', 34, 10)

stu.info()
print("-----------------")
teacher.info()
