"""
BFS:单对节点间最短路径问题，如果每条边的权值都一样(或者说边一样长)的话
动规中的DAG最短路径算法:有向无环图,单对节点间最短路径问题
现实中的图总是有环的，边的权值也总是不同，而且可能有负权值，所以我们还需要其他的算法！
"""

# 松弛技术relaxtion
from copy import deepcopy

"""
D保存各个节点到源点的距离值估计(上界值)
P保存节点的最短路径上的前驱节点
W保存边的权值,其中不存在的边的权值为inf

松弛：
松弛就是说，假设节点 u 和节点 v 事先都有一个最短距离的估计
如果现在要松弛边(u,v)，也就是对从节点 u 通过边(u,v)到达节点 v，
将这条路径得到节点 v 的距离估计值(7+3=10)和原来的节点 v 的距离估计值(13)进行比较，
如果前者更小的话，就表示我们可以放弃在这之前确定的从源点到节点 v 的最短路径，改成从源点到节点 u，
然后节点 u 再到节点 v，这条路线距离会更短些，这也就是发生了一次松弛！

如果随机地对边进行松弛，那么与该边有关的节点的距离估计值就会慢慢地变得更加准确，
这样的改进会在整个图中进行传播，如果一直这么松弛下去的话，
最终整个图所有节点的距离值都不会发生变化的时候我们就得到了从源点到所有节点的最短路径值。

每次松弛可以看作是向最终解前进了“一步”，我们的目标自然是希望松弛的次数越少越好，
关键就是要确定松弛的次数和松弛的顺序(好的松弛顺序可以让我们直接朝着最优解前进，缩短算法运行时间)
"""
inf = float ('inf')


def relax(W, u, v, D, P):
    d = D.get (u, inf) + W[u][v]  # 可能的捷径估计
    if d < D.get (v, inf):  # 这真的是一条捷径吗?
        D[v], P[v] = d, u  # 更新估计和父
        return True  # 有一个改变!


# 测试代码
# u = 0; v = 1
# D, W, P = {}, {u:{v:3}}, {}
# D[u] = 7
# D[v] = 13
# print (D[u])  # 7
# print (D[v])  # 13
# print (W[u][v])  # 3
# relax(W, u, v, D, P) # True
# print (D[v])  # 10
# D[v] = 8
# relax(W, u, v, D, P)
# print (D[v])  # 8



# Bellman-Ford 算法的一个重要作用：判断图中是否存在负权回路。
def bellman_ford(G, s):
    D, P = {s: 0}, {}  # Zero-dist to s; 没有父母
    for rnd in G:  # n = len(G) 循环
        changed = False  # 到目前为止没有变化。
        for u in G:  # 对于每个从节点…
            for v in G[u]:  # ... 和它的节点。..
                if relax (G, u, v, D, P):  # 从u到v的捷径?
                    changed = True  # 是的!所以的东西改变了
        if not changed: break  # 没有改变:完成。
    else:  # 在第一轮之前没有做过?
        raise ValueError ('negative cycle')  # 负周期检测
    return D, P  # 否则:D和P是正确的。


# 测试代码
# s, t, x, y, z = range (5)
# W = {
#     s: {t: 6, y: 7},
#     t: {x: 5, y: 8, z: -4},
#     x: {t: -2},
#     y: {x: -3, z: 9},
#     z: {s: 2, x: 7}
# }
# D, P = bellman_ford (W, s)
#
# print ([D[v] for v in [s, t, x, y, z]]) # [0, 2, 4, 7, -2]
# print (s not in P)  # True
# print ([P[v] for v in [t, x, y, z]] == [x, y, s, t]) # True
# W[s][t] = -100
# print (bellman_ford(W, s))



# Dijkstra算法
"""
Dijkstra算法，它看起来非常像Prim算法，同样是基于贪心策略，
每次贪心地选择松弛距离最近的“边缘节点”所在的那条边
Dijkstra算法隐藏了一个DAG最短路径算法

DAG最短路径算法是先进行拓扑排序然后松弛，
Dijkstra算法是每次直接贪心地选择一条边来松弛。

Dijkstra算法和Prim算法的实现很像，也和BFS算法实现很像
ijkstra算法的时间复杂度和使用的优先队列有关
"""
# Dijkstra算法
from heapq import heappush, heappop


