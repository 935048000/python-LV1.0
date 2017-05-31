#!/usr/bin/env python
# coding=utf-8

'''
 删除字符串中不需要的字符
去掉文本字符串开头，结尾或者中间不想要的字符，比如空白。
strip() 方法能用于删除开始或结尾的字符。 
lstrip() 和 rstrip() 分别从左和从右执行删除操作。
'''

s = ' hello world \n'
print s.strip()
print  s.lstrip()
print  s.rstrip()
print

t = '-----hello====='
print  t.lstrip('-')
print  t.strip('-=')
print

s = ' hello world \n'
s = s.strip()
print s
print s.replace(' ', '')
print


import re
print re.sub('\s+', ' ', s)

with open(filename) as f:
    lines = (line.strip() for line in f)
    for line in lines:
        print(line)

