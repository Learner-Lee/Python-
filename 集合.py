# set集合
print(dir(set))
# 创建集合
s1 = {1, 2, 4, 4, 3, 4, 2, 5, 3, 4, 5, 3, 4, 5, 6, 2, 4}  # 无序且不重复，所以集合会过滤掉重复的
print(s1)
s2 = {}  # 这是字典
print(type(s2))
print(type(s1))
s3 = set()  # 空集合
a = {12, '45', 12.345, '张三'}
b = set([1, 2, 2, 3])  # set()函数也可以是字符串或元组
print(b)  # 会自动去掉2

print("-----------------------------------------------")
#访问集合，不可以用索引
del a#删除集合
s1.remove(2)#移除，如果没有就报错
print(s1)
s1.discard('ok')#移除，如果没有也不会报错
print(s1.pop())#随即删除
s1.clear()#清除

print("-----------------------------------------------")
#内置方法
s1 = {1, 2, 4, 4, 3, 4, 2, 5, 3, 4, 5, 3, 4, 5, 6, 2, 4}
s1.add(8)
print(s1)
s2={'hell','ok','good',5,6}
s1.update(s2)#加入没有的元素
print(s1)

print("-----------------------------------------------")
#集合中常用运算符
s1={0,1,2,3,4,5,6,7}
s2={2,3,4,5,6,7,8}
a=s1&s2#“&”求交集
print(a)
a2=s1.intersection(s2)#相同
print(a2)
print("---")

b=s1|s2#“|”求并集
print(b)
b2=s1.union(s2)#相同
print(b2)
print("---")

c=s1-s2#“-”求差集
print(c)
c2=s1.difference(s2)#相同
print(c2)
#//////////////////
d=s2-s1
print(d)
d2=s2.difference(s1)#相同
print(d2)
print("---")

e=s1^s2#“^”求对称差集
print(e)
e2=s1.symmetric_difference(s2)#相同
print(e2)

