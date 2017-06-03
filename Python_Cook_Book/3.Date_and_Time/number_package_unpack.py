#!/usr/bin/env python
# coding=utf-8


'''
字节到大整数的打包与解包
一个字节字符串并想将它解压成一个整数。
将一个大整数转换为一个字节字符串。
'''
import os

data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'

print len(data)
print int.from_bytes(data,'little')
print int.from_bytes(data, 'big')

x = 94522842520747284487117727783387188
print x.to_bytes(16, 'big')
print x.to_bytes(16, 'little')


import struct

hi, lo = struct.unpack('>QQ', data)
print  (hi << 64) + lo









