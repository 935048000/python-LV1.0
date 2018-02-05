#!/usr/bin/env python
# coding=utf-8

'''
冒泡排序
从第一个元素开始，每每相邻的两个元素进行比较，若前者比后者大则交换位置。
最后两个相邻元素比较完成后，最大的元素形成，然后再次从头开始进行比较，
若元素个数为n+1个，则总共需要进行n轮比较就可完成排序.
两个循环，外循环控制轮数，内循环控制每轮的次数。
'''


#冒泡排序交换法，效率低。
import random

import time

def print_time(arr):
    def _time_cha(arg):
        t1 = time.time()
        ret = arr(arg)
        print ((time.time () - t1), "s")
        print (ret)
        return ret
    return _time_cha

unsortedList = []

# 产生0-100的无序列表
def generateUnsortedList(num):
    for i in range(0, num):
        unsortedList.append(random.randint(0, 1000000))
    print (unsortedList)

generateUnsortedList(10000)


# 冒泡排序
@print_time
def bubbleSort_1(arr):
    list_length = len(arr)
    for i in range(0, list_length - 1):
        for j in range(0, list_length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


print (bubbleSort_1 (unsortedList))

'''
选择排序(正宗冒泡排序)，遍历数组，挑选最小的数，排在前边。
    从未排序的序列中找到一个最小的元素，放到第一位，再从剩余未排序的序列中找到最小的元素，放到第二位，
依此类推，直到所有元素都已排序完毕。
    用未排序序列的第一个元素和后续的元素依次相比较，如果后续元素小，
则后续元素和第一个元素交换位置放到，这样一轮后，排在第一位的一定是最小的。这样进行n轮，就可排序。
'''
@print_time
def bubbleSort_2(arr):
    list_length = len(arr)
    for i in range(0, list_length - 1):
        for j in range(i+1, list_length):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


print (bubbleSort_2 (unsortedList))

'''
冒泡排序优化版，排序排到数组无变化后（排序成功后）中断排序，节约资源。
'''
@print_time
def bubbleSort_3(arr):
    list_length = len(arr)
    flag=1
    for i in range(0, list_length - 1):
        if flag == 0:
            break
        flag=0
        for j in range(i+1, list_length):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                flag=1
    return arr


print (bubbleSort_3 (unsortedList))
