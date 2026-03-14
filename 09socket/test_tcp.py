"""
网络通信是两台计算机上的两个进程之间的通信
Socket是网络编程的一个抽象概念。通常我们用一个Socket表示“打开了一个网络链接”，而打开一个Socket需要知道目标计算机的IP地址和端口号，再指定协议类型即可

"""
import socket
from pathlib import Path

current_dir = Path(__file__).parent


def test_client():
    # 创建一个socket:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 建立连接:
    s.connect(('www.baidu.com', 80))
    s.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')

    # 接收数据:
    buffer = []
    while True:
        # 每次最多接收1k字节:
        d = s.recv(1024)
        if d:
            buffer.append(d)
        else:
            break
    data = b''.join(buffer)
    # 关闭连接:
    s.close()

    # 只分割1次（找到第一个 \r\n\r\n 就停止）
    header, html = data.split(b'\r\n\r\n', 1)
    print(header.decode('utf-8'))
    # 把接收的数据写入文件
    with open(current_dir.joinpath('baidu.html'), 'wb') as f:
        f.write(html)


def _main():
    test_client()


if __name__ == '__main__':
    _main()
