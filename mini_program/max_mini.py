#!/usr/bin/env python
# coding=utf-8
"""
 查找最大或最小的 N 个元素
 heapq 模块有两个函数：nlargest() 和 nsmallest() 可以完美解决这个问题。
 强大的heapq模块。
"""

import heapq
import os

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
# 最大的三个数,大到小培训
print(heapq.nlargest(3, nums))
# 最小的三个数，小到大排序
print(heapq.nsmallest(3, nums))

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
# 以price为依据，进行从小到大排序，选出最小的三个
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
# 以price为依据，进行从大到小排序，选出最大的三个
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])

print cheap
print expensive

print max(nums),min(nums)


