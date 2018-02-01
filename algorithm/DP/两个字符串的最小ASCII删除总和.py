

"""
给定两个字符串s1, s2，查找删除字符的最低ASCII和使两个字符串相等。

输入:s1 = "sea"， s2 = "eat"
输出:231
说明:从"sea"中删除"s"，将"s"(115)的ASCII值加到总和。
从“eat”中删除“t”增加了116的总和。
在最后，两个字符串都是相等的，115 116 = 231是实现这个的最小和。

"""


def minimumDeleteSum(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: int
    """
    l1, l2 = len(s1), len (s2)
    dp = [[0] * (l2 + 1) for _ in range (l1 + 1)]
    for i in range (l1):
        for j in range (l2):
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = dp[i][j] + ord (s1[i])
            else:
                dp[i + 1][j + 1] = max (dp[i][j + 1], dp[i + 1][j])
    result = sum (map (ord, s1 + s2)) - dp[l1][l2] * 2
    return result

print(minimumDeleteSum("sea","eat"))