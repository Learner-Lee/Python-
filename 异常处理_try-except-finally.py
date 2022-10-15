# try:     //没有异常，全部执行
#       <语句块1>
# except  <异常类型1>:   //如果有异常不执行else，但执行finally
#      <异常处理语句块2>
# else:
#      <语句块3>
# finally:
#      <语句块4>
try:
    str = '编程中可能会遇到异常'
    i = eval(input("请输入一个整数："))
    print(str[i])
except NameError:
    print('输入错误，请输入一个整数！')
else:
    print('没有发生异常')
finally:
    print("一定要执行语句！")
