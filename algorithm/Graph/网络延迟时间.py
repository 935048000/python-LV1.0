"""
有N网络节点，标记1来N。
给定times一个作为有向边的传播时间列表
源节点times[i] = (u, v, w)在哪里u,v是目标节点，w是信号从源到目标传输所花费的时间。
现在，我们从某个节点发出一个信号K。所有节点接收信号需要多长时间？如果不可能，则返回-1


我们会保持dist[node]，我们最早到达每一个node。
当访问一个node，而elapsed时间已经过去，如果这是该节点的当前速度最快的信号，让我们从该节点的广播信号。
为了加快速度，在每个被访问的节点上，我们将通过对边缘进行排序来考虑先退出节点的信号。
"""
import collections


def networkDelayTime(times, N, K):
    graph = collections. defaultdict(list)
    for u, v, w in times:
        graph[u]. append((w, v))
    
    dist = {node: float('inf') for node in range (1, N + 1)}
    
    def dfs(node, elapsed):
        if elapsed >= dist[node]: return
        dist[node] = elapsed
        for time, nei in sorted (graph[node]):
            dfs (nei, elapsed + time)
    
    dfs (K, 0)
    ans = max (dist.values ())
    return ans if ans < float ('inf') else -1



print(networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))




