#!/usr/bin/env python
# coding=utf-8


'''
使用生成器创建新的迭代模式
实现一个自定义迭代模式，跟普通的内置函数比如 range() , reversed() 不一样。
实现一种新的迭代模式，使用一个生成器函数来定义它。
'''

#生产某个范围内浮点数的生成器
#一个函数中需要有一个 yield 语句即可将其转换为一个生成器。
#生成器只能用于迭代操作。
#一个生成器函数主要特征是它只会回应在迭代中使用到的 next 操作。
# 一旦生成器函数返回退出，迭代终止。

def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment

print list(frange(0, 4, 0.5))
print list(frange(0, 1, 0.125))
print

def countdown(n):
    print('Starting to count from', n)
    while n > 0:
        yield n
        n -= 1
    print('Done!')

c = countdown(3)
print c
print c.next()
print c.next()
print c.next()
print c.next()















