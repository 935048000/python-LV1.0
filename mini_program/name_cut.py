#!/usr/bin/env python
# coding=utf-8

'''
命名切片
程序已经出现一大堆已无法直视的硬编码切片下标，清理下代码。
'''

###### 0123456789012345678901234567890123456789012345678901234567890'
record = '....................100 .......513.25 ..........'
cost = int(record[20:23]) * float(record[31:37])
print cost

SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost = int(record[SHARES]) * float(record[PRICE])
print cost
print

items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print items[2:4]
print items[a]
items[a] = [10, 11]
print items
del items[a]
print items
print

a = slice(5, 50, 2)
print a.start
print a.stop
print a.step
print

s = 'HelloWorld'
print a.indices(len(s))
for i in range(*a.indices(len(s))):
    print(s[i])

