#!/usr/local/bin/python
# -*- coding:utf-8 -*-

import os
import re

# 定义学生类
from pip._vendor.distlib.compat import raw_input


class Student:
    def __init__(self):
        self.name = ''
        self.ID = ''
        self.score = 0


# 根据学生分数进行从大到小的冒泡排序
def BuddleSortByScore(stulist):
    n = len(stulist)
    for i in range(n):
        for j in range(n - i - 1):
            if stulist[j].score < stulist[j + 1].score:
                # tmp = stulist[j+1]
                # stulist[j+1] = stulist[j]
                # stulist[j] = tmp
                stulist[j], stulist[j + 1] = stulist[j + 1], stulist[j]

            # 按顺序输出所有学生的信息


def PrintAllStudentInfo(stulist):
    print(u"______________________学生列表_______________")

    for i in range(len(stulist)):
        print(u"姓名:"),
        print(stulist[i].name),
        print(
        " "),
        print(
        u"学号:"),
        print(
        stulist[i].ID),
        print(
        " "),
        print(
        u"分数："),
        print(
        stulist[i].score)
    print(
        "____________________________________________")


# 增加一个学生,增加成功返回True，否则返回False
def Add(stulist, stu):
    if searchByID(stulist, stu.ID) == 1:
        print(u"此ID已经存在！")

        return False
    stulist.append(stu)

    # 给出是否保存更新数据的选择
    print("Do you want to save the result ?")

    nChoose = raw_input("Choose:Y/N:")

    if nChoose == 'Y' or nChoose == 'y':
        # 将改变后的结果写入文件中,追加写文件
        file_object = open("students.txt", "a")
        file_object.write(stu.ID)
        file_object.write(" ")
        file_object.write(stu.name)
        file_object.write(" ")
        file_object.write(str(stu.score))
        file_object.write("\r\n")
        file_object.close()
        return True
    else:
        stulist.remove(stu)

    # 根据ID删除一个学生的信息，删除成功则返回True，否则返回false


def DeleteByID(stulist, ID):
    for stu in stulist:
        if stu.ID == ID:
            stulist.remove(stu)

            # 选择是否保存已经改变的内容
            print("Do you want to save the changed result ?")

            nChoose = raw_input("Choose:Y/N:")

            if nChoose == 'Y' or nChoose == 'y':
                file_object = open("students.txt", "w+")
                for stu2 in stulist:
                    file_object.write(stu2.ID)
                    file_object.write(" ")
                    file_object.write(stu2.name)
                    file_object.write(" ")
                    file_object.write(str(stu2.score))
                    file_object.write("\r\n")
                file_object.close()
                print(u"删除成功!")

            return True
    print(u"删除失败!")

    return False


# 根据姓名删除一个学生的信息，删除成功返回True,否则返回False
def DeleteByName(stulist, name):
    pos = searchByName(stulist, name)
    if pos != -1:
        del stulist[pos]

        # 选择是否保存已经改变的内容
        print("Do you want to save the changed result ?")
        nChoose = raw_input("Choose:Y/N:")

        if nChoose == 'Y' or nChoose == 'y':
            file_object = open("students.txt", "w+")
            for stu2 in stulist:
                file_object.write(stu2.ID)
                file_object.write(" ")
                file_object.write(stu2.name)
                file_object.write(" ")
                file_object.write(str(stu2.score))
                file_object.write("\r\n")
            file_object.close()
            print(u"删除成功!")

        return True
    else:
        print(u"删除失败!")

        print(pos)

        return False


# 根据学号查找一个学生是否存在,存在返回学生在列表中的下标，否则返回-1
def searchByID(stulist, ID):
    for i in range(len(stulist)):
        if stulist[i].ID == ID:
            print(u"姓名："),
            print(stulist[i].name),
            print(" "),
            print(u"学号:"),
            print(stulist[i].ID),
            print(" "),
            print(u"分数:"),
            print(stulist[i].score)

            return i
    return -1


# 根据姓名查找一个学生是否存在，存在返回学生在列表中的下标,否则返回-1
def searchByName(stulist, name):
    for i in range(len(stulist)):
        if stulist[i].name == name:
            print(
            u"姓名："),
            print(
            stulist[i].name),
            print(
            " "),
            print(
            u"学号:"),
            print(
            stulist[i].ID),
            print(" "),
            print(u"分数:"),
            print(stulist[i].score)

            return i
    return -1


