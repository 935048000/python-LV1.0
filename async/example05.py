"""
一个简单的状态机在Python中
下载URL的内容从一个队列中获取

"""

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
        print(f'任务 {name} 总时间: {et():.1f}')
        yield


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

    tasks = [
        task('One', work_queue),
        task('Two', work_queue)
    ]
    # run the scheduler to run the tasks
    et = ET()
    done = False
    while not done:
        for t in tasks:
            try:
                next(t)
            except StopIteration:
                tasks.remove(t)
            if len(tasks) == 0:
                done = True

    print()
    print(f'总共过去的时间: {et():.1f}')


if __name__ == '__main__':
    main()
