"""
给定一个非负整数NUM。对于范围0≤i≤num中的每个数字i，计算二进制表示中1的个数并将其作为数组返回。

例如：
对于num = 5您应该返回[0,1,1,2,1,2]。

用运行时O（n * sizeof（integer））来解决这个问题非常容易。
但是，你可以在线性时间O（n） 可能在一个单一的通行证？
空间复杂度应该是O（n）。

"""


def countBits(num):
    """
    :type num: int
    :rtype: List[int]
    """
    add = [0]
    while len (add) <= num:
        add += [i + 1 for i in add]
    return add[:num + 1]


print(countBits(5))



