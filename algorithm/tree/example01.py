# 创建二叉树节点
class Node(object):
    def __init__(self, data, left, right):
        """
        :param data: 数据
        :param left: 左
        :param right: 右
        """
        self.data = data
        self.left = None
        self.right = None

# 创建二叉树
class Tree(object):
    # 创建一棵树，默认会有一个根节点
    def __init__(self, data):
        self.root = Node(data, None, None)
        self.size = 1

        ## 为了计算二叉树的宽度而用
        # 存放各层节点数目
        self.n = []
        # 初始化层，否则列表访问无效
        for item in range(pow(2, 5)):
            self.n.append(0)
        # 索引标识
        self.maxwidth = 0
        self.i = 0
        self.preorderList = []
        self.inorderList = []
        self.postorderList = []

    # 求二叉树包含的节点数目
    def getsize(self):
        stack = [self.root]
        # 为了正确获取数目，这里需要先初始化一下
        self.size = 0
        while stack:
            temp = stack.pop(0)
            self.size += 1
            if temp.left:
                stack.append(temp.left)
            if temp.right:
                stack.append(temp.right)
        return self.size

    # 默认以层次遍历打印出该二叉树
    def print(self):
        result = []
        if not self.root:
            return result
        A = []
        A.append (self.root)
        while A:
            temp = []
            size = len (A)
            for Node in A:
                temp.append (Node.data)
            result.append (temp)
            for i in range (size):
                node = A.pop (0)
                if node.left:
                    A.append (node.left)
                if node.right:
                    A.append (node.right)
        # result.reverse() # 反着
        return result

    # 递归实现前序遍历
    def qianxuDG(self, root):
        if root:
            # print(root.data)
            self.preorderList.append (root.data)
            self.qianxuDG(root.left)
            self.qianxuDG(root.right)
        # print(self.list)
        return self.preorderList

    # 递归实现中序遍历
    def zhongxuDG(self, root):
        if root:
            self.zhongxuDG(root.left)
            # print(root.data)
            self.inorderList.append (root.data)
            self.zhongxuDG(root.right)
        return self.inorderList

    # 递归实现后序遍历
    def houxuDG(self, root):
        if root:
            self.houxuDG (root.left)
            self.houxuDG (root.right)
            # print(root.data)
            self.postorderList.append (root.data)
        return self.postorderList


    # 求得二叉树的最大高度
    def height(self, root):
        """
        :param root:
        :return max hight: int
        每找到左或右节点就左+1或右+1，取最大的，继续递归
        """
        if not root:
            return 0
        ldeepth = self.height(root.left)
        rdeepth = self.height(root.right)
        return max(ldeepth+1, rdeepth+1)

    # 求得二叉树的最大深度
    def deepth(self, root):
        return self.height(root)-1

    # 求一颗二叉树的最大宽度
    def width(self, root):
        if root is None:
            return
        else:
            # 如果是访问根节点
            if self.i == 0:
                # 第一层加一
                self.n[0] = 1
                # 到达第二层
                self.i += 1
                if root.left:
                    self.n[self.i] += 1
                if root.right:
                    self.n[self.i] += 1
                    # print('临时数据：', self.n)
            else:
                # 访问子树
                self.i += 1
                # print('二叉树所在层数：', self.i)
                if root.left:
                    self.n[self.i] += 1
                if root.right:
                    self.n[self.i] += 1
            # 开始判断, 取出最大值
            # maxwidth = max(maxwidth, n[i])
            # maxwidth.append(max(max(maxwidth), n[i]))
            self.maxwidth = max (self.maxwidth, self.n[self.i])
            # 遍历左子树
            self.width (root.left)
            # 往上退一层
            self.i -= 1
            # 遍历右子树
            self.width (root.right)
        
            return self.maxwidth

    # 最大宽度
    def maxWidth(self, root):
        self._maxWidth = 0
        level = [(1, root)]
        while level:
            self._maxWidth = max (self._maxWidth, level[-1][0] - level[0][0] + 1)
            level = [kid
                     for number, node in level
                     for kid in enumerate ((node.left, node.right), 2 * number)
                     if kid[1]]
        return self._maxWidth

    # 最大宽度
    def widthOfBinaryTreeBFS(self, root):
        """
        给每个节点一个位置值,BFS中，所有具有相同深度的节点都是相邻搜索的，
        只需要记住每个深度的第一个和最后一个位置。
        """
        queue = [(root, 0, 0)]
        cur_depth = left = ans = 0
        for node, depth, pos in queue:
            if node:
                queue.append ((node.left, depth + 1, pos * 2))
                queue.append ((node.right, depth + 1, pos * 2 + 1))
                if cur_depth != depth:
                    cur_depth = depth
                    left = pos
                ans = max (pos - left + 1, ans)
    
        return ans

    # 最大宽度
    def widthOfBinaryTreeDFS(self, root):
        """
        创建一个dfs迭代器来产生每个节点的深度和位置。
        需要知道每个深度，剩下的最左边的位置（深度）和最右边的位置（深度）。遍历节点时最大的宽度。
        """
    
        def dfs(node, depth=0, pos=0):
            if node:
                yield depth, pos
                yield from dfs (node.left, depth + 1, pos * 2)
                yield from dfs (node.right, depth + 1, pos * 2 + 1)
    
        left = {}
        right = {}
        ans = 0
        for depth, pos in dfs (root):
            left[depth] = min (left.get (depth, pos), pos)
            right[depth] = max (right.get (depth, pos), pos)
            ans = max (ans, right[depth] - left[depth] + 1)
    
        return ans

    # 二叉树的先序遍历非递归实现
    def xianxu(self):
        """
        进栈向左走， 如果当前节点有右子树， 则先把右子树入栈，再把左子树入栈。来实现先根遍历效果
        :return:
        """
        if self.root is None:
            return
        else:
            stack = [self.root]
            while stack:
                current = stack.pop()
                print(current.data)
                if current.right:
                    stack.append(current.right)
                if current.left:
                    stack.append(current.left)

    # 二叉树的中序非递归实现
    def zhongxu(self):
        if self.root is None:
            return
        else:
            # stack = [self.root]
            # current = stack[-1]
            stack = []
            current = self.root
            while len(stack)!=0 or current:
                if current:
                    stack.append(current)
                    current = current.left
                else:
                    temp = stack.pop()
                    print(temp.data)
                    current = temp.right

    # 二叉树的中序非递归实现
    def zhongxuIterator(self,root):
        result = []
        if root is None:
            return
        else:
            stack = []
            current = root
            while len (stack) != 0 or current:
                if current:
                    stack.append (current)
                    current = current.left
                else:
                    temp = stack.pop ()
                    current = temp.right
                    yield temp.data


    # 二叉树的后序非递归实现
    def houxu(self):
        if self.root is None:
            return
        else:
            stack1 = []
            stack2 = []
            stack1.append(self.root)
            # 对每一个头结点进行判断，先将该头结点放到栈2中，如果该节点有左子树则放入栈1， 有右子树也放到栈1
            while stack1:
                current = stack1.pop()
                stack2.append(current)
                if current.left:
                    stack1.append(current.left)
                if current.right:
                    stack1.append(current.right)
            # 直接遍历输出stack2即可
            while stack2:
                print(stack2.pop().data)

    # 翻转(镜像)二叉树
    def invertTree(self,root):
        if root is None:
            return
        root.left, root.right = root.right, root.left
        self.invertTree (root.right)
        self.invertTree (root.left)
        return root

    # 递归 是否对称？
    def isSymmetric(self, root):
        def isSym(L, R):
            if L and R and L.data == R.data:
                return isSym (L.left, R.right) and isSym (L.right, R.left)
            return L == R
    
        return isSym (root, root)

    # 迭代 是否对称？
    def isSymmetric2(self, root):
        queue = [root]
        while queue:
            values = [i.data if i else None for i in queue]
            if values != values[::-1]: return False
            queue = [child for i in queue if i for child in (i.left, i.right)]
        return True

    # 比较二叉树是否完全一样
    def isIdentical(self, a, b):
        if a == None and b == None:
            return True
        if a == None or b == None:
            return False

        if a.data != b.data:
            return False

        return self.isIdentical (a.left, b.left) and self.isIdentical (a.right, b.right)

    # 打印二叉树矩阵
    def TreeMatrix(self, root):
        rows = self.height (root)
        cols = 2 ** rows - 1
        res = [['' for _ in range (cols)] for _ in range (rows)]
    
        def traverse(node, level, pos):
            if not node:
                return
            left_padding, spacing = 2 ** (rows - level - 1) - 1, 2 ** (rows - level) - 1
            index = left_padding + pos * (spacing + 1)
            # print (level, index, node.data)
            res[level][index] = str (node.data)
            traverse (node.left, level + 1, pos << 1)
            traverse (node.right, level + 1, (pos << 1) + 1)
    
        traverse (root, 0, 0)
        return res

    # 和叶数的和
    def sumNumbers(self, root):
        self.res = 0
    
        def dfs(root, value):
            if root:
                # if not root.left and not root.right:
                #    self.res += value*10 + root.val
                dfs (root.left, value * 10 + root.data)
                # if not root.left and not root.right:
                #    self.res += value*10 + root.val
                dfs (root.right, value * 10 + root.data)
                if not root.left and not root.right:
                    self.res += value * 10 + root.data
    
        dfs (root, 0)
        return self.res

