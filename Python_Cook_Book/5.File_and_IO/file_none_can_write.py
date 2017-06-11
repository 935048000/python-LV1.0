#!/usr/bin/env python
# coding=utf-8


'''
文件不存在才能写入
一个文件中写入数据，但是前提必须是这个文件在文件系统上不存在。
不允许覆盖已存在的文件内容。
'''

with open('somefile', 'wt') as f:
    f.write('Hello\n')

#mode: x --> w

with open('somefile', 'xt') as f:
    f.write('Hello\n')



























