#!/usr/bin/env python
# coding=utf-8


'''
 矩阵与线性代数运算
执行矩阵和线性代数运算，比如矩阵乘法、寻找行列式、求解线性方程组等等。
NumPy 库有一个矩阵对象可以用来解决这个问题。
'''


import numpy as np
m = np.matrix([[1,-2,3],[0,4,5],[7,8,-9]])
print m
print
print m.T
print
print m.I
print

v = np.matrix([[2], [3], [4]])
print v
print
print m*v

import numpy.linalg
print numpy.linalg.det(m)
print
print numpy.linalg.eigvals(m)
x = numpy.linalg.solve(m, v)
print
print x
print
print m*x
print
print v



















