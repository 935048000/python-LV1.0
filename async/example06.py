"""
下载URL的内容从一个队列中获取。它还使用gevent以异步方式获取URL。

"""

import gevent
from gevent import monkey
monkey.patch_all()

import queue
import requests
from elapsed_time import ET


def task(name, work_queue):
    while not work_queue.empty():
        url = work_queue.get()
        print(f'任务 {name} 获取 URL: {url}')
        et = ET()
        requests.get(url)
        print(f'任务 {name} 得到 URL: {url}')
        print(f'任务 {name} 总共过去的时间: {et():.1f}')

def main():
    """
    This is the main entry point for the program
    """
    # create the queue of 'work'
    work_queue = queue.Queue()

    # put some 'work' in the queue
    for url in [
        "http://qq.com",
        "http://hao123.com",
        "http://baidu.com",
        "http://sina.com.cn",
        "http://silentdusk.com",
        "http://github.com"
    ]:
        work_queue.put(url)

    # run the tasks
    et = ET()
    tasks = [
        gevent.spawn(task, 'One', work_queue),
        gevent.spawn(task, 'Two', work_queue)
    ]


    gevent.joinall(tasks)
    print()
    print(f'总共过去的时间: {et():.1f}')

if __name__ == '__main__':
    main()
