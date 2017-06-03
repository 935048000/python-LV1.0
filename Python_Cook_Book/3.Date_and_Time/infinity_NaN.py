#!/usr/bin/env python
# coding=utf-8


'''
无穷大与 NaN
创建或测试正无穷、负无穷或 NaN(非数字) 的浮点数。
'''
import os,sys

a = float('inf')
b = float('-inf')
c = float('nan')

print a
print b
print c
print

# print math.isinf(a)
# print math.isnan(c)

a=float('inf')
print a + 45
print a * 10
print 10 / a

a = float('inf')
print a/a

b = float('-inf')
print a+b


c=float('nan')
print c + 23
print c/2
print c*2

#测试一个 NaN 值得唯一安全的方法就是使用 math.isnan()









