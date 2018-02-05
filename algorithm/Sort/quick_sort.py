#!/usr/bin/env python
# coding=utf-8


'''
快速排序
一种分治思想，基本思想是先随便在无序列表中找一个元素，以这个元素为基准，
其他所有元素都跟该元素比，比该元素小的成为一个子序列，比该元素大的成为另一个子序列，接着重复此过程，
最终达到排序效果。我们也用递归的方式来实现。

'''

from random import *
import random
import time

unsortedList = []

# 产生0-100的无序列表
def generateUnsortedList(num):
    for i in range(0, num):
        unsortedList.append(random.randint(0, 1000000))


# 相对简约
def quickSort(List):
    if len (List) < 2:
        return List
    less=[]
    greater=[]
    middle = List.pop (0)
    
    for item in List:
        if item<middle:
            less.append(item)
        else:
            greater.append(item)

    return quickSort(less)+[middle]+quickSort(greater)


# 普通的
def quickSort2(arr):
    less = []  # 小的列表
    pivotList = []  # 中心列表
    more = []  # 大的列表
    
    if len (arr) <= 1:  # 列表长度不小于等于1
        return "sort list len <= 1\n"  # 小于等于1则报错
    
    else:  # 列表大于一
        pivot = arr[0]  # 原列表第一个值赋值给 中心值
        # pivot = choice (a)  # 从列表随机取一个元素
        for i in arr:  # 把列表循环赋值给i
            if i < pivot:  # i小于中心值
                less.append (i)  # 把i添加进小的列表里
            elif i > pivot:  # i大于中间值
                more.append (i)  # 把i添加进大的列表里
            else:  # i等于中心值
                pivotList.append (i)  # 把i添加进中心列表
        
        less = quickSort2 (less)  # 递归小的列表，排序小的列表里面的顺序
        more = quickSort2 (more)  # 递归大的列表，排序大的列表里面的顺序
        return less + pivotList + more  # 返回三个列表的组合


# 简短的 一行
def qsort(L):
    return (qsort ([y for y in L[1:] if y < L[0]]) +
            L[:1] +
            qsort ([y for y in L[1:] if y >= L[0]])) if len (L) > 1 else L


# 简短的 一行
def qSort(a):
    if len (a) <= 1:
        return a
    else:
        q = choice (a)
        return qSort ([elem for elem in a if elem < q]) + [q] * a.count (q) + qSort ([elem for elem in a if elem > q])


# 简短的 三行
def Qsort(list):
    if not list:
        return []
    else:
        pivot, *list = list
        less = Qsort ([x for x in list if x < pivot])
        more = Qsort ([x for x in list if x >= pivot])
        return less + [pivot] + more


# 可选区间排序
def quicksort(array):
    _quicksort (array, 0, len (array) - 1)
    return array


def _quicksort(array, start, stop):
    if stop - start > 0:
        pivot, left, right = array[start], start, stop
        while left <= right:
            while array[left] < pivot:
                left += 1
            while array[right] > pivot:
                right -= 1
            if left <= right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
        _quicksort (array, start, right)
        _quicksort (array, left, stop)
    return 0


if __name__ == '__main__':
    # generateUnsortedList (10000)
    
    # t1 = time.time ()
    # print (t1)
    # print (quickSort (unsortedList))
    # print ((time.time () - t1), "s")
    #
    a = [99, 4, 65, 2, -31, 0, 99, 83, 782, 1, 99]
    print (a)
    
    # print (quickSort(a))
    print (Qsort (a))
