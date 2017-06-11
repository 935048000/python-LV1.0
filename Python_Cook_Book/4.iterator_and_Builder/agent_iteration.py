#!/usr/bin/env python
# coding=utf-8


'''
代理迭代
构建了一个自定义容器对象，里面包含有列表、元组或其他可迭代对象。
直接在你的这个新容器对象上执行迭代操作。
'''

#定义一个 __iter__() 方法，将迭代操作代理到容器内部的对象上

class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

# Example
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    # Outputs Node(1), Node(2)
    for ch in root:
    print ch
























