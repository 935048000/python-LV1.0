"""

给定一个字符串小号，发现最长的回文子小号。你可以假定s的最大长度是1000。

例：
输入： “babad”
输出： “bab”
注意： “aba”也是一个有效的答案。

例：
输入： “cbbd”
输出： “bb”

当你增加1个字符的时候，你只能增加 maxLen 1或2，而新的maxLen包含这个新的字符。

只需要从头到尾扫描，每次添加一个字符，
跟踪maxLen，并且为每个添加的字符检查以该新字符结尾的子字符串，
长度为P + 1或P + 2是回文，并相应更新。

删除奇数长度字符串的1个字符或奇数/偶数长度字符串的2个字符，
其余字符串仍然是一个回文字符串，Q - 1或Q - 2仍然大于P.
"""


def longestPalindrome(s):
    if len (s) == 0:
        return 0
    maxLen = 1
    start = 0
    
    for i in range (len (s)):
        # print(s[i - maxLen - 1:i + 1],s[i - maxLen - 1:i + 1][::-1])
        imaxlen = i - maxLen
        # print(imaxlen)
        if imaxlen >= 1 and s[imaxlen - 1:i + 1] == s[imaxlen - 1:i + 1][::-1]:
            start = imaxlen - 1
            maxLen += 2
            continue
        
        if imaxlen >= 0 and s[imaxlen:i + 1] == s[imaxlen:i + 1][::-1]:
            start = imaxlen
            maxLen += 1
            
    return s[start:start + maxLen]


print(longestPalindrome("abcbb"))