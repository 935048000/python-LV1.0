#!/usr/bin/env python
# coding=utf-8


'''
打印不合法的文件名
取了一个目录中的文件名列表，但是当它试着去打印文件名的时候程序崩溃，出现了 UnicodeEncodeError 异常和一条奇怪的消息
'''

def bad_filename(filename):
    return repr(filename)[1:-1]

try:
        print(filename)
except UnicodeEncodeError:
        print(bad_filename(filename))



























