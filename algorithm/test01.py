
"""3 number sum"""
def threeSum(nums):
    nums.sort ()
    res = []
    for i in range (len (nums) - 2):
        j = i + 1

        if nums[i] + nums[j] + nums[j + 1] > 0:
            return res
        k = len (nums) - 1 # 因为 i < j < k
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        while j < k: # 如果没有交叉
            if j > i + 1 and nums[j] == nums[j - 1]:
                j += 1
                continue
            total = nums[i] + nums[j] + nums[k]

            # 需要更小的和，向后移动k，记得我们对数组进行排序吗
            if total > 0:
                k -= 1
            else:
                if total == 0:
                    res.append ([nums[i], nums[j], nums[k]])
                j += 1
    return res


# print(threeSum([-1,0,1 ,2 ,-1, -4]))





