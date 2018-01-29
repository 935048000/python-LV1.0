"""
哈夫曼树：

先对序列进行排序，然后永远找到序列中最小的两个值，然后在序列中去掉这俩。
加和之后放到原来的序列中，再次进行排序。
进行下一次循环的执行，直到序列中只剩下一个元素就可以停止了。

"""


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = None
        self.right = None

class Huffman(object):

    def __init__(self, items=[]):
        while len(items)!=1:
            a, b = items[0], items[1]
            newvalue = a.value + b.value
            newnode = Node(value=newvalue)
            newnode.left, newnode.right = a, b
            items.remove(a)
            items.remove(b)
            items.append(newnode)
            items = sorted(items, key=lambda node: int(node.value))
            # 每次都要记得更新新的霍夫曼树的根节点
            self.root = newnode

    def print(self):
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            print(current.value, end='\t')
            if(current.left):
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        print()


if __name__ == '__main__':
    ls = [Node(i) for i in range(1, 5)]
    huffman = Huffman(items=ls)
    huffman.print()
