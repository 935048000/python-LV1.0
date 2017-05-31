#!/usr/bin/env python
# coding=utf-8

'''
字符串对齐
通过某种对齐方式来格式化字符串
使用字符串的 ljust() , rjust() 和 center()方法。
'''


text = 'Hello World'
print text.ljust(20)
print text.rjust(20)
print text.center(20)
print  text.rjust(20,'=')
print  text.center(20,'*')
print

print  format(text, '>20')
print format(text, '<20')
print format(text, '^20')
print

print  format(text, '=>20s')
print  format(text, '*^20s')
print


print  '{:>10s} {:>10s}'.format('Hello', 'World')
print

x = 1.2345
print format(x, '>10')
print  format(x, '^10.2f')
print

print  '%-20s' % text
print  '%20s' % text










