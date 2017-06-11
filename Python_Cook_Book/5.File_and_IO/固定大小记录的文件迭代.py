#!/usr/bin/env python
# coding=utf-8


'''
固定大小记录的文件迭代
在一个固定长度记录或者数据块的集合上迭代，而不是在一个文件中一行一行的迭代。

iter() 函数有一个鲜为人知的特性就是，如果你给它传递一个可调用对象和一个
标记值，它会创建一个迭代器。这个迭代器会一直调用传入的可调用对象直到它返回
标记值为止，这时候迭代终止。
'''

# records 对象是一个可迭代对象
from functools import partial
RECORD_SIZE = 32
with open('somefile.data', 'rb') as f:
    records = iter(partial(f.read, RECORD_SIZE), b'')
    for r in records:


























