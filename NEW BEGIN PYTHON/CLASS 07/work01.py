from pip._vendor.distlib.compat import raw_input


class Student:
    stuID = ""
    name = ""
    sex = "M"
    classID = "NULL"

    # set ID
    def setStuID(self, stuID):
        self.stuID = stuID

    def setName(self, name):
        self.name = name

    def setSex(self, sex):
        self.sex = sex

    def setClassID(self, classID):
        self.classID = classID

    def getStuId(self):
        return self.stuID

    def getName(self):
        return self.name

    def getSex(self):
        return self.sex

    def getClassID(self):
        return self.classID


import os
import re
import sys
import string
import student

# save file
global FILEPATH
FILEPATH = "student.db"
# temporary file
global TEMPFILE
TEMPFILE = "temp.db"


# This is menu
def menu():
    while True:
        print
        "1.Add a student information"
        print
        "2.Query student information"
        print
        "3.Delete a student information"
        print
        "0.Quit"
        opt = raw_input("Select:")
        if opt == "1":
            while True:
                addStudent()
            opt2 = raw_input("Continue Add(Y/N)?:")
            if opt2 == "Y" or opt2 == "y" or opt2 == "":
                continue
            else:
                break
        elif opt == "2":
            while True:
                query()
            opt2 = raw_input("Continue Query(Y/N)?:")
            if opt2 == "Y" or opt2 == "y" or opt2 == "":
                continue
            else:
                break
        elif opt == "3":
            while True:
                delMenu()
            opt2 = raw_input("Continue Delete(Y/N)?:")
            if opt2 == "Y" or opt2 == "y" or opt2 == "":
                continue
            else:
                break
        elif opt == "0":
            exitProgram()
            break
        else:
            print
            "Error input"


# Add a student
def addStudent():
    stu = student.Student()
    while True:
        stuID = raw_input("ID(001-999):")
        # match ID 001-999
        p = re.match("^[0-9]{3}$", stuID)
        if p:
            if stuID == "000":
                print
                "ID must be 001-999"
                continue
            if isIDExist(stuID):
                print
                "ID = %s already exist!" % stuID
                continue
            else:
                stu.setStuID(stuID)
                break
        else:
            print
            "ID must be 001-999"

    while True:
        stuName = raw_input("Name(a-z,A-Z,5 char):")
        # match name a-z A-Z 5 char
        p = re.match("^[a-zA-Z]{1,5}$", stuName)
        if p:
            stu.setName(stuName)
            break
        else:
            print
            "Name format error must a-z,A-Z,within 5 char"

        while True:
            stuSex = raw_input("Sex(default is M):")
        # default value
        if stuSex == "":
            stu.setSex("M")
            print
            "Sex:M"
            break
        if stuSex == "M" or stuSex == "m":
            stu.setSex(string.upper(stuSex))
            break
            # if stuSex == "M" or stuSex == "m" || stuSex == "F" stuSex == "f":
        p = re.match("^M|m|F|f$", stuSex)
        if p:
            stu.setSex(string.upper(stuSex))
            break
        else:
            print
            "Sex(M/f)"

    while True:
        stuClass = raw_input("Class(01-99):")
        # default value
        if stuClass == "":
            stu.setClassID("NULL")
            print
            "CLASS:NULL"
            break
        # match 00-99
        p = re.match("^[0-9]{2}$", stuClass)
        if p:
            # get rid of 00
            if stuClass == "00":
                print
                "Class must 01-99"
            continue
            stu.setClassID(stuClass)
            break
        else:
            print
            "Class must 01-99"
        # save to file
        file1 = open(FILEPATH, "a")
        print
        "ID\tNAME\tSEX\tCLASS"
        print
        stu.getStuId(), "\t", stu.getName(), "\t", stu.getSex(), "\t", stu.getClassID()
        file1.write(stu.getStuId() + "\t" + stu.getName() + "\t" + stu.getSex() + "\t" + stu.getClassID() + "\n")
        print
        "Add student success!"
        file1.close()


# Delete student menu
def delMenu():
    print("1.Delete by ID")

    print("2.Delete contains ID")

    opt = raw_input("Select:")
    if opt == "1":
        delStudentByID()
    elif opt == "2":
        delStudentContainsID()
    else:
        print
        "Error input"


