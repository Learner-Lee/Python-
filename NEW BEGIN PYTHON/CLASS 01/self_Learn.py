

# python 保留字
import keyword
print(keyword.kwlist)

print("---------------------------------------------------------------------------------")


# 注释

# 这是单行注释

"""
    这是
    多行
    注释
"""

'''
    这也是
    多行
    注释
'''



# 标准数据类型
"""
Python 中有六个标准的数据类型：

Number（数字）
String（字符串）
List（列表）
Tuple（元组）
Set（集合）
Dictionary（字典）
Python3 的六个标准数据类型中：

不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。"""



# 类型判断
# python可以用type函数来检查一个变量的类型

x = "i like python"
print(type(x))
x = 100
print(type(x))
x = ('1','2','3')
print(type(x))
x = ['1','2','3']
print(type(x))

print("---------------------------------------------------------------------------------")




# 字符串

# Python 中单引号和双引号使用完全相同，但单引号和双引号不能匹配。
# 使用三对引号('''或""")可以囊括一个多行字符串。
# 与其他语言相似，python也使用 '\'作为转义字符
# 自然字符串， 通过在字符串前加 r 或 R。 如 r"this is a line with \n" 则\n会显示，并不是换行。
# Python 允许处理 unicode 字符串，加前缀 u 或 U， 如 u"this is an unicode string"。
# 字符串是不可变的。
# 按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
# 字符串可以用 + 运算符连接在一起，用 * 运算符重复。
# Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
# Python中的字符串不能改变（详见上一小点的引用）。
# Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
# 字符串的截取的语法格式如下：变量 [头下标: 尾下标: 步长]


word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以由多行组成"""


str = 'W3Cschool'

print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符,[左闭右开]
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始后的所有字符
print(str[1:5:2])  # 输出从第二个开始到第五个且每隔两个的字符
print(str * 2)  # 输出字符串两次
print(str + '你好')  # 连接字符串

print("---------------------------------------------------------------------------------")

print('hello\nW3Cschool')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nW3Cschool')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
