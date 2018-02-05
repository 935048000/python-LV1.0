#!/usr/bin/env python
# coding=utf-8



'''
计算函数运行时间的装饰器


'''


import time

def print_time(arr):
    def _time_cha(arg):
        t1 = time.time()
        ret = arr(arg)
        print ((time.time () - t1), "s")
        print (ret)
        return ret
    return _time_cha






