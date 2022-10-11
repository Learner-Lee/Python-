#函数


abs(x)
#取数组x的绝对值
abs(-78)=78

divmod(x,y)
#有两个结果，并以数值对（）形式输出，
#第一个值为x//y的结果，第二个值为x%y的结果
divmod(14,5) = (2,4)

pow(x,y,[z])
#第三个参数z可以缺省，即：
#pow(x,y)=x**y;pow(x,y,z)=x**y%z.
pow(2,10)=1024
pow(2,10,5)=4
pow(9,0.5)=3.0#(开根号)

round (x,n)
#对x进行四舍五入，保留n位小数位数
round(3.12456,3)=3.125

max(x1,x2,...,xn)
#在一堆同类型数据中取最大值
max(1,2,3,4)=4

min(x1,x2,...,xn)
#在一堆同类型数据中取最小值
min(1,2,3,4)=1
