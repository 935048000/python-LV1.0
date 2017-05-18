#!/usr/bin/env python
#coding=utf-8
'''
生产者消费者队列
'''
from random import randrange #使其生产和消费的数量不同
from time import sleep
from Queue import Queue #队列
from myThread import MyThread

def writeQ(queue): #生产
    print '生产一个对象',
    queue.put('xxx', 1) #对象xxx
    print "对象总数：", queue.qsize()

def readQ(queue): #消费
    val = queue.get(1)
    print '消费一个对象 对象总数：', queue.qsize()

def writer(queue, loops): #单线程，向队列中放入（生产）一个对象，等待片刻，重复
    for i in range(loops):
        writeQ(queue)
        sleep(randrange(1, 4))

def reader(queue, loops): #单线程，向队列中取出（消费）一个对象，等待片刻，重复
    for i in range(loops):
        readQ(queue)
        sleep(randrange(2, 6))

funcs = [writer, reader] #设置 派生 的线程总数
nfuncs = range(len(funcs)) #设置 执行 的线程总数

def main():
    nloops = randrange(2, 6)
    q = Queue(32)

    threads = []
    for i in nfuncs: #创建线程
        t = MyThread(funcs[i], (q, nloops), \
            funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start() #执行线程

    for i in nfuncs:
        threads[i].join() #

    print '全部结束'

if __name__ == '__main__':
    main()
