# 用列表实现：
name = ['python', 'java', 'c++', 'PHP', 'Hadoop']
ID = ['001', '002', '003', '004', '005']
print(ID[0] + ':' + name[0])
print('{0}:{1}'.format(ID[1], name[1]))

print("------------------------------------------------------------------------")
# 运用字典
KC = {'001': 'python', '002': 'java', '003': 'c++', '004': 'PHP', '005': 'Hadoop'}
# 不可以用列表    d1={[1,2,3]:'001'}
# 但可以用元组    d2={(1,2,3):'001'}
print(KC)
print(type(KC))
print(KC['001'])  # 查找键为001的值
KC['005'] = 'JSP'  # 覆盖005的值
KC['006'] = 'R'  # 增加006的值
print(KC)

print("------------------------------------------------------------------------")
# 创建字典
{}
d1 = dict()
print(d1)
d2 = dict(morty='0023', rick='0024')
print(d2)
KC = {'001': 'python', '002': 'java', '003': 'c++', '004': 'PHP', '005': 'Hadoop'}
print(KC)
print(len(KC))
# 访问字典与增，删，改的操作
del KC['005']  # 删除005的操作
print(KC)
# 视图对象
print(KC.keys())  # 显示所有的键
print(KC.values())  # 显示所有的值
print(KC.items())  # 显示所有的键值对
k_view = KC.keys()
print(type(k_view))
k_list = list(KC.keys())
print(type(k_list))
del KC['004']
print(k_view)  # 视图对象,是动态的
print(k_list)
# print(KC['006'])会报错
print(KC.get('002'))
print(KC.get('006'))  # 不会报错
print(KC.get('006', '没有006课程'))  # 不会报错，返回默认值
print(KC.pop('002'))
# print(KC.pop('006')) 会报错
print(KC.pop('006', '没有006课程'))  # 不会报错，返回默认值
print(KC.popitem())  # 随机删除一个键值对
print(KC.clear())  # 删除所有键值对
del KC  # 删除整个字典
# print(KC)没有KC
print("------------------------------------------------------------------------")
kc = {'001': 'python', '002': 'java', '003': 'c++', '004': 'PHP', '005': 'Hadoop'}
print(dir(dict))
kc.update([('006', 'jsp'), ('007', 'R')])  # 外围表示方法，中括号表示参数
print(kc)
print(id(kc))  # 内存地址
