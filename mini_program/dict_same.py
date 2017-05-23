#!/usr/bin/env python
# coding=utf-8

'''
 查找两字典的相同点
在两个字典中寻寻找相同点 (比如相同的键、相同的值等等)
'''

a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}
b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}

# Find keys in common
#a.keys() & b.keys() # { 'x', 'y' }
# Find keys in a that are not in b
#a.keys() - b.keys() # { 'z' }
# Find (key,value) pairs in common
#a.items() & b.items() # { ('y', 2) }

# Make a new dictionary with certain keys removed
#c = {key:a[key] for key in a.keys() - {'z', 'w'}}
# c is {'x': 1, 'y': 2}