if __name__ == '__main__':
    # 手动创建一课二叉树
    print('手动创建一课二叉树')
    tree = Tree(1)
    tree.root.left = Node(2, None, None)
    tree.root.right = Node(3, None, None)
    tree.root.left.left = Node(4, None, None)
    tree.root.left.right = Node(5, None, None)
    tree.root.right.left = Node(6, None, None)
    tree.root.right.right = Node(7, None, None)
    tree.root.left.left.left = Node(8, None, None)
    tree.root.left.left.right = Node(9, None, None)
    tree.root.left.right.left = Node(10, None, None)
    tree.root.left.right.left = Node(11, None, None)
    # # 测试一下是否创建成功
    # print('测试一下是否创建成功')
    # print(tree.root.data)
    # print(tree.root.left.data)
    # print(tree.root.right.data)
    # print(tree.root.left.left.data)
    # print(tree.root.left.right.data)
    # 调用方法打印一下效果：以层次遍历实现
    # print('翻转二叉树（镜像）')
    # tree.invertTree(tree.root)
    print ('调用方法打印一下效果：以层次遍历实现')
    print (tree.print ())
    # print ('调用方法打印一下效果：打印二叉树矩阵')
    # print(tree.TreeMatrix(tree.root))

    # print ('前序遍历递归实现', tree.qianxuDG (tree.root))
    # print ('中序遍历递归实现', tree.zhongxuDG (tree.root))
    # print ('后序遍历递归实现', tree.houxuDG (tree.root))
    
    # # 求取二叉树的高度
    # print('求取二叉树的高度')
    # print(tree.height(tree.root))
    # # 求取二叉树的深度
    # print('求取二叉树的深度')
    # print(tree.deepth(tree.root))
    # # 二叉树的非递归先序遍历实现
    # print('二叉树的非递归先序遍历实现')
    # tree.xianxu()
    # print('中序非递归遍历测试')
    # tree.zhongxu()
    # print ('中序非递归 迭代器 遍历测试')
    # print (next (tree.zhongxuIterator(tree.root)))
    # print('后序非递归遍历测试')
    # tree.houxu()
    # print ('二叉树的最大宽度为：',tree.width(tree.root))
    # print ('二叉树的最大宽度为：',tree.maxWidth (tree.root))
    # print('二叉树的节点数目为： {}'.format(tree.getsize()))
    # print("是否对称？",tree.isSymmetric(tree.root))
    print ("和叶数的和", tree.sumNumbers (tree.root))