def dijkstra(G, s):
    D, P, Q, S = {s: 0}, {}, [(0, s)], set ()  # Est., tree, queue, visited
    while Q:  # 还未处理的节点吗?
        _, u = heappop (Q)  # 节点与最低估计
        if u in S: continue  # 已经访问了吗?跳过它
        S.add (u)  # 我们参观了现在
        for v in G[u]:  # 穿过所有的邻居。
            relax (G, u, v, D, P)  # 放松条边
            heappush (Q, (D[v], v))  # 添加到队列中,w /美国东部时间。作为革命制度党
    return D, P  # 最后D和P返回。


# 测试代码
# s, t, x, y, z = range(5)
# W = {
#     s: {t:10, y:5},
#     t: {x:1, y:2},
#     x: {z:4},
#     y: {t:3, x:9, z:2},
#     z: {x:6, s:7}
#     }
# D, P = dijkstra(W, s)
# print ([D[v] for v in [s, t, x, y, z]]) # [0, 8, 9, 5, 7]
# print (s not in P) # True
# print ([P[v] for v in [t, x, y, z]] == [y, t, s, y]) # True


# Johnson算法
"""
巧妙地利用Bellman-Ford和Dijkstra算法结合来解决所有节点对最短路径问题的算法
特别适合用于稀疏图，算法的时间复杂度是O(mnlgn)

使用Bellman-Ford算法得到每个节点的最短路径值，
然后利用这些值修改图中边的权值，
最后我们对图中所有节点都运行一次Dijkstra算法就解决了所有节点对最短路径问题
"""


def johnson(G):  # 所有对最短路径
    G = deepcopy (G)  # 不要破坏原有的东西。
    s = object ()  # 保证独特的节点
    G[s] = {v: 0 for v in G}  # s的边为0 wgt
    h, _ = bellman_ford (G, s)  # h[v]: 从s最短的距离
    del G[s]  # 不再需要 s
    for u in G:  # u的体重...
        for v in G[u]:  # ... to v...
            G[u][v] += h[u] - h[v]  # ... 调整(nonneg)。
    D, P = {}, {}  # D[u][v] and P[u][v]
    for u in G:  # 从每一个u…
        D[u], P[u] = dijkstra (G, u)  # ... 寻找最短路径
        for v in G:  # 为每个目的地……
            D[u][v] += h[v] - h[u]  # ... 调整的距离
    return D, P  # 这些都是二维的


# a, b, c, d, e = range (5)
# W = {
#     a: {c: 1, d: 7},
#     b: {a: 4},
#     c: {b: -5, e: 2},
#     d: {c: 6},
#     e: {a: 3, b: 8, d: -4}
# }
# D, P = johnson (W)
# print ([D[a][v] for v in [a, b, c, d, e]]) # [0, -4, 1, -1, 3]
# print ([D[b][v] for v in [a, b, c, d, e]]) # [4, 0, 5, 3, 7]
# print ([D[c][v] for v in [a, b, c, d, e]]) # [-1, -5, 0, -2, 2]
# print ([D[d][v] for v in [a, b, c, d, e]]) # [5, 1, 6, 0, 8]
# print ([D[e][v] for v in [a, b, c, d, e]]) # [1, -3, 2, -4, 0]



# Floyd-Warshall算法
"""
基于动态规划的算法，时间复杂度是O(n3)，n是图中节点数

假设所有节点都有一个数字编号(从1开始)，我们要把原来的问题reduce成一个个子问题，
子问题有三个参数：起点 u、终点 v、能经过的节点的最大编号k，
也就是求从起点 u 到终点 v 只能够经过编号为(1,2,3,…,k)的节点的最短路径问题

d(u,v,k) = min(d(u,v,k-1), d(u,k,k-1) + d(k,v,k-1))
"""

