#!/usr/bin/env python
# coding=utf-8

'''
字符串忽略大小写的搜索替换
以忽略大小写的方式搜索与替换文本字符串

'''

import re

text = 'UPPER PYTHON, lower python, Mixed Python'
print re.findall('python', text, flags=re.IGNORECASE)
print re.sub('python', 'snake', text, flags=re.IGNORECASE)
print


def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace

print  re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)







