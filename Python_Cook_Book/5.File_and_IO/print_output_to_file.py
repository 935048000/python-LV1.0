#!/usr/bin/env python
# coding=utf-8


'''
打印输出至文件中
将 print() 函数的输出重定向到一个文件中去
在 print() 函数中指定 file 关键字参数

sys.stdout = file:将标准输出管道连到打开的文件
sys.stdout.close():关闭管道，所以，使用print 输出的数据，本来是存放在管道中，close()之后，全部写入文件中。
sys.stdout = temp:重新连接到标准的输出
'''
import sys


temp=sys.stdout
f=open('testfile.txt','a+')
data=f.read()
print data
sys.stdout = f
print "test data"
print '\n'
sys.stdout=temp
#sys.stdout.flush()
sys.stdout.close()



























