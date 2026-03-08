# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程
import os
import random
import time
from multiprocessing import Pool


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


def _main():
    print('Parent process %s.' % os.getpid())

    # 同时跑4个进程
    p = Pool(4)
    for i in range(5):
        # p.apply(long_time_task, args=(i,))
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')

    """
    如果不调用p.close(), 直接调用p.join()会报 ValueError: Pool is still running
    """
    p.close()

    """
    对 Pool 对象调用 join() 方法会等待所有子进程执行完毕，
    调用 join() 之前必须先调用close() ，
    调用 close() 之后就不能继续添加新的 Process 了
    """
    p.join()

    print('All subprocesses done.')


if __name__ == '__main__':
    _main()
