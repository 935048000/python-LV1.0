#!/usr/bin/env python
# coding=utf-8

'''
 映射名称到序列元素
有一段通过下标访问列表或者元组中元素的代码，但是这样有时候会使得你的代
码难以阅读，想通过名称来访问元素。
collections.namedtuple() 函数通过使用一个普通的元组对象来帮你解决这个问题。
'''

from collections import namedtuple
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print sub
Subscriber(addr='jonesy@example.com', joined='2012-10-19')
print sub.addr
print sub.joined
print len(sub)
addr, joined = sub
print  addr
print joined
print

def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total

from collections import namedtuple
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
    total += s.shares * s.price
    return total
s = Stock('ACME', 100, 123.45)
print s
s = s._replace(shares=75)
print s
print

'''
replace() 方法还有一个很有用的特性就是当你的命名元组拥有可选或者缺失字
段时候，它是一个非常方便的填充数据的方法。你可以先创建一个包含缺省值的原型
元组，然后使用 replace() 方法创建新的值被更新过的实例。
'''
from collections import namedtuple
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
# Create a prototype instance
stock_prototype = Stock('', 0, 0.0, None, None)
# Function to convert a dictionary to a Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)
a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
print  dict_to_stock(a)
print  dict_to_stock(b)







