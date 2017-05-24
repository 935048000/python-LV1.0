#!/usr/bin/env python
# coding=utf-8

'''
字典排序
创建一个字典，并且在迭代或序列化这个字典的时候能够控制元素的顺序。
控制一个字典中元素的顺序，使用 collections 模块中的OrderedDict 类,在迭代操作的时候它会保持元素被插入时的顺序.
'''

from collections import OrderedDict
import json

def ordered_dict():
    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4
    # Outputs "foo 1", "bar 2", "spam 3", "grok 4"
    for key in d:
        print(key, d[key])
    print "d dict : ",d
    print "json dict : ",json.dumps(d)
print ordered_dict()
