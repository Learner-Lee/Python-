from typing import List

a = [1, 2, 4, 4, 5, 2, 11, 6, 7, "hello", True]

b = ["a", "ab", "good", "pi"]

c = a + b
print(c)
d = b * 2
print(d)
print(b in a)  # b是否属于a，bool类型
print(a[4])
print(a[1:4])
print(a[::2])
print(a[::-1])
lst = list("python")
print(lst)

lst2 = list((1, 2, 4, 5))
print(lst2)

e = [1, 2, [3, 4]]
print(e)

print("-------------------------------------------")

# 排序
x = [1, 2, 4, 5, 3, 2, 7, 9]
print(sum(x))
print(max(x))
print(min(x))
print(len(x))

print(sorted(x))  # 排序
print(x)
print(sorted(x, reverse=True))  # 排序逆序
x.sort()  # 永久排序
print(x)

b = ["a", "ab", "good", "pi"]
b.sort(key=len)
print(b)

print("-------------------------------------------------")

# 增加对应列表
print(lst)
lst.append("hello")  # 在末尾加一个数
print(lst)
# lst.append(0,10)#只能加一个参数，不能多个
# print(lst)
lst.append([1, 34])
print(lst)

print(lst2)
lst2.insert(3, "I'm a rickest man")  # 在指定位置增加个数
print(lst2)

f = ['hello', 'Eva']
lst2.extend(f)  # 在末尾追加序列f
print(lst2)

print("-------------------------------------------------")

# 删除对应列表
a = [1, 2, 3, 4, "interesting", 8, 3, 9]
a.pop(1)  # 删除序列号为1的对应元素
print(a)

# print(d.index(8))#用元素名查找序列号

a.remove(3)  # 删除第一次出现的元素3
print(a)

b = [1, 23, 3]
print(b)
b.clear()  # 清空列表
print(b)

del a[1:5]  # 删除1-4的元素
print(a)

print("--------------------------------------------")

a = [1, 2, 3, 3, 3, 3, 3, 3, 5, 64]
b = a.copy()  # 复制a列表到b中
print(b)

print(a.index(2))  # 返回列表元素的序列号
print(a.count(3))  # 列表中3的个数

a[3] = "apple"  # 列表中元素的修改，多增少减
print(a)
a[3:8] = "aa"
print(a)
a[4:5] = "Eva"
print(a)

print("------------------------------------------------")

x = [1, None, True, 2.3, "", []]  # 系统将0，“”，‘’，【】，空元组和None都当成False
print(any(x))  # 任何一个是True就是True
print(all(x))  # 任何一个是False就是False

print("-----------------------------------------------------")

# 元组的特点
# 元组属于不可变的序列，可以当成键

a = ()
print(type(a))
b = (30)  # *******************
print(type(b))
b = (30,)
print(type(b))
c = 1, 2, 3
print(type(c))
(b, e, d) = c  # 将c赋值给b,e,d
print(b)
print(e)
print(d)

a = [1, 2, 3, 4]
print(type(a))  # 列表与元组的相互转换
b = tuple(a)
print(b)
print(type(b))
c = list(b)
print(type(c))
