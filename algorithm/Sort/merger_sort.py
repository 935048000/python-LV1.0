#!/usr/bin/env python
# coding=utf-8


'''
归并排序
一种典型的分治思想，把一个无序列表一分为二，对每个子序列再一分为二，继续下去，直到无法再进行划分为止。
然后，就开始合并的过程，对每个子序列和另外一个子序列的元素进行比较，依次把小元素放入结果序列中进行合并，最终完成归并排序。

'''


import random
import time

unsortedList = []

# 产生0-100的无序列表
def generateUnsortedList(num):
    for i in range(0, num):
        unsortedList.append(random.randint(0, 1000000))

generateUnsortedList(10000)

def mergeSort(unsortedList):
    if len(unsortedList)<2:
        return unsortedList
    sortedList=[]
    left=mergeSort(unsortedList[:len(unsortedList)/2])
    right=mergeSort(unsortedList[len(unsortedList)/2:])
    while len(left)>0 and len(right)>0:
        if left[0]<right[0]:
            sortedList.append(left.pop(0))
        else:
            sortedList.append(right.pop(0))
    if len(left)>0:
        sortedList.extend(mergeSort(left))
    else:
        sortedList.extend(mergeSort(right))
    return sortedList

t1=time.time()
print t1
print mergeSort(unsortedList)
print (time.time() - t1),"s"



