# 李祥潜20215080910034
# i'm king of the Gothem(注释）
"""
此处为多行注释
作者
版本号
"""
print("**************")  # 用于输出一串星号
print("How are you !")
print("*************")

sum = 0
t = 1
while t <= 4:
    sum += t
    t += 1
print(sum)

sum = 0
t = 1
while t <= 4:
    sum += t
    t += 1
    print(sum)
print("//////////////////////////////////////////////////////////////////////////")

flag = 2  # ??

while flag:
    print('Given flag is really true!')

print("Good bye!")
print("//////////////////////////////////////////////////////////////////////////")

count = 0
while count < 9:
    print('The count is:', count)
    count = count + 1
print("Good bye!")
print("//////////////////////////////////////////////////////////////////////////")

count = 0
while count < 5:
    print(count, " is  less than 5")
    count = count + 1
else:
    print(count, " is not less than 5")
print("//////////////////////////////////////////////////////////////////////////")

var = 1
while var == 1:  # 该条件永远为true，循环将无限执行下去
    num = input("Enter a number  :")
    print("You entered: ", num)
print("Good bye!")
print("//////////////////////////////////////////////////////////////////////////")
