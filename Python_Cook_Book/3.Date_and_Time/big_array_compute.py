#!/usr/bin/env python
# coding=utf-8


'''
大型数组运算
大数据集 (比如数组或网格) 上面执行计算
涉及到数组的重量级运算操作，可以使用 NumPy 库。
NumPy 是 Python 领域中很多科学与工程库的基础，同时也是被广泛使用的最大最复杂的模块。
导入 NumPy 模块的时候会使用语句 import numpy as np 。
这样的话你就不用再你的程序里面一遍遍的敲入 numpy ，只需要输入 np 就行了，节省了不少时间。
'''


x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
print x * 2
#print x + 10
print x + y
print

import numpy as np
ax = np.array([1, 2, 3, 4])
ay = np.array([5, 6, 7, 8])
print ax * 2
print ax + 10
print ax + ay
print ax * ay

grid = np.zeros(shape=(10000, 10000), dtype=float)
print grid



a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print a
print
# Select row 1
print a[1]
print

# Select column 1
print a[:,1]
print

# Select a subregion and change it
print a[1:3, 1:3]
print

a[1:3, 1:3] += 10
print a
print


# Broadcast a row vector across an operation on all rows
print a + [100, 101, 102, 103]
print

print a
print

# Conditional assignment on an array
print np.where(a < 10, a, 10)
print

