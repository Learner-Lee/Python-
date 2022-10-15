#单个
# try:
#     a=eval(input("请输入一个数字："))
#     print("数的平方为：",a**2)
# except:
#     print("输入异常")

#多个
# try:
#       <语句块1>
# except  <异常类型1>:
#       <异常处理语句块1>
# ……
# except  <异常类型N>:
#       <异常处理语句块N>
# except：
#       <异常处理语句块N+1>
# else:
#       <语句块>

try:
    a=int(input("请输入一个数字："))
    print("数的平方为：",a**2)
except ValueError:
    print("请输入一个数")
except :
    print("未知错误")