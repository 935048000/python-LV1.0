#coding=utf-8


def quickSort(arr):
    less = [] #小的列表
    pivotList = [] #中心列表
    more = [] #大的列表

    if len (arr) <= 1: #列表长度不小于等于1
        return "sort list len <= 1\n"  #小于等于1则报错

    else: #列表大于一
        pivot = arr[0] #原列表第一个值赋值给 中心值
        for i in arr: #把列表循环赋值给i
            if i < pivot: #i小于中心值
                less.append (i) #把i添加进小的列表里
            elif i > pivot: #i大于中间值
                more.append (i) #把i添加进大的列表里
            else: #i等于中心值
                pivotList.append (i) #把i添加进中心列表

        less = quickSort (less) #递归小的列表，排序小的列表里面的顺序
        more = quickSort (more) #递归大的列表，排序大的列表里面的顺序
        return less + pivotList + more #返回三个列表的组合


def qsort(L):
    return (qsort ([y for y in L[1:] if y < L[0]]) +
            L[:1] +
            qsort ([y for y in L[1:] if y >= L[0]])) if len (L) > 1 else L

def qsort2(list):
    if not list:
        return []
    else:
        pivot = list[0]
        less = [x for x in list     if x <  pivot]
        more = [x for x in list[1:] if x >= pivot]
        return qsort2(less) + [pivot] + qsort2(more)


from random import *


def qSort(a):
    if len (a) <= 1:
        return a
    else:
        q = choice (a)
        return qSort ([elem for elem in a if elem < q]) + [q] * a.count (q) + qSort ([elem for elem in a if elem > q])


def quickSort(a):
    if len (a) <= 1:
        return a
    else:
        less = []
        more = []
        pivot = choice (a)
        for i in a:
            if i < pivot:
                less.append (i)
            if i > pivot:
                more.append (i)
        less = quickSort (less)
        more = quickSort (more)
        return less + [pivot] * a.count (pivot) + more

#python 3
def Qsort(array):
    if len(array) < 2:
        return array
    head,*tail = array
    less = Qsort([i for i in tail if i < head])
    more = Qsort([i for i in tail if i >= head])
    return less + [head] + more

def quicksort(array):
    _quicksort(array, 0, len(array) - 1)
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
        _quicksort(array, start, right)
        _quicksort(array, left, stop)
    return 0


a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
# a = quickSort (a)
#a = qsort(a)
#a = qsort2(a)
#a = qSort(a)
#a = quickSort(a)
#a = Qsort(a)
a = quicksort(a)


print (a)



