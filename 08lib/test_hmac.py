"""
通常我们计算MD5时采用 md5(message + salt) 。
但实际上，把salt看做一个“口令”，加salt的哈希就是：计算一段message的哈希时，根据不同口令计算出不同的哈希。
要验证哈希值，必须同时提供正确的口令

这实际上就是Hmac算法：Keyed-Hashing for Message Authentication
它通过一个标准算法，在计算哈希的过程中，把key混入计算过程中
"""
import hmac


def test_hmac():
    message = b'Hello, world!'
    key = b'secret'

    h = hmac.new(key, message, digestmod='MD5')
    # fa4ee7d173f2d97ee79022d1a7355bcf
    print(h.hexdigest())

    message = b'Hello'
    key = b'secret'

    h = hmac.new(key, message, digestmod='MD5')
    # 数据长可以使用update操作
    h.update(b', world!')
    print(h.hexdigest())


def _main():
    test_hmac()


if __name__ == '__main__':
    _main()
