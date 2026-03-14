"""
哈希算法又称摘要算法、散列算法。
它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）
目的是为了发现原始数据是否被人篡改过。

常见算法：
MD5，SHA1等等

应用场景：
密码等明文加盐加密成密文

"""
import hashlib


def test_md5():
    """
    MD5是最常见的哈希算法，速度很快，生成结果是固定的128 bit/16字节，通常用一个32位的16进制字符串表示。
    :return:
    """
    md5 = hashlib.md5()
    md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
    # d26a53750bc40b38b65a520292f69306
    print(md5.hexdigest())

    # 数据长可以多次调用
    md5 = hashlib.md5()
    md5.update('how to use md5 in '.encode('utf-8'))
    md5.update('python hashlib?'.encode('utf-8'))
    print(md5.hexdigest())


def test_sha1():
    """
    SHA1的结果是160 bit/20字节，通常用一个40位的16进制字符串表示
    比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，而且哈希长度更长
    :return:
    """
    sha1 = hashlib.sha1()
    sha1.update('how to use sha1 in '.encode('utf-8'))
    sha1.update('python hashlib?'.encode('utf-8'))
    # 2c76b57293ce30acef38d98f6046927161b46a44
    print(sha1.hexdigest())


def _main():
    # test_md5()
    test_sha1()


if __name__ == '__main__':
    _main()
