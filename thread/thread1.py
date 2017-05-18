#!/usr/bin/env python

import thread
from time import sleep,ctime

def loop0():
    print 'start loop0 time:',ctime()
    sleep(4)
    print 'esc loop0 time:',ctime()

def loop1():
    print 'start loop1 time:',ctime()
    sleep(2)
    print 'esc loop1 time:',ctime()

def main():
    print 'starting time:',ctime()
    thread.start_new_thread(loop0,())
    thread.start_new_thread(loop1,())
    sleep(6)
    print 'esc all time',ctime()

if __name__ == '__main__':
    main()