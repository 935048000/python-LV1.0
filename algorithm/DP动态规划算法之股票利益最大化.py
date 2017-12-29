

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
def maxProfit1(l):
    length=len(l)
    #求出前一天与后一天的差值
    diff=[]
    for i in range(length-1):
        diff.append(l[i+1]-l[i])
    max_sum=0
    cur_sum=0
    for d in diff:
        if cur_sum+d>0:
            cur_sum+=d
        else:
            cur_sum=0
        max_sum = max(cur_sum,max_sum)
    return max_sum



"""
假设有一个数组，它的第i个元素是一个给定的股票在第i天的价格。
设计一个算法来找到最大的利润。你可以完成尽可能多的交易(多次买卖股票)。
然而,你不能同时参与多个交易(你必须在再次购买前出售股票)。

买卖次数无限，所以只要能获利就进行买卖，这样能保证所有利润都吃到自然利润最大。
"""
def maxProfit2(prices):
    max = 0
    for i in range(1,len(prices)):
        d = prices[i] - prices[i-1]
        if d > 0 :
            max += d

    return max




# public int maxProfit(int[] prices) {
#     int hold1 = Integer.MIN_VALUE, hold2 = Integer.MIN_VALUE;
#     int release1 = 0, release2 = 0;
#     for(int i:prices){                              // Assume we only have 0 money at first
#         release2 = Math.max(release2, hold2+i);     // The maximum if we've just sold 2nd stock so far.
#         hold2    = Math.max(hold2,    release1-i);  // The maximum if we've just buy  2nd stock so far.
#         release1 = Math.max(release1, hold1+i);     // The maximum if we've just sold 1nd stock so far.
#         hold1    = Math.max(hold1,    -i);          // The maximum if we've just buy  1st stock so far.
#     }
#     return release2; ///Since release1 is initiated as 0, so release2 will always higher than release1.
# }
"""
假设你有一个数组，其中第i 个元素是第i天给定股票的价格。
设计一个算法来找到最大的利润。您最多可以完成两笔交易。
您不可以同时进行多笔交易（即您必须在再次购买之前出售股票）。
"""
def maxProfit3(prices):
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

def maxProfit31(p):
    sell = [0]
    buyd = [0]
    n = len (p)
    minp = p[0]
    maxp = p[-1]

    for i in range (1, n):
        minp, maxp = min (minp, p[i]), max (maxp, p[n - i - 1])
        sell.append (max (sell[i - 1], p[i] - minp))
        buyd.append (max (buyd[i - 1], maxp - p[n - i - 1]))

    return max (sell[i] + buyd[n - i - 1] for i in range (n))


"""
假设你有一个数组，它的第i个元素是一支给定的股票在第i天的价格。
设计一个算法来找到最大的利润。你最多可以完成 k 笔交易。
你不可以同时参与多笔交易(你必须在再次购买前出售掉之前的股票)
"""
def maxProfit4(k,prices):
    if not prices: return 0
    n = len (prices)
    if k >= n // 2:
        return sum (
            x - y
            for x, y in zip (prices[1:], prices[:-1])
            if x > y)

    profits = [0] * n
    for j in range (k):
        # Update new_profits
        max_all = max_prev = max_here = 0
        for i in range (1, n):
            profit = prices[i] - prices[i - 1]
            max_here = max (max_here + profit, max_prev + profit, max_prev)
            max_prev = profits[i]
            profits[i] = max_all = max (max_all, max_here)
    return profits[-1]





L = [4,4,6,1,1,4,2,5]
L2 =  [3,2,3,1,2]
L3 = [2,1,2,0,1]


# print(calculateMax(L,2))
# print(get_diff_max_best(L3))
# print(maxProfit31(L))
print (maxProfit4(2,L))

