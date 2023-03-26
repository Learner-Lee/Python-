# print(" i like python",end=",")


# # 打开文件“demofile2.txt”并将内容附加到文件中：
#
# f = open("demofile2.txt", "a")
# f.write("Now the file has more content!")
# f.close()
#
# #open and read the file after the appending:
# f = open("demofile2.txt", "r")
# print(f.read())
# print()





f = open("demofile2.txt", "r")
a = 0
for s in f.read():
    print(s,end="")
    a += 1
else:
    print()
    print(a)
    print("遍历结束")



import numpy as np

x = np.empty([0,3],dtype=str)


f = open("demofile2.txt", "r")
str1 = "N"
a = 0
for s in f.read():
    if s == str1:
        for i in range(3):
            print()
    print(s,end="")
    a += 1
else:
    print()
    print(a)
    print("遍历结束")