# Delete contains id
def delStudentContainsID():
    contID = raw_input("ID:")
    if getInfoContainsID(contID) == 0:
        print
        "Can't find ID contains \"%s\" student" % contID
        return
        opt = raw_input("Are you sure delete all(Y/N):")
    if not opt == "y" or opt == "Y":
        return
    f = open(FILEPATH, "r")
    tmp = open(TEMPFILE, "a")
    i = 0
    for eachLine in f:
        items = eachLine.split("\t")
    # if not re.match(contID, items[0]):
    if items[0].count(contID) == 0:
        tmp.write(eachLine)
    else:
        i += 1
    f.close()
    tmp.close()
    os.remove(FILEPATH)
    os.rename(TEMPFILE, FILEPATH)
    print
    "Deleted %d data" % i


# get contains ID information
def getInfoContainsID(stuID):
    f = open(FILEPATH)
    i = 0
    for eachLine in f:
        items = eachLine.split("\t")

    if not items[0].count(stuID) == 0:
        # if re.match(stuID,items[0]):
        i += 1
        if i == 1:
            print
            "ID\tNAME\tSEX\tCLASS"
        print
        eachLine,
    if i == 0:
        return 0
    else:
        return i
    f.close()


# Delete student by ID
def delStudentByID():
    delID = raw_input("Delete ID:")
    if not isIDExist(delID):
        print
        "Can't find ID = %s student information" % delID
    return

    getInfoByID(delID)
    opt = raw_input("Are you sure delete it(Y/N):")
    if not (opt == "Y" or opt == "y"):
        return

    f = open(FILEPATH, "r")
    tmp = open(TEMPFILE, "a")

    for eachLine in f:
        split = eachLine.split("\t")
    if not delID == split[0]:
        tmp.write(eachLine)
    tmp.close()
    f.close()
    os.remove(FILEPATH)
    os.rename(TEMPFILE, FILEPATH)
    print
    "Delete success!"


# Query menu
def query():
    print
    "1.Query student by ID"
    print
    "2.Query all students"
    opt = raw_input("Select:")
    if opt == "1":
        queryByID()
    elif opt == "2":
        queryAll()
    # default is query all
    elif opt == "":
        queryAll()
    else:
        print
        "Error Input!"


# query ID exist
def isIDExist(ID):
    f = open(FILEPATH)
    flag = 0
    for eachline in f:
        temp = eachline.split("\t")
    if temp[0] == ID:
        flag += 1
    f.close()
    if flag == 0:
        return False
    else:
        return True


# get information by ID for delete student
def getInfoByID(stuID):
    f = open(FILEPATH)
    i = 0
    for eachLine in f:
        items = eachLine.split("\t")
    if items[0] == stuID:
        i += 1
        if i == 1:
            print
            "ID\tNAME\tSEX\tCLASS"
        print
        eachLine
    f.close()


# Query student by ID
def queryByID():
    queryID = raw_input("ID:")
    f = open(FILEPATH)
    # lines = f.readlines()
    # print lines[0].strip()
    # for line in lines:
    # a = line.split()
    # if queryID == a[1].strip():
    #  print line.strip()
    flag = 0
    for eachline in f:
        # split by "\t" get as C array temp[4]
        temp = eachline.split("\t")
        # print temp[0] , temp[1] , temp[2] , temp[3]
    if temp[0] == queryID:
        flag += 1
        if flag == 1:
            print
            "ID\tNAME\tSEX\tCLASS"
        print
        eachline,
    if flag == 0:
        print
        "Can't find ID = %s student information" % queryID
    f.close()


# f = open(FILEPATH)
# readLines = f.readlines()

# for eachLine in f:
# eachLine
#
# if eachLine == queryID:
#  print eachLine
# f.close()

# Query all students
def queryAll():
    f = open(FILEPATH, "r")
    i = 0
    for eachLine in f:
        i += 1
    if i == 1:
        print('"ID\tNAME\tSEX\tCLASS"')

    print
    eachLine,
    f.close()
    if i == 0:
        print
        "No data!"


def exitProgram():
    print
    "Thank you Bye!"


# sys.exit()

def init():
    if os.path.exists(FILEPATH):
        print
        "Load file successful"
    else:
        try:
            f = open(FILEPATH, "w")
        except Exception:
            print
            "Can't open file"
            sys.exit()
        finally:
            f.close()


if __name__ == '__main__':
    init()
    menu()
