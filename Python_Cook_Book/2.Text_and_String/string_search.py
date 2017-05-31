#!/usr/bin/env python
# coding=utf-8

'''
字符串搜索和替换
在字符串中搜索和匹配指定的文本模式
简单的字面模式，直接使用 str.repalce() 方法即可
复杂的模式，请使用 re 模块中的 sub() 函数
'''


text = 'yeah, but no, but yeah, but no, but yeah'
print text.replace('yeah', 'yep')
print

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
import re
print re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
print

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print datepat.sub(r'\3-\1-\2', text)
print


from calendar import month_abbr
def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

print datepat.sub(change_date, text)

newtext, n = datepat.subn(r'\3-\1-\2', text)
print newtext





























