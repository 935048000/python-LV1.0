"""
如果一个数列由至少三个元素组成，并且任意两个连续元素之间的差异是相同的，则称为算术。
例如，这些是等差数列:
1、3、5、7、9
7、7、7、7
3、1、-5、-9

不是算术。1 1 2 5 7。


"""


def numberOfArithmeticSlices(A):
    curr, sum = 0, 0
    for i in range (2, len (A)):
        if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
            curr += 1
            sum += curr
        else:
            curr = 0
    return sum

print(numberOfArithmeticSlices([1,3,5,7,9]))