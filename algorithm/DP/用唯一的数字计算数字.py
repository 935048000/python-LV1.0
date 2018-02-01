"""
用唯一的数字计算数字

给定一个非负整数n，计算所有数字的唯一数字x，其中0≤x<10 n。

示例：
给定n = 2，返回91.（答案应该是0≤x<100范围内的总数，不包括[11,22,33,44,55,66,77,88,99]）
"""


def countNumbersWithUniqueDigits(n):
    """
    :type n: int
    :rtype: int
    """
    choices = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    ans, product = 1, 1
    
    for i in range (min(n, 10)):
        product *= choices[i]
        ans += product
    
    return ans

print(countNumbersWithUniqueDigits(3))












