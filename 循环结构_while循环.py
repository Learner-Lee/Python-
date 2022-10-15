# 被三整除
# i = 1
# while i <= 100:
#     if i % 3 == 0:
#         print(i)
#     i += 1
###########################
#  冰雹猜想
# n=eval(input("请输入一个整数"))
# while n!=1:
#     if n%2==0:
#         n=n/2
#     else:
#         n=n*3+1
#     print(n)
# print("可以论证冰雹猜想")
###########################
#  遍历列表
# s="我爱你中国"
# i=0
# while i<len(s):
#     print("显示进行中：{}".format(s[i]))
#     i+=1
# print("显示结束")
###########################
#  最值问题
# N = eval(input("循环几次"))
# max = eval(input("请输入一个数"))
# i = 0
# while i <= N:
#     a = eval(input("请输入一个数"))
#     if a > max:
#         max = a
#     i += 1
# print(max)
###########################
#  累加问题
a=b=0
i=1
while i<100:
    if i%2==0:
        a+=i
        i+=1
    else:
        b+=i
        i+=1
print(a)
print(b)