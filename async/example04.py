"""
一个简单的状态机在Python中有延迟影响

"""
import gevent
from gevent import monkey
monkey.patch_all()

import time
import queue
from elapsed_time import ET


def task(name, work_queue):
    while not work_queue.empty():
        count = work_queue.get()
        total = 0
        et = ET()
        for x in range(count):
            print(f'Task {name} running')
            time.sleep(1)
            total += 1
        print(f'Task {name} total: {total}')
        print(f'Task {name} total elapsed time: {et():.1f}')


def main():
    """
    This is the main entry point for the programWhen
    """
    # create the queue of 'work'
    work_queue = queue.Queue()

    # put some 'work' in the queue
    for work in [15, 10, 5, 2]:
        work_queue.put(work)

    # run the tasks
    et = ET()
    tasks = [
        gevent.spawn(task, 'One', work_queue),
        gevent.spawn(task, 'Two', work_queue)
    ]
    gevent.joinall(tasks)
    print()
    print(f'Total elapsed time: {et():.1f}')


if __name__ == '__main__':
    main()
