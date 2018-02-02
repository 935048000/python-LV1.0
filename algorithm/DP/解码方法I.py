
def numDecodings(s):
    # dp[i] = dp[i-1] if s[i] != "0"
    #       +dp[i-2] if "09" < s[i-1:i+1] < "27"
    if s == "": return 0
    dp = [0 for x in range(len (s) + 1)]
    dp[0] = 1
    for i in range (1, len (s) + 1):
        if s[i - 1] != "0":
            dp[i] += dp[i - 1]
        if i != 1 and s[i - 2:i] < "27" and s[i - 2:i] > "09":  # "01"ways = 0
            dp[i] += dp[i - 2]
    return dp[len (s)]


def numDecodings2(s):
    '''
    在这里，我们尝试计算每个i的dp[i]，它是字符串s[i:len(s)]可以解码的方式的数目。
    '''
    if not s:   return 0
    i, n = len (s) - 1, len (s)
    prev, prevPrev = 1, 1
    while i >= 0:
        char = s[i]
        # 如果当前字符是3 - 9，那么dp[i] = dp[i + 1]，因为没有其他方法可以通过这些数字来诱导。
        if char in '3456789':
            curr = prev
        # 如果当前的char是0，那么可以有0种方法来解码以0开头的字符串。
        elif char == '0':
            curr = 0
        elif char in '12':
            # 如果当前char是1或2，下一个字符是0，那么我们就没有额外的解码方法。
            # 因此，dp[i] = dp[i+2](注:dp[i+1]为0，因为s[i+1]为'0'
            if i < n - 1 and s[i + 1] == '0':
                curr = prevPrev
            # 如果下一个字符是1-6(或者7-9用curr char作为'1'), 那么 dp[i] = dp[i+1] + dp[i+2]
            # dp[i] = dp[i+1] (表示当我们把1/2当作A/B时的数字。) + dp[i+2] (表示1/2和下一个数字的数字
            elif i < n - 1 and ((s[i + 1] in '123456') or (s[i + 1] in '789' and char == '1')):
                curr = prev + prevPrev
            # 如果我们有1/2作为字符串的最右边的数字，那么我们就没有其他的方法来生成了。
            else:
                curr = prev
        prev, prevPrev = curr, prev
        i -= 1
    return prev


print(numDecodings("102"))

















