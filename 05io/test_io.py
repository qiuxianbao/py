from pathlib import Path

current_dir = Path(__file__).parent


def test_bytes_io_r():
    """
    操作二进制数据
    :return:
    """
    from io import BytesIO

    f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
    text = f.read()

    print(text)
    print(text.decode("utf-8"))


def test_bytes_io_w():
    """
    操作二进制数据
    :return:
    """
    from io import BytesIO

    f = BytesIO()
    f.write('中文'.encode("utf-8"))

    print(f.getvalue())


def test_stringio_r():
    from io import StringIO

    f = StringIO('Hello!\nHi!\nGoodbye!')
    while True:
        s = f.readline()
        if s == '':
            break
        print(s.strip())


def test_stringio_w():
    from io import StringIO

    f = StringIO()
    f.write('hello')

    print('f.getvalue()', f.getvalue())


def _main():
    # test_stringio_w()
    # test_stringio_r()

    test_bytes_io_w()
    test_bytes_io_r()


if __name__ == '__main__':
    _main()
