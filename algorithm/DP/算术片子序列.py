"""
Input: [2, 4, 6, 8, 10]

Output: 7

Explanation:
所有的算术子序列都是:
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10] # 不只是相邻的，固定间隔子序列也算


我们用一组字典dp来记忆，这样dp [i] [j]存储算术片（包括长度为2的算术片）的数量，其常数差是以i结尾的。
关键是要存储所有 2±长度 的算术片（这有助于从其子问题构建解），而仅添加有效的3±长度片。
我们遍历数组中的所有对。
每个（A [j]，A [i]）是我们以前从未遇到的具有常数差异A [i] -A [j]的2长度的片段，
所以增加dp [i] [A [i] A [j]]减1（但是总数保持不变，因为它的长度不超过3）。
如果有任何A [i] - A [j]长度的切片在索引j处结束（如果dp [j]中的A [i] -A [j] :)，
则将它们“扩展”为索引i并添加 总的来说，因为任何终止于索引j的分片现在至少有长度3终止于i。

"""


def numberOfArithmeticSlices(A):
    from collections import defaultdict
    total = 0
    dp = [defaultdict(int) for item in A]
    for i in range(len(A)):
        for j in range(i):
            dp[i][A[i] - A[j]] += 1
            if A[i]-A[j] in dp[j]:
                dp[i][A[i] - A[j]] += dp[j][A[i]-A[j]]
                total += dp[j][A[i]-A[j]]
    return total

def numberOfArithmeticSlices2(A):
    """
    :type A: List[int]
    :rtype: int
    """
    lookup = collections.defaultdict(list)
    for i, a in enumerate(A):
        lookup[a] += i,
    dp = [{} for _ in range(len(A))]

    for k, num in enumerate(A):
        for i in range(0, k):
            diff = A[k] - A[i]
            X = A[i] - diff
            if X in lookup:
                for index in lookup[X]:
                    if index < i:
                        dp[k][diff] = dp[k].get(diff, 0) + 1
                    else: break
            if diff in dp[i]:
                dp[k][diff] = dp[k].get(diff, 0) + dp[i][diff]
    return sum([x[k] for x in dp for k in x])



print(numberOfArithmeticSlices([2,4,6,8,10]))








