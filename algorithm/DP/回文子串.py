"""

给定一个字符串，你的任务是计算这个字符串中有多少回文子串。
具有不同起始索引或结束索引的子字符串即使包含相同的字符也会被计为不同的子字符串。

例1：
输入： “abc”
 输出： 3
 说明：三个回文串：“a”，“b”，“c”。
 
例2：
输入： “aaa”
 输出： 6
 说明：六个回文串：“a”，“a”，“a”，“aa”，“aa”，“aaa”。
 
注意：
输入的字符串长度不会超过1000。
"""




def countSubstrings(S):
    N = len(S)
    ans = 0
    for center in range(2*N - 1):
        left = center / 2
        right = left + center % 2
        while left >= 0 and right < N and S[left] == S[right]:
            ans += 1
            left -= 1
            right += 1
    return ans

def countSubstrings2(s):
    """
    :type s: str
    :rtype: int
    """
    res = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i:j+1] == s[i:j+1][::-1]: # 如果子串等于字串的逆序，则计1次
                res += 1
    return res

print(countSubstrings2("aaa"))