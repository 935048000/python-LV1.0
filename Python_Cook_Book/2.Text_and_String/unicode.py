#!/usr/bin/env python
# coding=utf-8

'''
 将 Unicode 文本标准化
处理 Unicode 字符串，需要确保所有字符串在底层有相同的表示

'''

import unicodedata

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print s1
print s2
print s1 == s2
print len(s1)
print len(s2)



t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print t1 == t2
print(ascii(t1))
t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)
print t3 == t4

t4 = unicodedata.normalize('NFD', s2)
print t3 == t4
print(ascii(t3))

s = '\ufb01'  # A single character
print s
print  unicodedata.normalize('NFD', s)
print unicodedata.normalize('NFKD', s)
print  unicodedata.normalize('NFKC', s)

t1 = unicodedata.normalize('NFD', s1)
print ''.join(c for c in t1 if not unicodedata.combining(c))



