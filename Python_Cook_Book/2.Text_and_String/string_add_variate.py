#!/usr/bin/env python
# coding=utf-8

'''
字符串中插入变量
创建一个内嵌变量的字符串，变量被它的值所表示的字符串替换掉。

'''

import sys
import string

s = '{name} has {n} messages.'
print s.format(name='Guido', n=37)

name = 'Guido'
n = 37
print s.format_map(vars())

class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n

a = Info('Guido',37)
print s.format_map(vars(a))
print  s.format(name='Guido')

class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'
del n
print s.format_map(safesub(vars()))

def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))


name = 'Guido'
n = 37
print(sub('Hello {name}'))
print(sub('You have {n} messages.'))
print(sub('Your favorite color is {color}'))
print '%(name) has %(n) messages.' % vars()
s = string.Template('$name has $n messages.')
print s.substitute(vars())

