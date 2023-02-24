# Python Math

# Python 有一组内置的数学函数，包括一个广泛的数学模块，允许您对数字执行数学任务。



'''内置数学函数'''

# 函数可用于查找可迭代对象中的最小值或最大值：min()max()

x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

print("-------------------------------")


# 该函数返回指定数字的绝对（正）值：abs()

x = abs(-7.25)

print(x)

print("-------------------------------")


# 该函数将 x 的值返回到 y 的幂 pow(x, y).

# 将 4 的值返回 3 的幂（与 4 * 4 * 4 相同）：

x = pow(4, 3)

print(x)

print("-------------------------------")




"""数学模块"""

# Python 还有一个名为 的内置模块，它扩展了数学函数的列表。math

# 要使用它，您必须导入模块：math

import math

# 导入模块后，您将 可以开始使用模块的方法和常量。math

# 例如，该方法返回一个数字的平方根：math.sqrt()

import math

x = math.sqrt(64)

print(x)

print("-------------------------------")


# 该方法将数字向上舍入为 其最接近的整数，该方法将数字向下舍入到其最接近的整数，并返回结果：math.ceil()math.floor()

import math

x = math.ceil(1.4)  # 向上取整
y = math.floor(1.4)  # 向下取整

print(x) # returns 2
print(y) # returns 1

print("-------------------------------")


# 常量，返回 PI （3.14...）：math.pi

import math

x = math.pi

print(x)

print("-------------------------------")