# 递归版本的Floyd-Warshall算法
from functools import wraps


def memo(func):
    cache = {}  # 存储子问题的解决方案
    
    @wraps (func)  # 让wrap看起来像func。
    def wrap(*args):  # memoize的包装器
        if args not in cache:  # 没有计算?
            cache[args] = func (*args)  # 计算并缓存解决方案。
        return cache[args]  # 返回缓存的解决方案
    
    return wrap  # 返回包装


def rec_floyd_warshall(G):  # 全部最短路
    @memo  # 存储上
    def d(u, v, k):  # u to v via 1..k
        if k == 0: return G[u][v]  # Assumes v in G[u]
        return min (d (u, v, k - 1), d (u, k, k - 1) + d (k, v, k - 1))  # 使用k或不?
    
    return {(u, v): d (u, v, len (G)) for u in G for v in G}  # D[u,v] = d(u,v,n)


# 空间优化后的Floyd-Warshall算法
def floyd_warshall1(G):
    D = deepcopy (G)  # 没有中间体
    for k in G:  # 用k寻找捷径。
        for u in G:
            for v in G:
                D[u][v] = min (D[u][v], D[u][k] + D[k][v])
    return D


# 求最短路径问题我们还需要知道最短路径是什么，这个时候我们只需要在进行选择的时候设置一个前驱节点就行了
# 最终版本的Floyd-Warshall算法
def floyd_warshall(G):
    D, P = deepcopy (G), {}
    for u in G:
        for v in G:
            if u == v or G[u][v] == inf:
                P[u, v] = None
            else:
                P[u, v] = u
    for k in G:
        for u in G:
            for v in G:
                shortcut = D[u][k] + D[k][v]
                if shortcut < D[u][v]:
                    D[u][v] = shortcut
                    P[u, v] = P[k, v]
    return D, P

# 测试代码
# a, b, c, d, e = range (1, 6)  # 从一开始的
# W = {
#     a: {c: 1, d: 7},
#     b: {a: 4},
#     c: {b: -5, e: 2},
#     d: {c: 6},
#     e: {a: 3, b: 8, d: -4}
# }
# for u in W:
#     for v in W:
#         if u == v: W[u][v] = 0
#         if v not in W[u]: W[u][v] = inf

# D = rec_floyd_warshall (W)
# print ([D[a,v] for v in [a, b, c, d, e]]) # [0, -4, 1, -1, 3]
# print ([D[b,v] for v in [a, b, c, d, e]]) # [4, 0, 5, 3, 7]
# print ([D[c,v] for v in [a, b, c, d, e]]) # [-1, -5, 0, -2, 2]
# print ([D[d,v] for v in [a, b, c, d, e]]) # [5, 1, 6, 0, 8]
# print ([D[e,v] for v in [a, b, c, d, e]]) # [1, -3, 2, -4, 0]

# D, P = floyd_warshall(W)
# print ([D[a][v] for v in [a, b, c, d, e]]) #[0, -4, 1, -1, 3]
# print ([D[b][v] for v in [a, b, c, d, e]]) #[4, 0, 5, 3, 7]
# print ([D[c][v] for v in [a, b, c, d, e]]) #[-1, -5, 0, -2, 2]
# print ([D[d][v] for v in [a, b, c, d, e]]) #[5, 1, 6, 0, 8]
# print ([D[e][v] for v in [a, b, c, d, e]]) #[1, -3, 2, -4, 0]
# print ([P[a,v] for v in [a, b, c, d, e]]) #[None, 2, 0, 4, 2]
# print ([P[b,v] for v in [a, b, c, d, e]]) #[1, None, 0, 4, 2]
# print ([P[c,v] for v in [a, b, c, d, e]]) #[1, 2, None, 4, 2]
# print ([P[d,v] for v in [a, b, c, d, e]]) #[1, 2, 3, None, 2]
# print ([P[e,v] for v in [a, b, c, d, e]]) #[1, 2, 3, 4, None]
