# 用于操作迭代对象的函数
import itertools


def test_count():
    """
    无限迭代器
    从1开始
    """
    for n in itertools.count(1):
        if n > 10:
            break
        print(n)


def test_cycle():
    """
    循环迭代
    """
    cs = itertools.cycle('ABC')  # 注意字符串也是序列的一种
    for c in cs:
        print(c)


def test_repeat():
    """
    重复迭代，限定重复次数
    """
    for n in itertools.repeat('A', 3):
        print(n)


def test_takewhile():
    """
    取出有限序列
    """
    natuals = itertools.count(1)
    ns = itertools.takewhile(lambda x: x <= 10, natuals)
    print(list(ns))


def test_chain():
    for c in itertools.chain('ABC', 'XYZ'):
        print(c)


def test_groupby():
    for key, group in itertools.groupby('AaABBBCCAAA', lambda c: c.upper()):
        print(key, list(group))


def _main():
    # test_count()
    # test_cycle()
    # test_repeat()
    # test_takewhile()
    test_chain()
    test_groupby()


if __name__ == '__main__':
    _main()
