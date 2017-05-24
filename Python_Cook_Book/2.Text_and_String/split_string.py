#!/usr/bin/env python
# coding=utf-8

'''
使用多个界定符分割字符串
将一个字符串分割为多个字段，但是分隔符 (还有周围的空格) 并不是固定
的。
'''

# re.split() 是非常实用的，因为它允许你为分隔符指定多个正则模式。
line = 'asdf fjdk; afed, fjek,asdf, foo'
import re
print re.split(r'[;,\s]\s*', line)
print

fields = re.split(r'(;|,|\s)\s*', line)
print fields
print


values = fields[::2]
delimiters = fields[1::2] + ['']
print values
#['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
print delimiters
#[' ', ';', ',', ',', ',', '']
print

# Reform the line using the same delimiters
print zip(values,delimiters)
print ''.join(v+d for v,d in zip(values, delimiters))
#'asdf fjdk;afed,fjek,asdf,foo'
print

print  re.split(r'(?:,|;|\s)\s*', line)















