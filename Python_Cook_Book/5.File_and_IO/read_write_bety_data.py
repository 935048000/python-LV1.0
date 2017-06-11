#!/usr/bin/env python
# coding=utf-8


'''
 读写字节数据
写二进制文件，比如图片，声音文件等等
'''


# Read the entire file as a single byte string
with open('somefile.bin', 'rb') as f:
data = f.read()
# Write binary data to a file
with open('somefile.bin', 'wb') as f:
f.write(b'Hello World')

b = b'Hello World'
print b[0]
#output 72


with open('somefile.bin', 'rb') as f:
    data = f.read(16)
    text = data.decode('utf-8')

with open('somefile.bin', 'wb') as f:
    text = 'Hello World'
    f.write(text.encode('utf-8'))

import array
nums = array.array('i', [1, 2, 3, 4])
with open('data.bin','wb') as f:
    f.write(nums)


import array
a = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0])
with open('data.bin', 'rb') as f:
    f.readinto(a)
print a















