"""
给定一个字符串s，找出s中最长的回文序列的长度。你可以假定s的最大长度是1000。

示例1：
输入：
“bbbab”
输出：
4
一个可能的最长的回文序列是“bbbb”。

思想:
dp[i][j] = s[i to j]最长的palindrome子序列。
如果 s[i] == s[j], dp[i][j] = 2 + dp[i+1][j - 1]
则 dp[i][j] = max(dp[i+1][j], dp[i][j-1])
"""


def longestPalindromeSubseq(s):
    """
    :type s: str
    :rtype: int
    """
    n = len (s)
    dp = [1] * n
    for j in range (1, len (s)):
        pre = dp[j]
        for i in reversed (range (0, j)):
            print(i,dp)
            tmp = dp[i]
            if s[i] == s[j]:
                dp[i] = 2 + pre if i + 1 <= j - 1 else 2
            else:
                dp[i] = max (dp[i + 1], dp[i])
            pre = tmp
    return dp[0]

def longestPalindromeSubseq2(s):
    if s == s[::-1]:
        return len (s)

    n = len (s)
    dp = [0 for j in xrange (n)]
    dp[n - 1] = 1

    for i in xrange (n - 1, -1, -1):  # 实际上可以从n-2开始…
        newdp = dp[:]
        newdp[i] = 1
        for j in xrange (i + 1, n):
            if s[i] == s[j]:
                newdp[j] = 2 + dp[j - 1]
            else:
                newdp[j] = max (dp[j], newdp[j - 1])
        dp = newdp

    return dp[n - 1]

print(longestPalindromeSubseq("bbbab"))



