a = 12
# 在默认情况下，print() 函数输出之后总会换行，
# 这是因为 print() 函数的 end 参数的默认值是“\n”
print(a, end=".")
print(a, end="%")
print()
# 设置end 参数，指定输出之后不再换行
print(40, '\t', end="")
print(50, '\t', end="")
print(60, '\t', end="")
print()
print("//////////////////////////////////////////////////////////////////////////")

user_name = 'Charlie'
user_age = 8
# 同时输出多个变量和字符串
print("读者名：", user_name, "年龄：", user_age)
print("//////////////////////////////////////////////////////////////////////////")

# 指定分隔符
print("读者名：", user_name, "年龄：", user_age, sep='|')  # 改变默认的分隔符，可通过 sep 参数进行设置
print("//////////////////////////////////////////////////////////////////////////")

# 指定 print() 函数的输出目标
f = open("demo.txt", "w")  # 打开文件以便写入
print('沧海月明珠有泪', file=f)
print('蓝田日暖玉生烟', file=f)
print('游戏人生，有生之年', file=f)
f.close()
print("已写完")
print("//////////////////////////////////////////////////////////////////////////")

# 刷新
f = open("demo02.txt", "w")  # 打开文件以便写入
print('沧海月明珠有泪', file=f, flush=True)  # 默认False，不刷新，Ture时刷新
print('蓝田日暖玉生烟', file=f, flush=True)  # 当flush=True时它会立即把内容刷新存到 demo02.txt 中
print('游戏人生，有生之年', file=f, flush=True)
print('Rick永远的神', file=f, flush=True)
f.close()
print("已写完")
print("//////////////////////////////////////////////////////////////////////////")
