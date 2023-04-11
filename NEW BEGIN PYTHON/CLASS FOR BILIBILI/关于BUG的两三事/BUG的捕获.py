# 用于解决程序运行时出现的问题

# try中是捕获内容
# 如果出错，执行except
# 如果未出错，执行else
# 无论程序是否出错都会执行finally
# finally主要用于提示，与关闭容器

try:
    a = int(input('请输入一个整数：'))
    b = int(input('请输入一个整数：'))
    result = a / b
except ZeroDivisionError:
    print('分母不能为0', ZeroDivisionError)
except ValueError:
    print('输入必须为整数', ValueError)
except BaseException as e:
    print('未知错误', e)
else:
    print('结果为：', result)
finally:
    print("无论程序是否产生异常都会执行！！")
print('程序结束~')
