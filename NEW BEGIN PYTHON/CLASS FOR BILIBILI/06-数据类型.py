""" 整数类型 """
# 可以表示，正数，负数，0
n1 = 90
n2 = -78
n3 = 0
print(n1, type(n1))
print(n2, type(n2))
print(n3, type(n3))

# 整数可以表示为二进制，十进制，八进制，十六进制
print('十进制', 118)
print('二进制', 0b111000100010)  # 二进制以0b开头
print('八进制', 0o176)  # 八进制以0o开头
print('十六进制', 0x1A6F)  # 十六进制以0x开头


print('='*30)


""" 浮点类型 """
a = 3.14159
print(a, type(a))

# 浮点数的计算
n1 = 1.1
n2 = 2.2
n3 = 2.1
print(n1 + n2)
print(n1 + n3)


# 计算优化
from decimal import Decimal
print(Decimal('1.1') + Decimal('2.2'))


print('='*30)


""" bool类型 """
f1 = True
f2 = False
print(f1,type(f1))
print(f2,type(f2))

# bool值可以转换成整数计算
print(f1 + 1)   # 2         1+1的结果为2，所以true表示1
print(f2 + 1)   # 1         0+1的结果为1，所以false表示0


print('='*30)


""" 字符串类型 """
str1 = '人生苦短，我学python'
str2 = "人生苦短，我学python"
str3 = """ 人生苦短，
我学python"""
str4 = '''人生苦短，
我学python'''

print(str1,type(str1))
print(str2,type(str2))
print(str3,type(str3))
print(str4,type(str4))





