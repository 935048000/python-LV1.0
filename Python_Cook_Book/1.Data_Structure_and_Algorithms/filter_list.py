#!/usr/bin/env python
# coding=utf-8

'''
过滤序列元素
有一个数据序列，利用一些规则从中提取出需要的值或者是缩短序列
'''

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print [n for n in mylist if n > 0]
print [n for n in mylist if n < 0]
print

#对内存比较敏感，使用生成器表达式迭代产生过滤的元素。
pos = (n for n in mylist if n > 0)
print pos
print

for x in pos:
    print(x)
print

#处理一些异常或者其他复杂情况。这时候你可以将过滤代码放到一个函数中，然后使用内建的 filter() 函数。
values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
ivals = list(filter(is_int, values))
print(ivals)
print

import math
print [math.sqrt(n) for n in mylist if n > 0]
clip_neg = [n if n > 0 else 0 for n in mylist]
print clip_neg
clip_pos = [n if n < 0 else 0 for n in mylist]
print clip_pos
print


'''
    过滤工具就是 itertools.compress() ，它以一个 iterable
对象和一个相对应的 Boolean 选择器序列作为输入参数。然后输出 iterable 对象中
对应选择器为 True 的元素。当你需要用另外一个相关联的序列来过滤某个序列的时
候，这个函数是非常有用的。
    先创建一个 Boolean 序列，指示哪些元素复合条件。然后
compress() 函数根据这个序列去选择输出对应位置为 True 的元素
'''
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK'
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]

counts = [ 0, 3, 10, 4, 1, 7, 6, 1]

from itertools import compress
more5 = [n > 5 for n in counts]
print more5
print list(compress(addresses, more5))

