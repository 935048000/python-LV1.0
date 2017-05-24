#!/usr/bin/env python
# coding=utf-8

'''
字符串匹配和搜索
匹配或者搜索特定模式的文本
只需要调用基本字符串方法就行，比如str.find() , str.endswith() , str.startswith()
复杂的匹配需要使用正则表达式和 re 模块
'''

text = 'yeah, but no, but yeah, but no, but yeah'
# Exact match
print text == 'yeah'

# Match at start or end
print text.startswith('yeah')
print text.endswith('no')

# Search for the location of the first occurrence
print text.find('no')
print


text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
import re
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')
print

datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
else:
    print('no')

if datepat.match(text2):
    print('yes')
else:
    print('no')
print

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
datepat.findall(text)
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')
print m
print m.group(0)
print m.group(1)
print m.group(2)
print m.group(3)
print m.groups()
print

month, day, year = m.groups()
print text
print datepat.findall(text)
print

for month, day, year in datepat.findall(text):
    print('{}-{}-{}'.format(year, month, day))
print

for m in datepat.finditer(text):
    print(m.groups())
print





