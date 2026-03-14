# chardet 是 Python 的字符编码检测库
import chardet


def test_charset_detect():

    # {'encoding': 'ascii', 'confidence': 1.0, 'language': ''}
    print(chardet.detect(b'Hello, world!'))

    # {'encoding': 'GB2312', 'confidence': 0.7407407407407407, 'language': 'Chinese'}
    data = '离离原上草，一岁一枯荣'.encode('gbk')
    print(chardet.detect(data))

    # {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
    data = '离离原上草，一岁一枯荣'.encode('utf-8')
    print(chardet.detect(data))

    # {'encoding': 'EUC-JP', 'confidence': 0.99, 'language': 'Japanese'}
    data = '最新の主要ニュース'.encode('euc-jp')
    print(chardet.detect(data))


def _main():
    test_charset_detect()


if __name__ == '__main__':
    _main()
