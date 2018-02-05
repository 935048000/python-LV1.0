#!/usr/bin/env python
# coding=utf-8


'''
堆排序
堆排序使用的是堆这种数据结构
用列表才存储堆
先建立一个最大堆，在建立最大堆的过程中需要不断调整元素的位置。
最大堆建立后，顶端元素必定是最大的元素，把该最大元素与最末尾元素位置置换，最大元素就出现在列表末端。
重复此过程，直到排序。
'''


import random
import time

unsortedList = []

# 产生0-100的无序列表
def generateUnsortedList(num):
    for i in range(0, num):
        unsortedList.append(random.randint(0, 1000000))

generateUnsortedList(10000)


def maxHeapify(L, heap_size, i):
    leftChildIndex = 2 * i + 1
    rightChildIndex = 2 * i + 2
    # print 'leftChildIndex=',leftChildIndex
    # print 'rightChildIndex=',rightChildIndex
    largest = i
    if leftChildIndex < heap_size and L[leftChildIndex] > L[largest]:
        largest = leftChildIndex
    if rightChildIndex < heap_size and L[rightChildIndex] > L[largest]:
        largest = rightChildIndex
    if largest != i:
        L[i], L[largest] = L[largest], L[i]
        maxHeapify(L, heap_size, largest)


def buildMaxHeap(L):
    heap_size = len(L)
    if heap_size > 1:
        start = heap_size / 2 - 1
        # print 'start=',start
    while start >= 0:
        maxHeapify(L, heap_size, start)
        start = start - 1


def heapSort(L):
    heap_size = len(L)
    buildMaxHeap(L)
    i = heap_size - 1
    while i > 0:
        L[0], L[i] = L[i], L[0]
        heap_size = heap_size - 1
        i = i - 1
        maxHeapify(L, heap_size, 0)
    return L

t1=time.time()
print (t1)
print (heapSort (unsortedList))
print ((time.time () - t1), "s")
