#!/usr/bin/env python
# coding=utf-8

'''
用 Shell 通配符匹配字符串
使用 Unix Shell 中常用的通配符 (比如 *.py , Dat[0-9]*.csv 等) 去匹配文本字符串
fnmatch 模块提供了两个函数—— fnmatch() 和 fnmatchcase() ，可以用来实现这样的匹配
'''

from fnmatch import fnmatch, fnmatchcase
print fnmatch('foo.txt', '*.txt')
print fnmatch('foo.txt', '?oo.txt')
print fnmatch('Dat45.csv', 'Dat[0-9]*')
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print [name for name in names if fnmatch(name, 'Dat*.csv')]
print


# On OS X (Mac)
#fnmatch('foo.txt', '*.TXT')
#False
# On Windows
#fnmatch('foo.txt', '*.TXT')
#True

#完全使用你的模式大小写匹配
print fnmatchcase('foo.txt', '*.TXT')
print 

addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]
from fnmatch import fnmatchcase
print [addr for addr in addresses if fnmatchcase(addr, '* ST')]
print [addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')]






















