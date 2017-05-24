#!/usr/bin/env python
# coding=utf-8

'''
字符串开头或结尾匹配
需要通过指定的文本模式去检查字符串的开头或者结尾
'''


filename = 'spam.txt'
print filename.endswith('.txt')
print filename.startswith('file:')

url = 'http://www.python.org'
print url.startswith('http:')
print


import os
filenames = os.listdir('.')
print filenames
print [name for name in filenames if name.endswith(('.c', '.h')) ]
print any(name.endswith('.py') for name in filenames)
print

from urllib import urlopen
def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()
#read_data()


choices = ['http:', 'ftp:']
url = 'http://www.python.org'
#url.startswith(choices)
print url.startswith(tuple(choices))
print

filename = 'spam.txt'
print filename[-4:] == '.txt'
url = 'http://www.python.org'
print url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp:'
print

import re
url = 'http://www.python.org'
print re.match('http:|https:|ftp:', url)

#检查某个文件夹中是否存在指定的文件类型
if any(name.endswith(('.c', '.h')) for name in listdir(dirname)):
