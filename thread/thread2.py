#!/usr/bin/env python
#coding=utf8
import thread
from time import sleep,ctime

loops = [4,2]

def loop(nloop,nsec,lock):
    print 'start loop',nloop,'time:',ctime()
    sleep(nsec)
    print 'loop',nloop,'end time:',ctime()
    lock.release() #释放锁

def main():
    print 'starting time:',ctime()
    locks = [] #创建锁列表
    nloops = range(len(loops))


    for i in nloops:
        lock = thread.allocate_lock() #得到锁对象
        lock.acquire() #取得锁（锁上）
        locks.append(lock) #添加到锁列表中

    for i in nloops:
        thread.start_new_thread(loop,(i,loops[i],locks[i]))
        #循环，派生线程，每个线程调用loop()，并且传递循环号、睡眠时间、锁参数

    for i in nloops:
        while locks[i].locked():
            pass

    print 'end all time',ctime()


if __name__ == '__main__':
    main()
