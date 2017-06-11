#!/usr/bin/env python
# coding=utf-8


'''
 手动遍历迭代器
遍历一个可迭代对象中的所有元素，但是却不想使用 for 循环
手动的遍历可迭代对象，使用 next() 函数并在代码中捕获 StopIteration 异常。
'''

# StopIteration 用来指示迭代的结尾。

def manual_iter():
    with open('/etc/passwd','r') as f:
        try:
            while True:
                line = f.next()
                print(line)
        except StopIteration:
            pass

manual_iter()
























