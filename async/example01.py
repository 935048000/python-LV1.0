"""
任务的同步运行

"""

import queue

def task(name, work_queue):
    if work_queue.empty():
        print(f'Task {name} nothing to do')
    else:
        while not work_queue.empty():
            count = work_queue.get()
            total = 0
            for x in range(count):
                print(f'Task {name} running')
                total += 1
            print(f'Task {name} total: {total}')

def main():
    # 创建“工作”队列
    work_queue = queue.Queue()

    # 把一些“工作”放在队列中
    for work in [15, 10, 5, 2]:
        work_queue.put(work)

    # 创建一些任务
    tasks = [
        (task, 'One', work_queue),
        (task, 'Two', work_queue)
    ]

    # 运行的任务
    for t, n, q in tasks:
        t(n, q)

if __name__ == '__main__':
    main()















