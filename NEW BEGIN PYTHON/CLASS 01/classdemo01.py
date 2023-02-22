# 字符串的替换
"""
str.replace(old,new,count=None)
例如：
"""

a = "i like python , it also like me"

print(a.replace("i","W"))
print(a.replace("i","W",1))

# 字符串分割 split()
# 语法
# string.split(separator, maxsplit)

a = "1 2 3 4 5"
print(a.split())

txt = "welcome to the jungle"
x = txt.split()
print(x)

txt = "hello, my name is Peter, I am 26 years old"
x = txt.split(", ")
print(x)

txt = "apple#banana#cherry#orange"
x = txt.split("#")
print(x)

txt = "apple#banana#cherry#orange"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)
print(x)


# 去除两侧多余的字符
# str.strip(chars=None)
# string.strip(characters)

W = "     strip      "
print(W.strip())

W = "*********strip******"
print(W.strip("*"))

txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(",.grt")
print(x)


# 写入现有文件
# 若要写入现有文件，必须向函数添加一个参数：open()
# "a"- 追加 - 将附加到文件末尾
# "w"- 写入 - 将覆盖任何现有内容

"""
创建新文件
要在 Python 中创建新文件，请使用该方法， 使用以下参数之一：open()

"x"- 创建 - 将创建一个文件，返回 如果文件存在，则为错误

"a"- 追加 - 将创建一个文件，如果 指定的文件不存在

"w"- 写入 - 将创建一个文件，如果 指定的文件不存在
"""



# 打开文件“demofile2.txt”并将内容附加到文件中：

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())


# 打开文件“demofile3.txt”并覆盖内容：

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())