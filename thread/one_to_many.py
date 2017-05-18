#!/usr/bin/env python
#coding=utf8
from myThread import MyThread #调用写好的类myThread.py
from time import ctime, sleep

#三个计算函数
def fib(x):
    sleep(0.005)
    if x < 2: return 1
    return (fib(x-2) + fib(x-1))

def fac(x):
    sleep(0.1)
    if x < 2: return 1
    return (x * fac(x-1))

def sum(x):
    sleep(0.1)
    if x < 2: return 1
    return (x + sum(x-1))

funcs = (fib, fac, sum)
n = 12

#主函数
def main():
    nfuncs = range(len(funcs))

    print '*** 单线程 ***'
    for i in nfuncs:
        print '运行', funcs[i].__name__, '时间:', ctime()
        print funcs[i](n)
        print funcs[i].__name__, '完成 时间:', ctime()

    print '\n*** 多线程  ***'
    print 'start time:',ctime()
    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (n,), funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()
        print threads[i].getResult()

    print '全部线程完成 end time:',ctime()

if __name__ == '__main__':
    main()
