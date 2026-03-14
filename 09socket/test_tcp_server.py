import socket
import threading
import time


def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')

    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)


def test_server():
    """
    客户端程序运行完毕就退出了，而服务器程序会永远运行下去，必须按Ctrl+C退出程序
    :return:
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #
    s.bind(('127.0.0.1', 8888))

    # 监听端口号
    # help(s.listen)  # 知识点：查看参数的含义
    s.listen(5)  # 最大连接数

    print('Waiting for connection...')

    while True:
        # 接受一个新连接:
        sock, addr = s.accept()
        # 创建新线程来处理TCP连接:
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()


def _main():
    test_server()


if __name__ == '__main__':
    _main()
