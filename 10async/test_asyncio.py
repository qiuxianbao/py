"""
多线程和多进程的模型虽然解决了并发问题，但是系统不能无上限地增加线程。
由于系统切换线程的开销也很大，所以，一旦线程数量过多，CPU的时间就花在线程切换上了，真正运行代码的时间就少了，结果导致性能严重下降。

我们要解决的问题是CPU高速执行能力和IO设备的龟速严重不匹配，多线程和多进程只是解决这一问题的一种方法。
另一种解决IO问题的方法是异步IO。

当代码需要执行一个耗时的IO操作时，它只发出IO指令，并不等待IO结果，然后就去执行其他代码了。
一段时间后，当IO返回结果时，再通知CPU进行处理。

说明：
对于大多数IO密集型的应用程序，使用异步IO将大大提升系统的多任务处理能力

#
asyncio可以实现单线程并发IO操作
asyncio 实现了TCP、UDP、SSL等协议

"""
import asyncio
import threading


async def hello(name):
    """
    async 把一个函数变成 coroutine 类型
    :return:
    """
    # 打印name和当前线程:
    print("Hello %s! (%s)" % (name, threading.current_thread))

    # 异步调用asyncio.sleep(1)
    # await 语法可以让我们方便地调用另一个async 函数
    await asyncio.sleep(1)

    print("Hello %s again! (%s)" % (name, threading.current_thread))
    return name


async def gather():
    """
    使用asyncio.gather()来并发执行多个任务
    :return:
    """
    L = await asyncio.gather(hello("Bob"), hello("Alice"))
    print(L)


def test_gather():
    asyncio.run(gather())


async def wget(host):
    print(f"wget {host}...")
    # 连接80端口:
    reader, writer = await asyncio.open_connection(host, 80)

    # 发送HTTP请求:
    header = f"GET / HTTP/1.0\r\nHost: {host}\r\n\r\n"
    writer.write(header.encode("utf-8"))

    await writer.drain()
    # 读取HTTP响应:
    while True:
        line = await reader.readline()
        if line == b"\r\n":
            break
        print("%s header > %s" % (host, line.decode("utf-8").rstrip()))

    # Ignore the body, close the socket
    writer.close()
    await writer.wait_closed()
    print(f"Done {host}.")


async def gather_web():
    await asyncio.gather(wget("www.sina.com.cn"), wget("www.sohu.com"),
                         wget("www.163.com"))


def test_gather_web():
    asyncio.run(gather_web())


def _main():
    test_gather()
    # test_gather_web()


if __name__ == '__main__':
    _main()
