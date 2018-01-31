"""
给定一个字符串S，你可以通过在它前面添加字符来将它转换为回文。
找到并返回最短的回文，你可以通过执行这个转换找到。

例如：
给定"aacecaaa"，回报"aaacecaaa"。
给定"abcd"，回报"dcbabcd"。

s          dedcba
r[0:]      abcded    Nope...
r[1:]   (a)bcded     Nope...
r[2:]  (ab)cded      Nope...
r[3:] (abc)ded       Yes! Return abc + dedcba

"""

def shortestPalindrome(s):
    r = s[::-1] # r为逆序
    for i in range(len(s) + 1):
        print(r[i:])
        if s.startswith(r[i:]): # 尾部等于前部
            return r[:i] + s  # r[:i]为添加的字符使其变为回文

def shortestPalindrome2(s):
    r = s[::-1]
    for i in range (len (s) + 1):
        if s[:len (s) - i] == r[i:]:
            return r[:i] + s

print("结果：",shortestPalindrome("a"*10000))
print("结果：",shortestPalindrome2("a"*10000))