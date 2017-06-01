#!/usr/bin/env python
# coding=utf-8


'''
快速排序
一种分治思想，基本思想是先随便在无序列表中找一个元素，以这个元素为基准，
其他所有元素都跟该元素比，比该元素小的成为一个子序列，比该元素大的成为另一个子序列，接着重复此过程，
最终达到排序效果。我们也用递归的方式来实现。

'''


import random
import time

unsortedList = []

# 产生0-100的无序列表
def generateUnsortedList(num):
    for i in range(0, num):
        unsortedList.append(random.randint(0, 1000000))

generateUnsortedList(10000)


def quickSort(unsortedList):
    if len(unsortedList)<2:
        return unsortedList
    less=[]
    greater=[]
    middle=unsortedList.pop(0)
    for item in unsortedList:
        if item<middle:
            less.append(item)
        else:
            greater.append(item)
    return quickSort(less)+[middle]+quickSort(greater)


t1=time.time()
print t1
print quickSort(unsortedList)
print (time.time() - t1),"s"








