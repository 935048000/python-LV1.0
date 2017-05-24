#!/usr/bin/env python
# coding=utf-8

'''
合并多个字典或映射
有多个字典或者映射，将它们从逻辑上合并为一个单一的映射后执行某些操作，比如查找值或者检查某些键是否存在。
'''


a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

from collections import  ChainMap
c = ChainMap(a,b)
print(c['x']) # Outputs 1 (from a)
print(c['y']) # Outputs 2 (from b)
print(c['z']) # Outputs 3 (from a)

len(c)
#3
list(c.keys())
#['x', 'y', 'z']
list(c.values())
#[1, 2, 3]

c['z'] = 10
c['w'] = 40
del c['x']
print a
#{'w': 40, 'z': 10}

values = ChainMap()
values['x'] = 1
# Add a new mapping
values = values.new_child()
values['x'] = 2
# Add a new mapping
values = values.new_child()
values['x'] = 3
print values
ChainMap({'x': 3}, {'x': 2}, {'x': 1})
print values['x']
#3

# Discard last mapping
values = values.parents
print values['x']
#2
# Discard last mapping
values = values.parents
print values['x']
#1
print values
#ChainMap({'x': 1})


#使用 update() 方法将两个字典合并
a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }
merged = dict(b)
merged.update(a)
print merged['x']
#1
print merged['y']
#2
print merged['z']
#3

a['x'] = 13
print merged['x']

a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }
merged = ChainMap(a, b)
print merged['x']
#1
a['x'] = 42
merged['x'] # Notice change to merged dicts
#42






