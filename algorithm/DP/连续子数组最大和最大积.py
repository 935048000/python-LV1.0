#  连续子数组最大和
def continuousSubarraySum(A):
    # e=max{ai,e+ai}
    e = max_so_far = A[0]
    for x in A[1:]:
        e = max(x, e + x)
        max_so_far = max(max_so_far, e)
        # print(x,max_so_far,e)
    return max_so_far


def maxSum(list_of_nums):
    """
    假设数组为a[i]
    因为最大连续的子序列和必须是在位置0-(n-1)之间的某个位置结束。
    那么，当循环遍历到第i个位置时，如果其前面的连续子序列和小于等于0，
    那么以位置i结尾的最大连续子序列和就是第i个位置的值即a[i]。
    如果其前面的连续子序列和大于0，则以位置i结尾的最大连续子序列和为b[i] = max{ b[i-1]+a[i]，a[i]}，
    其中b[i]就是指最大连续子序列的和。
    """
    maxsum = 0
    maxtmp = 0
    for i in range (len (list_of_nums)):
        if maxtmp <= 0:
            maxtmp = list_of_nums[i]
        else:
            maxtmp += list_of_nums[i]
        maxsum = max(maxtmp,maxsum)
    return maxsum

# 乘积最大子序列
def maxProduct(nums):
    lmin = nums[0]
    lmax = lmin
    gmax = lmax
    for i in range(1,len(nums)):
        t1 = nums[i] * lmax
        t2 = nums[i] * lmin
        lmax = max (max (t1, t2), nums[i])
        lmin = min (min (t1, t2), nums[i])
        gmax = max (gmax, lmax)
    return gmax


def maxProduct2(A):
    maxherepre = A[0]
    minherepre = A[0]
    maxsofar = A[0]

    for i in range(1,len(A)):
        maxhere = max (max (maxherepre * A[i], minherepre * A[i]), A[i])
        minhere = min (min (maxherepre * A[i], minherepre * A[i]), A[i])
        maxsofar = max (maxhere, maxsofar)
        maxherepre = maxhere
        minherepre = minhere
    return maxsofar

def maxProduct3(A):
    r = A[0]
    imax = r
    imin = r
    # imax/imin 存储 max/min 乘积
    # 以当前数字A[i]结束的子数组
    for i in range(1,len(A)):
        # 乘以一个负数使大的数变小，小的数更大
        # 所以我们用交换来重新定义极处
        # print(imax,imin)
        if A[i] < 0:
            imax,imin = imin,imax

        # 当前数字的max/min乘积是当前数字本身
        # 或者max/min除以前一个数乘以电流1
        imax = max(A[i], imax * A[i])
        imin = min(A[i], imin * A[i])
        # print (imax, imin)

        # 新计算的max值是我们全局结果的候选项
        # r = max(r, imax)
        print(r)
    return r

# print(maxProduct3([2,3,-2,3]))
# print(maxSum([3,2,3,1,2]))