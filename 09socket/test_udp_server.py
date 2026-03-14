"""
使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，就可以直接发数据包
不保证可靠传输

"""
import socket


def test_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('127.0.0.1', 9999))
    # 不需要监听
    print('Bind UDP on 9999...')

    while True:
        data, addr = s.recvfrom(1024)
        print('Received from %s:%s.' % addr)
        s.sendto(b'Hello, %s!' % data, addr)


def _main():
    test_server()


if __name__ == '__main__':
    _main()
