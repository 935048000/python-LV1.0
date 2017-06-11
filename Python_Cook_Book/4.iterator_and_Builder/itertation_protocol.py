#!/usr/bin/env python
# coding=utf-8


'''
实现迭代器协议
构建一个能支持迭代操作的自定义对象，并希望找到一个能实现迭代协议的简单方法。
一个对象上实现迭代最简单的方式是使用一个生成器函数。
'''


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

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()


# Example
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))
    for ch in root.depth_first():
    print(ch)
# Outputs Node(0), Node(1), Node(3), Node(4), Node(2), Node(5)






















