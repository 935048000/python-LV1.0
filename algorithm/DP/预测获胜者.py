

"""


给定一组非负整数的分数。玩家1从数组的任一端选择其中一个数字，然后是玩家2，然后是玩家1，依此类推。
每次玩家选择一个号码，该号码将不可用于下一个玩家。
这继续下去，直到所有的分数被选中。最高分的玩家获胜。
给定一系列的分数，预测玩家1是否是赢家。
你可以假设每个玩家都玩最大化他的分数。
"""


def PredictTheWinner(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    # nums = []

    
    p1 = 0
    p2 = 0
    
    for i in range(len(nums)):
        if i == 0 or i % 2 == 0:
            if len(nums) == 1:
                p1 += nums[0]
                break
            p1 += max(nums[0],nums[-1])
            if max(nums[0],nums[-1]) == nums[0]:
                nums.pop(0)
            else:
                nums.pop(-1)
            
        else:
            p2 += max (nums[0], nums[-1])
            if max (nums[0], nums[-1]) == nums[0]:
                nums.pop (0)
            else:
                nums.pop (-1)
        print (nums,p1,p2)

    if p1 >= p2:
        return True
    else:
        return False


def PredictTheWinner2(nums):
    def check(left, right, memo, depth=0):
        if left > right:
            return 0
        if left == right:
            return nums[left]
        if not (left, right) in memo:
            l, r = - check (left + 1, right, memo, depth + 1) + nums[left], - check (left, right - 1, memo, depth + 1) + nums[right]
            memo[(left, right)] = max(l, r)
        return memo[(left, right)]

    c1 = check (0, len (nums) - 1, {})
    return c1 >= 0


print(PredictTheWinner2([1,5,255,233,7]))


