#!/usr/bin/env python
# coding=utf-8

'''
通过某个关键字排序一个字典列表
一个字典列表，根据某个或某几个字典字段来排序这个列表
使用 operator 模块的 itemgetter 函数，可以非常容易的排序这样的数据结构。
'''
from operator import itemgetter

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]


rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_fname)
print(rows_by_uid)
print

'''
    rows 被传递给接受一个关键字参数的 sorted() 内置函数。这个参数是 callable 类型，
并且从 rows 中接受一个单一元素，然后返回被用来排序的值。itemgetter() 函数就是负责创建这个 callable 对象的。
    operator.itemgetter() 函数有一个被 rows 中的记录用来查找值的索引参数。可
以是一个字典键名称，一个整形值或者任何能够传入一个对象的 getitem () 方法的值。
    传入多个索引参数给 itemgetter() ，它生成的 callable 对象会返回一个包含所有元素值的元组，
并且 sorted() 函数会根据这个元组中元素顺序去排序。
'''
rows_by_lfname = sorted(rows, key=itemgetter('lname','fname'))
print(rows_by_lfname)
print

rows_by_fname = sorted(rows, key=lambda r: r['fname'])
rows_by_lfname = sorted(rows, key=lambda r: (r['lname'],r['fname']))
#使用 itemgetter() 方式会运行的稍微快点。因此，如果你对性能要求比较高的话就使用 itemgetter() 方式

print min(rows, key=itemgetter('uid'))
print max(rows, key=itemgetter('uid'))











