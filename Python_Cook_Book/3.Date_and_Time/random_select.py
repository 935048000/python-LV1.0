#!/usr/bin/env python
# coding=utf-8


'''
随机选择
从一个序列中随机抽取若干元素，或者想生成几个随机数
random 模块有大量的函数用来产生随机数和随机选择元素
'''

import random

values = [1, 2, 3, 4, 5, 6]

print  random.choice(values)
print  random.choice(values)
print  random.choice(values)
print  random.choice(values)
print  random.choice(values)
print  random.choice(values)
print

print random.sample(values, 2)
print random.sample(values, 2)
print

print random.sample(values, 3)
print random.sample(values, 3)
print

print values
random.shuffle(values)
print values
print

print random.randint(0, 10)
print random.randint(0, 10)
print random.randint(0, 10)
print random.randint(0, 10)
print

print  random.random()
print  random.random()
print  random.random()
print  random.random()
print

print random.getrandbits(200)




