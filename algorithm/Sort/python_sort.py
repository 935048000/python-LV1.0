#!/usr/bin/env python
# coding=utf-8

'''
Python有自己的列表排序方法，就是sorted函数和sort()函数
sorted函数返回一个有序的序列副本
sort()函数直接在当前列表进行排序，不创建副本，

'''

import random
import time

unsortedList = []

# 产生0-100的无序列表

def generateUnsortedList(num):
    for i in range(0, num):
        unsortedList.append(random.randint(0, 1000000))

generateUnsortedList(10000)

print ()
t1=time.time()
print (sorted (unsortedList))
print ((time.time () - t1), "s")
print ()
print (unsortedList.sort ())
