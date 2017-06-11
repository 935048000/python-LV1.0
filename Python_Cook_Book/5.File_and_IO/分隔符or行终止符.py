#!/usr/bin/env python
# coding=utf-8


'''
 使用其他分隔符或行终止符打印
使用 print() 函数输出数据，但是想改变默认的分隔符或者行尾符
在 print() 函数中使用 sep 和 end 关键字参数
'''


print 'ACME', 50, 91.5
print 1
print('ACME', 50, 91.5, sep=',')
print 1
print('ACME', 50, 91.5, sep=',', end = '!!\n')

for i in range(5):
    print(i, end=' ')




















