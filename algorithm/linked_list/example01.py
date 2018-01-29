class Node(object):
    '''
    data:数据
    _next：下一个节点的对象
    '''
    def __init__(self, data, pnext = None):
        self.data = data
        self._next = pnext

    def __repr__(self):
        '''输出data'''
        return str(self.data)

class ChainTable(object):
    '''
    head：链表头
    length：链表长度

    '''
    def __init__(self):
        self.head = None
        self.length = 0

    def isEmpty(self):
        '''判断是否为空'''
        return (self.length == 0)

    def append(self, dataOrNode):
        '''增加一个节点(在链表尾添加)'''
        item = None
        if isinstance(dataOrNode, Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)

        if not self.head:
            self.head = item
            self.length += 1

        else:
            node = self.head
            while node._next:
                node = node._next
            node._next = item
            self.length += 1

    def delete(self, index):
        '''
        删除一个节点
        删除一个节点之后把链表长度减一
        '''
        if self.isEmpty():
            print ("this chain table is empty.")
            return

        if index < 0 or index >= self.length:
            print ('error: out of index')
            return

        # 要注意删除第一个节点的情况
        # 如果有空的头节点就不用这样
        # 但是我不喜欢弄头节点
        if index == 0:
            self.head = self.head._next
            self.length -= 1
            return

        # prev为保存前导节点
        # node为保存当前节点
        # 当j与index相等时就
        # 相当于找到要删除的节点
        j = 0
        node = self.head
        prev = self.head
        while node._next and j < index:
            prev = node
            node = node._next
            j += 1

        if j == index:
            prev._next = node._next
            self.length -= 1

    def insert(self, index, dataOrNode):
        '''插入一个节点'''
        if self.isEmpty():
            print ("this chain tabale is empty")
            return

        if index < 0 or index >= self.length:
            print ("error: out of index")
            return

        item = None
        if isinstance(dataOrNode, Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)

        if index == 0:
            item._next = self.head
            self.head = item
            self.length += 1
            return

        j = 0
        node = self.head
        prev = self.head
        while node._next and j < index:
            prev = node
            node = node._next
            j += 1

        if j == index:
            item._next = node
            prev._next = item
            self.length += 1

    def update(self, index, data):
        '''修改一个节点'''
        if self.isEmpty() or index < 0 or index >= self.length:
            print ('error: out of index')
            return
        j = 0
        node = self.head
        while node._next and j < index:
            node = node._next
            j += 1

        if j == index:
            node.data = data

    def getItem(self, index):
        '''查找一个节点的data'''
        if self.isEmpty() or index < 0 or index >= self.length:
            print ("error: out of index")
            return
        j = 0
        node = self.head
        while node._next and j < index:
            node = node._next
            j += 1

        return node.data


    def getIndex(self, data):
        '''查找一个节点的索引'''
        j = 0
        if self.isEmpty():
            print ("this chain table is empty")
            return
        node = self.head
        while node:
            if node.data == data:
                return j
            node = node._next
            j += 1

        if j == self.length:
            print ("%s not found" % str(data))
            return

    def clear(self):
        '''清空链表'''
        self.head = None
        self.length = 0

    def __repr__(self):
        if self.isEmpty():
            return "empty chain table"
        node = self.head
        nlist = ''
        while node:
            nlist += str(node.data) + ' '
            node = node._next
        return nlist

    def __getitem__(self, ind):
        if self.isEmpty() or ind < 0 or ind >= self.length:
            print ("error: out of index")
            return
        return self.getItem(ind)

    def __setitem__(self, ind, val):
        if self.isEmpty() or ind < 0 or ind >= self.length:
            print ("error: out of index")
            return
        self.update(ind, val)

    def __len__(self):
        return self.length

if __name__ == '__main__':
    list = ChainTable()

    for i in range(10):
        list.append(i)

    print(list)
    print(list.getIndex(5))
    print(list.update(0,99))
    print(list.delete(1))
    print(list)
    print(list.insert(0,88))
    print(list)
    print(list.getItem(5))
    print(list[6])
    print("getItem",list.getItem(0))
    print ("getIndex",list.getIndex(88))
    print("len:",len(list))