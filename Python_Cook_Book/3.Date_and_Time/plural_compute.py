#!/usr/bin/env python
# coding=utf-8


'''
复数的数学运算
使用复数来执行一些计算操作
复数可以用使用函数 complex(real, imag) 或者是带有后缀 j 的浮点数来指定。
'''

a = complex(2,4)
b= 3 - 5j
print a
print b
print


print a.real
print a.imag
print a.conjugate()
print

print a+b
print a*b
print a/b
print abs(a)
print


import cmath
print cmath.sin(a)
print cmath.cos(a)
print cmath.exp(a)
print


import numpy as np

a = np.array([2 + 3j, 4 + 5j, 6 - 7j, 8 + 9j])
print a
print a+2
print














