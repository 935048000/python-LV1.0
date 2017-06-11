#!/usr/bin/env python
# coding=utf-8


'''
读取二进制数据到可变缓冲区中
直接读取二进制数据到一个可变缓冲区中，而不需要做任何的中间复制操作。
原地修改数据并将它写回到一个文件中去
读取数据到一个可变数组中，使用文件对象的 readinto() 方法
'''

import os.path

def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf



























