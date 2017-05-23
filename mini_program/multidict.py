#!/usr/bin/env python
# coding=utf-8

'''
 字典中的键映射多个值
使用 collections 模块中的 defaultdict 来构造这样的字典。defaultdict 的一个特征是它会自动初始化每个 key 刚开始对应的值.
'''

from collections import defaultdict

d = {
    'a' : [1, 2, 3],
    'b' : [4, 5]
}

e = {
    'a' : {1, 2, 3},
    'b' : {4, 5}
}

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)

d = {} # A regular dictionary
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)




