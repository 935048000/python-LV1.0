#!/usr/bin/env python
# coding=utf-8


'''
读写一个 gzip 或 bz2 格式的压缩文件。
gzip 和 bz2 模块可以很容易的处理这些文件。
'''


import gzip
with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()


import bz2
with bz2.open('somefile.bz2', 'rt') as f:
    text = f.read()


import gzip
with gzip.open('somefile.gz', 'wt', compresslevel=5) as f:
f.write(text)

import bz2
with bz2.open('somefile.bz2', 'wt', compresslevel=5) as f:
f.write(text)


import gzip
f = open('somefile.gz', 'rb')
with gzip.open(f, 'rt') as g:
    text = g.read()


















