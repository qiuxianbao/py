# 分布式进程

import queue
import time
from multiprocessing.managers import BaseManager


# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass


def task_worker():
    # 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
    QueueManager.register('get_task_queue')
    QueueManager.register('get_result_queue')

    # 连接到服务器，也就是运行task_master.py的机器:
    server_addr = '127.0.0.1'
    print('Connect to server %s...' % server_addr)
    # 端口和验证码注意保持与 task_master.py设置的完全一致:
    manager = QueueManager(address=(server_addr, 5000), authkey=b'abc')

    # 从网络连接:
    manager.connect()

    # 获取 Queue 的对象:
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    print(f'Worker: connected to server, task queue size: {task.qsize()}')

    # 从 task 队列取任务，并把结果写入 result 队列:
    for i in range(10):
        try:
            n = task.get(timeout=5)  # 设置 5 秒超时
            print('run task %d * %d...' % (n, n))
            r = '%d * %d = %d' % (n, n, n * n)
            time.sleep(1)
            result.put(r)
        except queue.Empty:
            print('task queue is empty.')
            break  # 队列为空时退出循环
    # 处理结束:
    print('worker exit.')


def _main():
    task_worker()


if __name__ == '__main__':
    _main()