# 初始化，读取文件，更新学生信息
def Init(stulist):
    print(u"初始化......")


    file_object = open("students.txt", "r", encoding='utf-8').read()

    # 按行读取文件中学生的信息
    for line in file_object:
        stu = Student()
        line = line.strip("\n")
        s = line.split(" ")
        stu.ID = s[0]
        stu.name = s[1]
        stu.score = s[2]
        stulist.append(stu)
    print(u"初始化成功!")



# 查找菜单
def QueryMenu(stulist):
    while True:
        print("******************************")

        print(u"根据学生的学号进行查找-------1")

        print(u"根据学生的姓名进行查找-------2")

        print(u"离开查找模块----------------3")

        print("******************************")


        nChoose = raw_input("请输入你的选择")

        if nChoose == "1":
            ID = raw_input("请输入你要输入查找的ID:")
            searchByID(stulist, ID)
        elif nChoose == "2":
            name = raw_input("请输入你要查找的姓名:")
            searchByName(stulist, name)
        elif nChoose == "3":
            return
        else:
            print(u"选择输入错误，请重新输入!")



# 删除模块
def DeleteMenu(stulist):
    while True:
        print("*****************************")

        print(u"根据学生的学号进行删除------1")

        print(u"根据学生的姓名进行删除------2")

        print(u"离开删除模块---------------3")

        print("******************************")

        nChoose = raw_input("请进行选择:")

        if nChoose == "1":
            ID = raw_input("请输入你要删除的ID:")
            DeleteByID(stulist, ID)
        elif nChoose == "2":
            name = raw_input("请输入你要删除的姓名:")
            DeleteByName(stulist, name)
        elif nChoose == "3":
            return
        else:
            print(u"您的选择有误，请重新输入！")


# 菜单
def menu(stulist):
    while True:
        print("***********************")

        print(u"--------菜单------------")

        print(u"增加学生信息---------1")

        print(u"查找一个学生的信息----2")

        print(
            u"删除一个学生的信息----3")
        print(u"输出所有学生的信息----4")

        print(u"根据分数排序---------5")

        print(u"退出程序-------------6")

        print("------------------------")

        print("************************")

        nChoose = raw_input("请输入你的选择:")

        if nChoose == "1":
            stu = Student()
            stu.name = raw_input("请输入学生的姓名：")

            # 匹配学生ID是否满足0--9中的数字
            while True:
                stu.ID = raw_input("请输入学生的ID:")
                # 创建编译一个正则表达式的模板
                p = re.compile('^[0-9]{3}$')
                if p.match(stu.ID):
                    break
                else:
                    print("学生的ID输入错误，正确形式应该为0--9之间的三位数字!")

            # 匹配学生的分数是否满足0--100之间
            while True:
                stu.score = eval(raw_input("请输入学生的分数："))
                # 利用普通的符号来判断分数是否符合标准
                # if stu.score >= 0 and stu.score <= 100:
                # break
                # 利用正则表达式来判断分数是否符合标准
                if re.match("^[0-9]", str(stu.score)) and stu.score <= 100 and stu.score >= 0:
                    break
                else:
                    print(u"分数不满足实际情况，应该为0--100之间的数字!")

            if Add(stulist, stu) == 1:
                print(u"学生信息增加成功!")

            else:
                print(u"学生信息增加失败!")

        elif nChoose == "2":
            QueryMenu(stulist)
        elif nChoose == "3":
            DeleteMenu(stulist)
        elif nChoose == "4":
            PrintAllStudentInfo(stulist)
        elif nChoose == "5":
            BuddleSortByScore(stulist)

            print("Do you want to save the sorted result?")

            choose = raw_input("please input your choice:Y/N:")
            if choose == 'Y' or choose == 'y':
                file_object = open("students.txt", "w", encoding='utf-8')
                for stu2 in stulist:
                    file_object.write(stu2.ID)
                    file_object.write(" ")
                    file_object.write(stu2.name)
                    file_object.write(" ")
                    file_object.write(str(stu2.score))
                    file_object.write("\r\n")
        elif nChoose == "6":
            return
        else:
            print(u"输入有误，请重新输入！")


# 测试函数部分
if __name__ == '__main__':
    open("students.txt", "w", encoding='utf-8')
    # 定义一个列表用来存储所有学生的信息
    stulist = []

    # 初始化，从文件中读取信息
    Init(stulist)

    # 菜单函数
    menu(stulist)
