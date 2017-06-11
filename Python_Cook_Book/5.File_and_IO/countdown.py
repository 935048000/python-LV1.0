#!/usr/bin/env python
# coding=utf-8


'''
不能被序列化:依赖外部系统状态的对象，比如打开的文件，网络连接，线程，进程，栈帧等等。
用户自定义类可以通过提供 getstate () 和 setstate () 方法来绕过这些限制。
如果定义了这两个方法，pickle.dump() 就会调用 getstate () 获取序列化的对象。
类似的， setstate ()在反序列化时被调用。
为了演示这个工作原理，下面是一个在内部定义了一个线程但仍然可以序列化和反序列化的类：
'''


import time
import threading
class Countdown:
    def __init__(self, n):
        self.n = n
        self.thr = threading.Thread(target=self.run)
        self.thr.daemon = True
        self.thr.start()

    def run(self):
        while self.n > 0:
            print('T-minus', self.n)
            self.n -= 1
            time.sleep(2)

    def __getstate__(self):
        return self.n

    def __setstate__(self, n):
        self.__init__(n)

























