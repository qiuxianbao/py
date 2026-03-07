from pathlib import Path

current_dir = Path(__file__).parent


def test_open_img():
    file_path = current_dir / 'test.png'

    # Read binary
    with open(file_path, 'rb') as f:
        print(f.read())  # b'\x89PNG...


def test_write_txt():
    file_path = current_dir / 'test.txt'
    with open(file_path, 'w') as f:
        # with open(file_path, 'a') as f:
        f.write('Hello World')


def test_open_txt():
    file_path = current_dir / 'test.txt'

    """
    简化版
    
    try:
        f = open(file_path, 'r')
        print(f.read())
    finally:
        if f:
            f.close()
            
    #
    像 open() 函数返回的这种有个 read() 方法的对象，在Python中统称为file-like Object
    """
    with open(file_path, 'r') as f:
        print(f.read())


def _main():
    test_open_txt()
    # test_write_txt()
    # test_open_img()


if __name__ == '__main__':
    _main()
