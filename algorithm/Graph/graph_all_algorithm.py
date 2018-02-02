"""
回溯法(探索与回溯法)是一种选优搜索法，按选优条件向前搜索，以达到目标。
但当探索到某一步时，发现原先选择并不优或达不到目标，就退回一步重新选择，
这种走不通就退回再走的技术为回溯法，而满足回溯条件的某个状态的点称为“回溯点”。


"""

"""
广度优先BFS

使用队列，集合
标记初始结点已被发现，放入队列
每次循环从队列弹出一个结点
将该节点的所有相连结点放入队列，并标记已被发现
通过队列，将迷宫路口所有的门打开，从一个门进去继续打开里面的门，然后返回前一个门处

（1）顶点v入队列。
（2）当队列非空时则继续执行，否则算法结束。
（3）出队列取得队头顶点v；访问顶点v并标记顶点v已被访问。
（4）查找顶点v的第一个邻接顶点col。
（5）若v的邻接顶点col未被访问过的，则col入队列。
（6）继续查找顶点v的另一个新的邻接顶点col，转到步骤（5）。
    直到顶点v的所有未被访问过的邻接点处理完。转到步骤（2）。

procedure BFS(G,v) is
   let Q be a queue
   Q.enqueue(v)
   label v as discovered
   while Q is not empty
    v ← Q.dequeue()
    procedure(v)
    for all edges from v to w in G.adjacentEdges(v) do
      if w is not labeled as discovered
        Q.enqueue(w)
        label w as discovered

"""


def procedure(v):
    pass


def BFS(G, v0):
    """ 广度优先搜索 """
    q, s = [], set ()
    q.extend (v0)
    s.add (v0)
    while q:  # 当队列q非空
        v = q.pop (0)
        procedure (v)
        for w in G[v]:  # 对图G中顶点v的所有邻近点w
            if w not in s:  # 如果顶点 w 没被发现
                q.extend (w)
                s.add (w)  # 记录w已被发现


"""
深度优先DFS

使用 栈，集合
初始结点入栈
每轮循环从栈中弹出一个结点，并标记已被发现
对每个弹出的结点，将其连接的所有结点放到队列中
通过栈的结构，一步步深入挖掘

（1）访问初始顶点v并标记顶点v已访问。
（2）查找顶点v的第一个邻接顶点w。
（3）若顶点v的邻接顶点w存在，则继续执行；否则回溯到v，再找v的另外一个未访问过的邻接点。
（4）若顶点w尚未被访问，则访问顶点w并标记顶点w为已访问。
（5）继续查找顶点w的下一个邻接顶点wi，如果v取值wi转到步骤（3）。直到连通图中所有顶点全部访问过为止。

Pseudocode[edit]
Input: A graph G and a vertex v of G
Output: All vertices reachable from v labeled as discovered
A recursive implementation of DFS:[5]
1 procedure DFS(G,v):
2   label v as discovered
3   for all edges from v to w in G.adjacentEdges(v) do
4     if vertex w is not labeled as discovered then
5       recursively call DFS(G,w)
A non-recursive implementation of DFS:[6]
1 procedure DFS-iterative(G,v):
2   let S be a stack
3   S.push(v)
4   while S is not empty
5      v = S.pop()
6      if v is not labeled as discovered:
7        label v as discovered
8        for all edges from v to w in G.adjacentEdges(v) do
9          S.push(w)

"""


def DFS(G, v0):
    S = []
    S.append (v0)
    label = set ()
    while S:
        v = S.pop ()
        if v not in label:
            label.add (v)
            procedure (v)
            for w in G[v]:
                S.append (w)


class Graph (object):
    def __init__(self, *args, **kwargs):
        self.node_neighbors = {}
        self.visited = {}
    
    def add_nodes(self, nodelist):
        for node in nodelist:
            self.add_node (node)
    
    def add_node(self, node):
        if not node in self.nodes ():
            self.node_neighbors[node] = []
    
    def add_edge(self, edge):
        u, v = edge
        if (v not in self.node_neighbors[u]) and (u not in self.node_neighbors[v]):
            self.node_neighbors[u].append (v)
            if (u != v):
                self.node_neighbors[v].append (u)
    
    def nodes(self):
        return self.node_neighbors.keys ()
    
    def depth_first_search(self, root=None):
        order = []
        
        def dfs(node):
            self.visited[node] = True
            order.append (node)
            for n in self.node_neighbors[node]:
                if not n in self.visited:
                    dfs (n)
        
        if root:
            dfs (root)
        for node in self.nodes ():
            if not node in self.visited:
                dfs (node)
        # print (order)
        return order
    
    def breadth_first_search(self, root=None):
        queue = []
        order = []
        
        def bfs():
            while len (queue) > 0:
                node = queue.pop (0)
                self.visited[node] = True
                for n in self.node_neighbors[node]:
                    if (not n in self.visited) and (not n in queue):
                        queue.append (n)
                        order.append (n)
        
        if root:
            queue.append (root)
            order.append (root)
            bfs ()
        for node in self.nodes ():
            if not node in self.visited:
                queue.append (node)
                order.append (node)
                bfs ()
        # print (order)
        return order


if __name__ == '__main__':
    g = Graph ()
    g.add_nodes ([i + 1 for i in range (8)])
    g.add_edge ((1, 2))
    g.add_edge ((1, 3))
    g.add_edge ((2, 4))
    g.add_edge ((2, 5))
    g.add_edge ((4, 8))
    g.add_edge ((5, 8))
    g.add_edge ((3, 6))
    g.add_edge ((3, 7))
    g.add_edge ((6, 7))
    print ("节点:", g.nodes ())
    order = g.breadth_first_search (1)
    print ("广度优先搜索:", order)
    order = g.depth_first_search (1)
    print ("深度优先搜索:", order)
