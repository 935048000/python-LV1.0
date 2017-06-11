#!/usr/bin/env python
# coding=utf-8


'''
测试文件是否存在
测试一个文件或目录是否存在。
测试一个文件或目录是否存在。
注意权限问题
'''

import os

print os.path.exists('/etc/passwd')
print os.path.exists('/tmp/spam')


print  os.path.isfile('/etc/passwd')
print os.path.isdir('/etc/passwd')
print  os.path.islink('/usr/local/bin/python3')
print os.path.realpath('/usr/local/bin/python3')


print os.path.getsize('/etc/passwd')
print os.path.getmtime('/etc/passwd')

import time
print time.ctime(os.path.getmtime('/etc/passwd'))













