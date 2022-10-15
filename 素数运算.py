x = int(input("请输入你想得到的最大素数："))
for n in range(2, x):
    n
    flag = 1
    for i in range(2, n):
        if n % i == 0:
            flag = 0
    if flag == 1:
        print(n, end=",")
