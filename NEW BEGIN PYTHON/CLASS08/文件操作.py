# coding=utf-8
# 开发者：xxx
# 开发时间： 10:25 
# "Stay hungry，stay foolish."

# a 续写 w 覆盖 r 读取
file = open('./filetest.txt', 'a')
file.write('adfasdfasdf\n')
file.close()
file = open('./filetest.txt', 'r')
print(file.read())
file.close()
