"""
线程

多线程模式通常比多进程快一点，但是也快不到哪去，
而且，多线程模式致命的缺点就是任何一个线程挂掉都可能直接造成整个进程崩溃，因为所有线程共享进程的内存。

在Windows上，如果一个线程执行的代码出了问题，你经常可以看到这样的提示：“该程序执行了非法操作，即将关闭”，其实往往是某个线程出了问题，但是操作系统会强制结束整个进程。

在Windows下，多线程的效率比多进程要高，所以微软的IIS服务器默认采用多线程模式。
由于多线程存在稳定性的问题，IIS的稳定性就不如Apache。

"""
import threading
import time


def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


def test_thread():
    # MainThread
    print('thread %s is running...' % threading.current_thread().name)

    t = threading.Thread(target=loop, name='LoopThread')

    t.start()
    t.join()
    print('thread %s ended.' % threading.current_thread().name)


# 假定这是你的银行存款
balance = 0
lock = threading.Lock()


def change_it(n):
    """
    先存后取，结果应该为0

    非正常顺序执行

    初始值 balance = 0
    t1: x1 = balance + 5 # x1 = 0 + 5 = 5
    t2: x2 = balance + 8 # x2 = 0 + 8 = 8
    t2: balance = x2 # balance = 8
    t1: balance = x1 # balance = 5

    t1: x1 = balance - 5 # x1 = 5 - 5 = 0
    t1: balance = x1 # balance = 0

    t2: x2 = balance - 8 # x2 = 0 - 8 = -8
    t2: balance = x2 # balance = -8

    结果 balance = -8

    :param n:
    :return:
    """
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    """
    锁的好处就是确保了某段关键代码只能由一个线程从头到尾完整地执行。
    坏处当然也很多，首先是阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了。

    其次，由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁，
    导致多个线程全部挂起，既不能执行，也无法结束，只能靠操作系统强制终止

    :param n:
    :return:
    """
    for i in range(10000000):
        # 获取锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            # 释放锁
            lock.release()


def test_lock():
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print(balance)


def _main():
    # test_thread()
    test_lock()


if __name__ == '__main__':
    _main()
