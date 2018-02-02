"""


在LeetCode商店，有一些项目出售。每个项目都有一个价格。
但是，有一些特别的优惠，特价优惠包括一个或多个销售价格不同的物品。
你会得到每件商品的价格，一系列特价商品以及我们需要为每件商品购买的商品数量。
这项工作是输出最低的价格，你必须支付的确切的某些项目给出，在那里你可以优化使用的特别优惠。
每个特别优惠都以数组的形式表示，
最后一个数字表示您需要为此特价支付的价格，其他数字则表示您购买此优惠时可获得的具体项目数。
您可以多次使用任何特殊优惠。

输入： [2,5]，[[3,0,5]，[1,2,10]]，[3,2]
输出： 14
说明：
有两种物品，A和B.他们的价格分别是2美元和5美元。
在特别优惠1，你可以支付3A和0B 5美元
在特别优惠2，你可以支付1A和2B $ 10。
你需要购买3A和2B，所以你可以支付1A和2B（特别优惠＃2）10美元，2A支付4美元。
"""


def shoppingOffers(price, special, needs):
    d = {}
    
    def dfs(cur):
        # 成本没有特殊
        val = sum (cur[i] * price[i] for i in range (len (needs)))
        for spec in special:
            tmp = [cur[j] - spec[j] for j in range (len (needs))]
            # 跳过超出需求的交易。
            if min (tmp) >= 0:
                # 首先检查字典，以获得结果，否则执行dfs。
                val = min (val, d.get (tuple (tmp), dfs (tmp)) + spec[-1])
        d[tuple (cur)] = val
        return val
    
    return dfs (needs)

print(shoppingOffers([2,5], [[3,0,5],[1,2,10]], [3,2]))















