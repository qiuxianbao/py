"""
ThreadLocal 最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，
这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。
"""

import threading


def test_threadlocal():
    """
    线程间传递变量
    可以理解为全局变量 local_school 是一个 dict

    创建全局ThreadLocal对象
    """
    local_school = threading.local()

    def process_student():
        # 获取当前线程关联的student
        print('Hello, %s (in %s)' % (local_school.student, threading.current_thread().name))

    def process_thread(name):
        # 绑定ThreadLocal的student
        local_school.student = name
        process_student()

    t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
    t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')

    t1.start()
    t2.start()

    t1.join()
    t2.join()


def _main():
    test_threadlocal()


if __name__ == '__main__':
    _main()
