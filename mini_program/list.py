#!/usr/bin/env python
# coding=utf-8

'''
删除序列相同元素并保持顺序
在一个序列上面保持元素顺序的同时消除重复的值
'''

def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10]
print "a=",a
print "order hash:",list(dedupe(a))
print "no order hash:",set(a)


def dedupe2(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
print "a=",a
print "order no hash:",list(dedupe2(a, key=lambda d: (d['x'], d['y'])))

print "order no hash delete  x same :",list(dedupe2(a, key=lambda d: d['x']))










