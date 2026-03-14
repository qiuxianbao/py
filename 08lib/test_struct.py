import struct


def test_struct():
    # pack 函数把任意【数据类型】变成 bytes

    """
    >I' 的意思是表示字节顺序是 big-endian，也就是网络序， I 表示4字节无符号整数
    """
    print(struct.pack('>I', 10240099))

    # 后面的 bytes 依次变为 I ：4字节无符号整数和 H ：2字节无符号整数
    print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))



def _main():
    test_struct()


if __name__ == '__main__':
    _main()
