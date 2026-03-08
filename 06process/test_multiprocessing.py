"""
多进程

多进程模式最大的优点就是稳定性高，因为一个子进程崩溃了，不会影响主进程和其他子进程。
（当然主进程挂了所有进程就全挂了，但是Master进程只负责分配任务，挂掉的概率低）著名的Apache最早就是采用多进程模式

多进程模式的缺点是创建进程的代价大，在Unix/Linux系统下，用 fork 调用还行，在Windows下创建进程开销巨大。
另外，操作系统能同时运行的进程数也是有限的，在内存和CPU的限制下，如果有几千个进程同时运行，操作系统连调度都会成问题。


是否采用多任务的第二个考虑是任务的类型: 我们可以把任务分为计算密集型和IO密集型
Python这样的脚本语言运行效率很低，完全不适合计算密集型任务。对于计算密集型任务，最好用C语言编写。

单线程的异步编程模型称为协程，有了协程的支持，就可以基于事件驱动编写高效的多任务程序。

--
在Thread和Process中，应当优选Process，因为Process更稳定，而且，Process可以分布到多
台机器上，而Thread最多只能分布到同一台机器的多个CPU上




"""

import os
import random
import time
from multiprocessing import Process, Queue


# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


def test_process():
    print('Parent process %s.' % os.getpid())
    # 创建子进程时，只需要传入一个执行函数和函数的参数
    p = Process(target=run_proc, args=('test',))

    print('Child process will start.')
    p.start()

    # join() 方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    p.join()
    print('Child process end.')


# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s, ppid: %s' % (os.getpid(), os.getppid()))
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s, ppid: %s' % (os.getpid(), os.getppid()))

    while True:
        """
        True是block参数，表示阻塞模式

        如果队列为空，调用会一直等待，直到有数据可用
        block=False：非阻塞模式。如果队列为空，立即抛出 queue.Empty 异常
        """
        value = q.get(True)
        print('Get %s from queue.' % value)


def test_queue():
    """
    进程间通信通过队列

    一个向队列中写数据，一个读数据
    :return:
    """
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))

    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()

    # 等待pw结束
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止
    pr.terminate()


def _main():
    # test_process()
    test_queue()


if __name__ == '__main__':
    _main()
