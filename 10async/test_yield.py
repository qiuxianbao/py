"""
子程序调用是通过栈实现的，一个线程就是执行一个子程序。子程序调用总是一个入口，一次返回，调用顺序是明确的。

协程（coroutine），看上去也是子程序，但执行过程中，在子程序内部可中断，然后转而执行别的子程序，在适当的时候再返回来接着执行。
协程的特点在于是一个线程执行。

Python对协程的支持是通过generator实现的
"""


def consumer():
    """
    consumer() 是一个 generator 函数
    1.因为函数内部有 yield 关键
    2.调用 consumer() 不会执行函数体，而是返回一个 generator 对象

    它可以被 send()、next() 等方法控制
    可以暂停（在 yield 处）和恢复执行ss
    :return:
    """
    r = ''
    while True:
        n = yield r  # consumer 通过 yield 拿到消息，处理，又通过 yield 把结果传回
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    """
    producer (生产者)          consumer (消费者/generator)
    |                           |
    |-- c.send(None) --------> |  启动协程
    |                          |  执行到 yield r，暂停
    |                           |
    |-- c.send(1) -----------> |  发送 n=1
    |                          |  打印 "Consuming 1..."
    |<-- return '200 OK' ----- |  返回 '200 OK'
    |                           |
    |-- c.send(2) -----------> |  发送 n=2
    |                          |  打印 "Consuming 2..."
    |<-- return '200 OK' ----- |  返回 '200 OK'
    |                           |
    ... (重复 5 次)

    :param c:
    :return:
    """
    c.send(None)  # 启动 generator <generator object consumer at 0x0000013381FB4E40>，让它运行到第一个 yield，
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)  # 通过 c.send(n) 切换到 consumer 执行
        print('[PRODUCER] Consumer return: %s' % r)
    # 关闭consumer
    c.close()


def _main():
    c = consumer()
    produce(c)


if __name__ == '__main__':
    _main()
