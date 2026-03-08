# 分布式进程

"""
架构示意图：

┌─────────────────────────────────────────┐       │       ┌─────────────────────────────────────────┐
│         task_master.py                  │       │       │         task_worker.py                  │
│                                         │       │       │                                         │
│  task = manager.get_task_queue()        │       │       │  task = manager.get_task_queue()        │
│  result = manager.get_result_queue()    │       │       │  result = manager.get_result_queue()    │
│              ↓                          │       │       │              ↑                          │
│  ┌──────────────────────────┐           │       │       │              │                          │
│  │  QueueManager (服务端)    │◄──────────┴───────┴───────┘──────────────│                          │
│  │  ┌──────────┐ ┌────────┐ │           │       │       │                                         │
│  │  │task_queue│ │result_q│ │           │       │       │                                         │
│  │  └──────────┘ └──────── │           │       │       │                                         │
│  └──────────────────────────┘           │       │       │                                         │
│                                         │       │       │                                         │
│  端口：5000                             │       │       │  连接到：127.0.0.1:5000                 │
│  验证码：abc                            │       │       │  验证码：abc                            │
└─────────────────────────────────────────┘       │       └─────────────────────────────────────────┘
                                ↕  Network (localhost:5000)              ↕
"""

import queue
import random
from multiprocessing.managers import BaseManager


# 从 BaseManager 继承的 QueueManager:
class QueueManager(BaseManager):
    pass


# 定义任务队列和结果队列
task_queue = queue.Queue()
result_queue = queue.Queue()

"""
定义函数，为了解决 Windows环境无法被 pickle 序列化
定义在外面， 是因为局部函数无法 pickle
"""


def get_task_queue():
    """
    不能直接 return queue.Queue()
    否则，master和 worker 用的不是一个同一个queue
    :return:
    """
    # return queue.Queue()
    return task_queue


def get_result_queue():
    # return queue.Queue()
    return result_queue


def task_master():
    # 知识点：lambda无法解决pickle序列化问题
    # QueueManager.register('get_task_queue', callable=lambda: task_queue)
    # QueueManager.register('get_task_queue', callable=lambda: result_queue)

    QueueManager.register('get_task_queue', callable=get_task_queue)
    QueueManager.register('get_result_queue', callable=get_result_queue)

    # 绑定端口 5000, 设置验证码'abc':
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
    # 启动 Queue
    manager.start()

    # 获得通过网络访问的 Queue 对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    # 放几个任务进去
    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n)

    print(f'Master: task queue size after putting: {task.qsize()}')

    # 从 result 队列读取结果
    print('Try get results...')
    for i in range(10):
        r = result.get(timeout=100)
        print('Result: %s' % r)

    # 关闭:
    manager.shutdown()
    print('master exit.')


def _main():
    task_master()


if __name__ == '__main__':
    _main()
