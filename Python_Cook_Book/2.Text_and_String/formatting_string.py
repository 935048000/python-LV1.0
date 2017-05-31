#!/usr/bin/env python
# coding=utf-8

'''
以指定列宽格式化字符串
使用 textwrap 模块来格式化字符串的输出

'''

import textwrap

s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

print(textwrap.fill(s, 70))
print
print(textwrap.fill(s, 40))
print
print(textwrap.fill(s, 40, initial_indent=' '))
print
print(textwrap.fill(s, 40, subsequent_indent=' '))














