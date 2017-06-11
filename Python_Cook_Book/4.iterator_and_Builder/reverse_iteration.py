#!/usr/bin/env python
# coding=utf-8


'''
反方向迭代一个序列
使用内置的 reversed() 函数
'''


a = [1, 2, 3, 4]
for x in reversed(a):
    print(x)
print
# f = open('/etc/passwd','r')
# for line in reversed(list(f)):
#     print(line)
# f.close()

class Countdown:

    def __init__(self, start):
        self.start = start

    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # Reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

for rr in reversed(Countdown(30)):
    print(rr)
print 
for rr in Countdown(30):
    print(rr)





















