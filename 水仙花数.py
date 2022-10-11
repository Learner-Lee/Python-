#水仙花数
#x所有数的立方和=x

x=eval(input("三位数"))
a=x//100
b=x//10%10
c=x%10
if(a**3+b**3+c**3==x):
    print("是水仙花数")
else:
    print("不是水仙花数")
