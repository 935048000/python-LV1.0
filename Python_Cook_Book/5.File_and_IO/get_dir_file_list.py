#!/usr/bin/env python
# coding=utf-8


'''
获取文件夹中的文件列表
获取文件系统中某个目录下的所有文件列表。
 os.listdir() 函数来获取某个目录中的文件列表
'''

import os
names = os.listdir('/tmp')
print names

names = [name for name in os.listdir('/tmp')
if os.path.isfile(os.path.join('/tmp', name))]
print 'file',names

dirnames = [name for name in os.listdir('/tmp')
if os.path.isdir(os.path.join('/tmp', name))]
print 'dir',dirnames

pyfiles = [name for name in os.listdir('/tmp')
if name.endswith('.py')]
print 'pythons',pyfiles


import glob
pyfiless = glob.glob('/tmp/*.py')
print 'pythonss',pyfiles

from fnmatch import fnmatch
pyfilesss = [name for name in os.listdir('/tmp')
            if fnmatch(name, '*.py')]
print 'pythonsss',pyfiles
print

# 忽略文件名编码
#使用原始文件名执行文件的 I/O 操作，文件名并没有经过系统默认编码去解码或编码过。
import sys
codings = sys.getfilesystemencoding()
print codings
print

with open('jalape\xf1o.txt', 'w') as f:
    f.write('Spicy!')
f.close()

print os.listdir('.')
print os.listdir(b'.')

with open(b'jalapen\xcc\x83o.txt') as f:
    print(f.read())




