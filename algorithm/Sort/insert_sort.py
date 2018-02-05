#!/usr/bin/env python
# coding=utf-8

'''
插入排序
把序列的第一个元素当成已排序列表中的元素，接着从第二个元素开始，与已排序列表中的元素一一比较，并放到合适的位置。

'''


import random
import time

unsortedList = []

# 产生0-100的无序列表
def generateUnsortedList(num):
    for i in range(0, num):
        unsortedList.append(random.randint(0, 1000000))

generateUnsortedList(10000)

def print_time(arr):
    def _time_cha(arg):
        t1 = time.time()
        ret = arr(arg)
        print ((time.time () - t1), "s")
        print (ret)
        return ret
    return _time_cha


@print_time
def insertionSort(arr):
    list_length=len(arr)
    if list_length<2:
        return arr
    for i in range(1,list_length):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
    return arr

insertionSort(unsortedList)



















