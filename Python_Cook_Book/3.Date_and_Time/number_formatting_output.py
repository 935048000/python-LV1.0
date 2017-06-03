#!/usr/bin/env python
# coding=utf-8


'''
数字的格式化输出
将数字格式化后输出，并控制数字的位数、对齐、千位分隔符和其他的细节。

'''

a = 1234.56789

print format(a,'0.2f')
print format(a,'<10.1f')
print format(a,'>10.1f')
print format(a,'^10.1f')
print format(a,',')
print format(a,'0,.1f')

print format(a,'e')
print format(a,'0.2E')


print '%0.2f' % a
print '%10.1f' % a
print '%-10.1f' % a








