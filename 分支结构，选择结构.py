"""
-单路分支
-双路分支
-多路分支
"""

# -单路分支 (if)
# 奇偶判断
# m = eval(input("m="))
# if m % 2 == 0:
#     print("是偶数")
# print("这个数是", m)
# if m % 2 == 0 and m % 3 == 0:
#     print("yes")
# else:
#     print("no")
print("---------------------------------------------------------------------")

# 成绩合格与否
# m = eval(input("m="))
# n = eval(input("n="))
# if (m >= 60 and n < 60) or (m < 60 and n >= 60) or (m < 60 and n < 60):
#     print("yes")
# else:
#     print("no")
print("---------------------------------------------------------------------")

# 车费问题
# n = eval(input("公里数="))
# if n <= 3:
#     m = 9
# else:
#     m = 8 + (n - 3) * 1.3 + 1
# m = round(m)  # 四舍五入
# print(m)
# print("费用为{}".format(m))
print("---------------------------------------------------------------------")

# 多路分支结构
# 包的型号
# n=input("型号为=")
# if n=="A":
#     a=450
# elif n=="B":
#     a=360
# elif n=="C":
#     a=300
# else:
#     a="error"
# print(a)
print("---------------------------------------------------------------------")

# 闰年
# y = eval(input("年份="))
# if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
#     print("闰年")
# else:
#     print("平年")
print("---------------------------------------------------------------------")

# 练习
x = int(input("x="))
if x < -5:
    y = x + 6
elif x > 5:
    y = 2 * x - 12
else:
    y = x * x + 4 * x + 1
print(y)
print("---------------------------------------------------------------------")
