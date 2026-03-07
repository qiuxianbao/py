import os


def test_os():
    print(os.name)  # nt

    # 环境变量
    print(os.environ)
    # print(os.environ.get('PATH'))
    # print(os.environ.get('key', 'default'))

    """
    查看当前目录的绝对路径
    返回的绝对路径会精确到你当前所在的最后一级文件夹
    """
    path = os.path.abspath('.')
    print(path)  # C:\VsCode\py

    test_dir = os.path.join(path, 'testdir')
    print(test_dir)

    if (not os.path.exists(test_dir)):
        os.mkdir(test_dir)

    #
    test_file = os.path.join(test_dir, 'file.txt')
    print(os.path.split(test_file))  # ('/Users/michael/testdir', 'file.txt')
    print(os.path.splitext(test_file))  # ('/Users/michael/testdir/file', '.txt')


    if (not os.path.exists(test_file)):
        with open(test_file, 'w') as f:
            f.write('Hello World')

    os.remove(test_file)
    os.rmdir(test_dir)

    #
    print([x for x in os.listdir('.') if os.path.isdir(x)])
    print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])


def _main():
    test_os()


if __name__ == '__main__':
    _main()
