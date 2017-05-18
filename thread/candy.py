#!/usr/bin/env python
#coding=utf-8
'''
虚拟糖果机
'''
from atexit import register
from random import randrange
from threading import BoundedSemaphore, Lock, Thread
from time import sleep, ctime

lock = Lock()
MAX = 5 #库存最大值
candytray = BoundedSemaphore(MAX) #糖果托盘

def refill(): #糖果机所有者向库中添加糖果时 执行
    lock.acquire()
    print '填充糖果...',
    try:
        candytray.release()
    except ValueError:
        print '满, 跳过'
    else:
        print 'OK'
    lock.release()

def buy(): #消费
    lock.acquire()
    print '购买糖果...',
    if candytray.acquire(False):
        print 'OK'
    else:
        print '空的, 跳过'
    lock.release()

def producer(loops): #调用refill()间暂停
    for i in xrange(loops):
        refill()
        sleep(randrange(3))

def consumer(loops): #调用buy()间暂停
    for i in xrange(loops):
        buy()
        sleep(randrange(3))

def _main():
    print '开始！ 时间:', ctime()
    nloops = randrange(2, 6)
    print '糖果机 (满： %d )' % MAX
    Thread(target=consumer, args=(randrange(
        nloops, nloops+MAX+2),)).start()  # 消费
    Thread(target=producer, args=(nloops,)).start() # 生产

@register
def _atexit():
    print '结束 时间:', ctime()

if __name__ == '__main__':
    _main()
