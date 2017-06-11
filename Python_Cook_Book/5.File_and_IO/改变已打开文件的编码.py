#!/usr/bin/env python
# coding=utf-8


'''
增加或改变已打开文件的编码
在不关闭一个已打开的文件前提下增加或改变它的 Unicode 编码
给一个以二进制模式打开的文件添加 Unicode 编码/解码方式，可以使用io.TextIOWrapper() 对象包装它。
'''


import urllib.request
import io
u = urllib.request.urlopen('http://www.python.org')
f = io.TextIOWrapper(u, encoding='utf-8')
text = f.read()


#在sys.stdout 上修改编码方式的例子
import sys
print sys.stdout.encoding
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='latin-1')
print sys.stdout.encoding






















