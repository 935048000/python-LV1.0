#!/usr/bin/env python
# coding=utf-8

'''
在正则式中使用 Unicode
使用正则表达式处理文本，但是关注的是 Unicode 字符处理
 re 模块已经对一些 Unicode 字符类有了基本的支持
'''

import re

num = re.compile('\d+')
# ASCII digits
print num.match('123')
# Arabic digits
print num.match('\u0661\u0662\u0663')
print

arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')

pat = re.compile('stra\u00dfe', re.IGNORECASE)
s = 'straße'
print  pat.match(s)
pat.match(s.upper())
print s.upper()








