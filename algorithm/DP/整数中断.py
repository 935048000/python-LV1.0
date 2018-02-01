
"""
整数中断


给定一个正整数n，将其分解成至少两个正整数的和，并使这些整数的乘积最大化。返回您可以获得的最大产品。
例如，给定n = 2，返回1（2 = 1 + 1）; 给定n = 10，返回36（10 = 3 + 3 + 4）。
n不小于2且不大于58

问题的关键是我们需要把这个数字分解成2s，3s和4s。
首先我们需要知道一个事实，if a,b > 3, |a-b| <= 1, then a*b>=a+b 才能使其获得最大。
所以，if n = a + b, a = a1+a2, b=b1+b2 我们应该打破n a1+a2+b1+b2,
|a1-a2|<1 and |b1-b2|<1 而不是 a + b，因为a1*a2>a, b1*b2>b。
但是，当我们得到一个3 or 时，我们将停止2，所以我们要做的是找到3和2。
你可能已经注意到为什么4出现了。因为如果我们打破了4，我们就得到了2+2，2+2 = 2*2所以我们得到两个2s 的条件也是一样的。
"""

from functools import reduce

def integerBreak(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 2:
        return 1
    if n == 3:
        return 2
    list_3 = [3] * int(n / 3)  # 生成一个3的列表。
    mod_3 = n % 3
    if mod_3 == 1:  # 如果左边是1，那么把它加到第一个元素上，得到4。
        list_3[0] += 1
    if mod_3 == 2:  # 如果剩下一个2，那么把它放到列表中。
        list_3.append (2)
    return reduce (lambda a, b: a * b, list_3)


print(integerBreak(10))







