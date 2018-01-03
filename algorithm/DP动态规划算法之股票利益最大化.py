

"""
假设有一个数组，它的第i个元素是一支给定的股票在第i天的价格。
如果你最多只允许完成一次交易,设计一个算法来找出最大利润。

a.先求出数组的前一个数与后一个数之差，组成新的数组 
b.求新数组的最大子数组和 
(原理：假设原数组(长度为n)为l[0…n-1]，新数组为d[0…n-2],其中d[i]=l[i+1]-l[i],
当求出d的最大子数组为d[x…y]时，则有： 
l[x+1]-l[x] + l[x+2]-l[x+1] … l[y+1]-l[y] = l[y+1]-l[x] 
也就求得原数组两数之差的最大值)

"""


def maxProfit1(list):
    # 算出利益比变化列表
    NEW=[]
    for i in range(len(list)-1):
        NEW.append(list[i+1]-list[i])
    # 初始化
    imax = 0
    temp = 0
    # 最大子数组和计算方式
    for d in NEW:
        if temp + d > 0:
            temp += d
        else:
            temp = 0
        # 获取当前最大子数组
        imax = max(temp,imax)
    return imax



"""
假设有一个数组，它的第i个元素是一个给定的股票在第i天的价格。
设计一个算法来找到最大的利润。你可以完成尽可能多的交易(多次买卖股票)。
然而,你不能同时参与多个交易(你必须在再次购买前出售股票)。

买卖次数无限，所以只要能获利就进行买卖，这样能保证所有利润都吃到自然利润最大。
"""
def maxProfit2(prices):
    max_profit = 0
    for i in range(1,len(prices)):
        d = prices[i] - prices[i-1]
        # 值为正即存在利益
        if d > 0 :
            max_profit += d
    return max_profit


"""
假设你有一个数组，其中第i 个元素是第i天给定股票的价格。
设计一个算法来找到最大的利润。您最多可以完成两笔交易。
您不可以同时进行多笔交易（即您必须在再次购买之前出售股票）。
"""

def maxProfit_3_1(prices):
    release1 = -999
    release2 = -999
    hold1 = 0
    hold2 = 0
    for i in prices:
        release2 = max (release2, hold2 + i)
        hold2 = max (hold2, release1 - i)
        release1 = max (release1, hold1 + i)
        hold1 = max (hold1, -i)
    return release2

def maxProfit_3_2(prices):
    sell = [0]
    buy = [0]
    plen = len (prices)
    minp = prices[0]
    maxp = prices[-1]

    for i in range (1, plen):
        minp, maxp = min (minp, prices[i]), max (maxp, prices[plen - i - 1])
        sell.append (max (sell[i - 1], prices[i] - minp))
        buy.append (max (buy[i - 1], maxp - prices[plen - i - 1]))

    return max (sell[i] + buy[plen - i - 1] for i in range (plen))


"""
假设你有一个数组，它的第i个元素是一支给定的股票在第i天的价格。
设计一个算法来找到最大的利润。你最多可以完成 k 笔交易。
你不可以同时参与多笔交易(你必须在再次购买前出售掉之前的股票)
"""
def maxProfit_4(k,prices):
    if not prices: return 0
    n = len (prices)
    if k >= n // 2:
        return sum (
            x - y
            for x, y in zip (prices[1:], prices[:-1])
            if x > y)

    profits = [0] * n
    for j in range (k):
        max_all = max_prev = max_here = 0
        for i in range (1, n):
            profit = prices[i] - prices[i - 1]
            max_here = max (max_here + profit, max_prev + profit, max_prev)
            max_prev = profits[i]
            profits[i] = max_all = max (max_all, max_here)
    return profits[-1]


"""
我将这些关键变量命名为本地利润和全局利润，以使事情更容易理解(至少对我来说是这样)。
"""
def maxProfit4(self, k, prices):
    n = len(prices)
    if n < 2:
        return 0
    if k >= n / 2:
        return sum(i - j
                   for i, j in zip(prices[1:], prices[:-1]) if i - j > 0)
    globalMax = [[0] * n for _ in xrange(k + 1)]
    for i in xrange(1, k + 1):
        # 最大的利润与我的交易和卖出股票在第j天。
        localMax = [0] * n
        for j in xrange(1, n):
            profit = prices[j] - prices[j - 1]
            localMax[j] = max(
                # 我们以(i - 1)的交易获利最多在(j - 1)天
                # 在最后一次交易中，我们每天买进股票(j - 1)，然后在第j日卖出。
                globalMax[i - 1][j - 1] + profit,
                # 在(j - 1)天内，我们以(i - 1)的转换期取得了最大的利润。
                # 最后一次交易，我们在j日买进股票，在同一天卖出，所以我们有0利润，显然我们不需要加它。
                globalMax[i - 1][j - 1],  # + 0,
                # 我们已在(j - 1)天内赢利。
                # 我们想取消那天(j - 1)的销售，在j日卖出。
                localMax[j - 1] + profit)
            globalMax[i][j] = max(globalMax[i][j - 1], localMax[j])
    return globalMax[k][-1]



L = [4,4,6,1,1,4,2,5]
L2 =  [3,2,3,1,2]
L3 = [2,1,2,0,1]


# print(calculateMax(L,2))
# print(get_diff_max_best(L3))
# print(maxProfit31(L))
print (maxProfit4(2,L))

