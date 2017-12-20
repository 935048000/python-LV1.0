"""
下载URL的内容从一个队列中获取。这个版本使用Twisted框架提供并发性

"""

from twisted.internet import defer
from twisted.web.client import getPage
from twisted.internet import reactor, task

import queue
from elapsed_time import ET


def success_callback(results, name, url, et):
    print(f'Task {name} got URL: {url}')
    print(f'Task {name} total elapsed time: {et():.1f}')


def my_task(name, queue):
    if not queue.empty():
        while not queue.empty():
            url = queue.get()
            print(f'Task {name} getting URL: {url}')
            et = ET()
            d = getPage(url)
            d.addCallback(success_callback, name, url, et)
            yield d


def main():
    """
    This is the main entry point for the program
    """
    # create the queue of 'work'
    work_queue = queue.Queue()

    # put some 'work' in the queue
    for url in [
        b"http://qq.com",
        b"http://hao123.com",
        b"http://baidu.com",
        b"http://sina.com.cn",
        b"http://silentdusk.com",
        b"http://github.com"
    ]:
        work_queue.put(url)

    # run the tasks
    et = ET()

    # create cooperator
    coop = task.Cooperator()

    defer.DeferredList([
        coop.coiterate(my_task('One', work_queue)),
        coop.coiterate(my_task('Two', work_queue)),
    ]).addCallback(lambda _: reactor.stop())

    # run the event loop
    reactor.run()

    print()
    print(f'Total elapsed time: {et():.1f}')


if __name__ == '__main__':
    main()
