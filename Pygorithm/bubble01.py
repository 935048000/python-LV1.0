import pygorithm
from pygorithm.sorting import bubble_sort
"""
这是一个基础算法的库
功能：获取 算法的功能、算法代码、算法时间复杂度

"""
list = [1,2,3,6,4,5,7,0,12,24,5,6,37,43,6,432,65,987,]

s = bubble_sort.sort(list)
print(s)

code = bubble_sort.get_code()
print(code)

time = bubble_sort.time_complexities()
print(time)


