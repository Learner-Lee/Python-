# coding=utf-8
# 开发者：xxx
# 开发时间： 17:01 
# "Stay hungry，stay foolish."


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


class Teacher(Person):
    def __init__(self, name, age, teachofyear):
        super().__init__(name, age)
        self.teachofyear = teachofyear


stu = Student('alen', 20, '1001')
teacher = Teacher('rick', 34, 10)

stu.info()
teacher.info()
