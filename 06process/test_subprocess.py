# subprocess 模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
import subprocess


def test_call():
    print('$ nslookup 127.0.0.1')
    r = subprocess.call(['nslookup', '127.0.0.1'])
    print('Exit code:', r)


def test_communicate():
    """
    相当于手动输入一下命名

    PS C:\Users\admin> nslookup
    默认服务器:  UnKnown
    Address:  fec0:0:0:ffff::1

    > set q=mx
    > 127.0.0.1
    服务器:  UnKnown
    Address:  fec0:0:0:ffff::1

    *** UnKnown 找不到 127.0.0.1: No response from server
    > exit
    :return:
    """
    print('$ nslookup')

    p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    output, err = p.communicate(b'set q=mx\n127.0.0.1\nexit\n')
    print(output.decode('utf-8'))
    print('Exit code:', p.returncode)


def _main():
    # test_call()
    test_communicate()


if __name__ == '__main__':
    _main()
