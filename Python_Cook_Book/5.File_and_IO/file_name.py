#!/usr/bin/env python
# coding=utf-8


'''
文件路径名的操作
使用路径名来获取文件名，目录名，绝对路径等等。
使用 os.path 模块中的函数来操作路径名。
'''

import os
path = '/home/ch/Data/data.csv'
print os.path.basename(path)
print os.path.dirname(path)

print os.path.join('tmp', 'data', os.path.basename(path))

path = '~/Data/data.csv'
print os.path.expanduser(path)
print  os.path.splitext(path)


















