#!/usr/bin/env python
# coding=utf-8


'''
二八十六进制整数
转换或者输出使用二进制，八进制或十六进制表示的整数。
将整数转换为二进制、八进制或十六进制的文本串，可以分别使用 bin() ,oct() 或 hex() 函数：
'''

a=1234

print bin(a)
print oct(a)
print hex(a)
print

print format(a, 'b')
print format(a, 'o')
print format(a, 'x')
print


b=-1234

print format(b, 'b')
print format(b, 'o')
print format(b, 'x')
print

print format(2**32 + b, 'b')
print format(2**32 + b, 'x')
print

print int('4d2',16)
print int('10011010010',2)









