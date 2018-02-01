"""
对链的最大长度。


给你一n对数字。在每一对中，第一个数字总是小于第二个数字。
现在，我们定义一对(c, d)可以遵循另一对，(a, b)当且仅当b < c。成对的链可以以这种方式形成。
给定一组对，找到可以形成的最长的链。你不需要用完所有给定的对。您可以按任意顺序选择对。
"""

def findLongestChain(pairs):
    cur, res = float('-inf'), 0
    
    for p in sorted(pairs, key=lambda x: x[1]): # 按照对的第二个元素升序
        print(p)
        if cur < p[0]: # 如果当前对的第一个元素大于上一对第二个元素 则 链+1
            cur, res = p[1], res + 1

    return res


print(findLongestChain([[1,2], [3,4], [2,3], [2,4],[5,6]]))