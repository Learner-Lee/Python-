# R = int(input("请输入圆半径:"))
# S = 3.1415 * R * R
# L = 2 * 3.1415 * R
# print("面积和周长:",S,L)
# print(f'面积{S}周长{L}')
# print('面积{}周长{}'.format(S,L))


# R = int(input("请输入正整数:"))
# i, S = 0, 0
# while (i<=R):
#     S = S + i
#     i = i + 1
# print("累加求和",S)



# PM = eval(input("请输入PM2.5数值: "))
# if PM >= 75:
#    print("空气存在污染，请小心！")
# else:
#    print("空气没有污染，可以开展户外运动!")



# PM = int(input("请输入PM2.5数值: "))
# print("空气{}污染!".format("存在" if PM >= 75 else "没有"))



# PM = int(input("请输入PM2.5数值: "))
# if 0<= PM < 35:
#     print("空气优质，快去户外运动!")
# elif 35 <= PM <75:
#     print("空气良好，适度户外活动！")
# elif 75 <= PM:
#     print("空气污染，请小心！")
# else:
#     print("请自己挖坑")



x = input(" input two nummbers:")
a,b = map(int,x.split())
if a>b:
    a,b = b,a
print(a,b)









