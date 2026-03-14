"""
Base64是一种用64个字符来表示任意二进制数据的方法
Base64是一种最常见的二进制编码方法

场景：
Base64适用于小段内容的编码，比如数字证书签名、Cookie的内容

--
原理：
原始字节  →  先补0凑满6bit的倍数  →  每6bit查表得1个字符  →  末尾补=

补位：
字节数是3的倍数，无需补
剩余 2 个字节，补 1 个 =
剩余 1 个字节，补 2 个 =


Base64 使用以下 64 个字符作为编码表：
索引	    字符
0-25	A-Z
26-51	a-z
52-61	0-9
62	    +
63	    /

说明：
每 6 bit 能表示一个Base64编码，64bit = 2^6 = 6 bit
1个字节是 8 bit
取 6 和 8 的最小公倍数： 2*3*2*2=24 bit

24bit
按字节:		24 / 8 = 3 组
按Base64:	24 / 6 = 4 组
"""
import base64


def test_binary():
    # 知识点：获取 'M' 的 ASCII 码
    print(ord('M'))  # 输出: 77
    # 转换为二进制
    # print(bin(ord('M')))      # 输出: 0b1001101
    # 格式化为 8 位二进制
    print(f"{ord('M'):08b}")  # 输出: 01001101

    # 查看字符串二进制
    text = 'Man'
    # 转换为字节
    byte_data = text.encode('utf-8')
    print(byte_data)  # b'Man' = 字节数组 ＝ 二进制 str

    for byte in byte_data:
        print(f"{byte:08b}")

    #
    s = "中"
    print(len(s.encode("utf-8")))  # 3，1个汉字3个字节
    print(len(s.encode("gbk")))  # 2
    print(len(s.encode("utf-16-be")))  # 2

    c = 'c'
    print(len(c.encode("utf-8")))  # 1，1个英文2个字节
    print(len(c.encode("gbk")))  # 1
    print(len(c.encode("utf-16-be")))  # 2


def test_b64():
    """
    情况一：字节数恰好是 3 的倍数（无需补=）
    以 "Man" 为例（3字节）：

        M          a          n
    01001101   01100001   01101110
    └────────────────────────────┘
              24 bit，÷6 = 4组

    010011  010110  000101  101110
      19      22      5       46
      T       W       F       u

    结果：TWFu   （无需补=）
    """
    # b'str' 可以表示字节
    encode = base64.b64encode(b'Man')
    print(encode)
    # print(base64.b64decode(encode))

    """
    情况二：剩余 2 个字节，补 1 个 =
    以 "Ma" 为例（2字节 = 16bit）：

        M          a
    01001101   01100001
    └──────────────────┘
        16 bit
    
    16 bit ÷ 6 = 2组余4bit
    → 末尾补2个0，凑成18bit（6的倍数，变成3组）
    
    010011  010110  000100
      19      22      4
      T       W       E
    
    3个字符 + 1个= → TWE=
    """
    encode = base64.b64encode(b'Ma')
    print(encode)
    # print(base64.b64decode(encode))

    """
    情况三：剩余 1 个字节，补 2 个 =
    以 "M" 为例（1字节 = 8bit）：

        M
    01001101
    └────────┘
       8 bit
    
    8 bit ÷ 6 = 1组余2bit
    → 末尾补4个0，凑成12bit（6的倍数，变成2组）
    
    010011  010000
      19      16
      T       Q
    
    2个字符 + 2个= → TQ==
    """
    encode = base64.b64encode(b'M')
    print(encode)
    # print(base64.b64decode(encode))


def test_b64_urlsafe():
    """
    由于标准的Base64编码后可能出现字符 + 和 / ，在URL中就不能直接作为参数
    所以又有一种"url safe"的base64编码，其实就是把字符 + 和 / 分别变成 - 和 _

    i 是可打印的 ASCII 字符
    x 表示 16进制
    """

    # b'abcd++//'
    print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))

    # b'abcd--__'
    print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))

    # b'i\xb7\x1d\xfb\xef\xff'
    print(base64.urlsafe_b64decode('abcd--__'))


def _main():
    # test_binary()
    # test_b64()
    test_b64_urlsafe()


if __name__ == '__main__':
    _main()
