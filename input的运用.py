# 李祥潜20215080910034
y_school = input("学校:")
y_class = input("班级:")
y_name = input("姓名:")
y_word = input("话:")
print(" i'm from :", y_school, y_class, y_name, "i wannar to tall you :", y_word)
print("//////////////////////////////////////////////////////////////////////////")


# input 写入的都是 str 类型
"""
我们可以使用 Python 内置函数将字符串转换成想要的类型，比如：

- int(string) 将字符串转换成 int 类型；
- float(string) 将字符串转换成 float 类型；
- bool(string) 将字符串转换成 bool 类型。
"""

a = input("Enter a number: ")
b = input("Enter another number: ")
print("更改之前")
print("aType: ", type(a))
print("bType: ", type(b))

a = float(a)
b = int(b)
print("更改之后")
print("aType: ", type(a))
print("bType: ", type(b))

result = a + b
print("resultValue: ", result)
print("resultType: ", type(result))
