#!/usr/bin/env python
# coding=utf-8

'''
字节字符串上的字符串操作


'''

data = b'Hello World'
print data
print data[0]
print data[0:5]
print data.startswith(b'Hello')
print  data.split()
print  data.replace(b'Hello', b'Hello Cruel')
print

data = bytearray(b'Hello World')
print data[0:5]
print data.startswith(b'Hello')
print  data.split()
print  data.replace(b'Hello', b'Hello Cruel')
print


data = b'FOO:BAR,SPAM'
import re
print re.split(b'[:,]', data)




