"""
并不是只有 open() 函数返回的fp对象才能使用 with 语句
实际上，任何对象，只要正确实现了上下文管理，就可以用于 with 语句
"""
from contextlib import contextmanager
from urllib.request import urlopen


class Query0(object):
    """
    实现上下文管理是通过 __enter__ 和 __exit__ 这两个方法实现的
    """

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' % self.name)


def test_enter_exit():
    """
    Begin
    Query info about Bob...
    End
    """
    with Query0('Bob') as q:
        q.query()


class Query(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)


# 知识点：装饰器，类似aop
@contextmanager
def create_query(name):
    """
    通过 @contextmanager 装饰器来实现上下文管理是
    """
    q = Query(name)
    # 用 yield 语句把 with ... as var 把变量输出出去
    yield q
    print('End')


@contextmanager
def tag(name):
    """
    方法前后执行逻辑
    :param name:
    :return:
    """
    print("<%s>" % name)
    yield
    print("</%s>" % name)


def test_contextmanager():
    """
    Query info about Bob...
    End
    """
    with create_query('Bob') as q:
        q.query()

    """
    <h1>
    hello
    world
    </h1>
    """
    with tag('h1'):
        print('hello')
        print('world')


"""
是把任意对象变为上下文对象，并支持 with 语句
"""


@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()


def test_closing():
    with closing(urlopen('https://www.python.org')) as page:
        for line in page:
            print(line)


def _main():
    # test_enter_exit()
    # test_contextmanager()
    test_closing()


if __name__ == '__main__':
    _main()
