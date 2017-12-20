"""
从work_queue下载URL的内容。
这个版本使用Twisted框架提供并发性

"""
from twisted.internet import defer
from twisted.web.client import getPage
from twisted.internet import reactor, task

import queue
from elapsed_time import ET


@defer.inlineCallbacks
def my_task(name, work_queue):
    try:
        while not work_queue.empty():
            url = work_queue.get()
            print(f'任务 {name} 获取 URL: {url}')
            et = ET()
            yield getPage(url)
            print(f'任务 {name} 得到 URL: {url}')
            print(f'任务 {name} 总加工时间: {et():.1f}')
    except Exception as e:
        print(str(e))


def main():
    """
    This is the main entry point for the program
    """
    # create the work_queue of 'work'
    work_queue = queue.Queue()

    # put some 'work' in the work_queue
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
    defer.DeferredList([
        task.deferLater(reactor, 0, my_task, 'One', work_queue),
        task.deferLater(reactor, 0, my_task, 'Two', work_queue)
    ]).addCallback(lambda _: reactor.stop())

    # run the event loop
    reactor.run()

    print()
    print(f'总加工时间: {et():.1f}')


if __name__ == '__main__':
    main()

