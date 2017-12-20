"""
Python中一个简单的状态机

"""

import queue

def task(name, queue):
    while not queue.empty():
        count = queue.get()
        print("count:",count)
        total = 0
        for x in range(count):
            print(f'Task {name} running')
            total += 1
            print("total:",total)
            yield
        print(f'Task {name} total: {total}')

def main():
    # create the queue of 'work'
    work_queue = queue.Queue()

    # put some 'work' in the queue
    for work in [15, 10, 5, 2]:
        work_queue.put(work)

    # create some tasks
    tasks = [
        task('One', work_queue),
        task('Two', work_queue)
    ]

    # run the tasks
    done = False
    while not done:
        for t in tasks:
            try:
                next(t)

            except StopIteration:
                tasks.remove(t)
            if len(tasks) == 0:
                done = True


if __name__ == '__main__':
    main()














