#!/usr/bin/env python
#coding=utf-8

from atexit import register
from random import randrange
from threading import Thread, Lock, currentThread
from time import sleep, ctime

class CleanOutputSet(set):#集合的子类，将默认输出改变为所以元素安装逗号分隔
    def __str__(self):
        return ', '.join(x for x in self)

#lock = Lock()
loops = (randrange(2, 5) for x in xrange(randrange(3, 7)))#随机生成3~6个线程，每个线程睡眠2~4s。
remaining = CleanOutputSet()#修改后集合的实例

def loop(nsec):
    myname = currentThread().name #保存当前执行它的进程名
    #lock.acquire()
    remaining.add(myname) #放入线程名
    print '[%s] Started %s' % (ctime(), myname) #线程输出是原子的
    #print '[{0}] Started {1}'.format(ctime(), myname)
    #lock.release()
    sleep(nsec) #睡眠
    #lock.acquire()
    remaining.remove(myname) #删除线程名
    print '[%s] Completed %s (%d secs)' % ( #完成的线程
    #print '[{0}] Completed {1} ({2} secs)'.format(
        ctime(), myname, nsec)
    print '    (remaining: %s)' % (remaining or 'NONE')  #剩余线程
    #print '    (remaining: {0})'.format(remaining or 'NONE')
    #lock.release()

def _main():
    for pause in loops: #执行每个线程
        Thread(target=loop, args=(pause,)).start()

@register #注册 _atexit() 函数
def _atexit(): #脚本退出前执行该函数。
    print 'all DONE at:', ctime()

if __name__ == '__main__':
    _main()