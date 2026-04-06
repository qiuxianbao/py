# collections 是Python内建的一个集合模块，提供了许多有用的集合类
import argparse
import os
from collections import namedtuple, deque, Counter, defaultdict, OrderedDict, ChainMap
from typing import Dict


def test_name_tuple():
    # p = (1, 2)
    # print(type(p))

    """
    namedtuple 是一个函数，它用来创建一个自定义的 tuple 对象，并且规定了 tuple 元素的个数，
    并可以用属性而不是索引来引用 tuple 的某个元素

    定义一个坐标，定义一个 class 又小题大做了
    :return:
    """
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(1, 2)
    print(type(p))  # <class '__main__.Point'>

    print(isinstance(p, Point))
    print(isinstance(p, tuple))


def test_deque():
    """
    双向列表，适合用于队列和栈
    :return:
    """
    q = deque(['a', 'b', 'c'])
    q.append('x')
    q.appendleft('y')

    print(q)


class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        # 知识点：调用父类构造函数的标准方式之一，Python2写法
        # super(LastUpdatedOrderedDict, self).__init__()
        super().__init__()
        self._capacity = capacity

    """
    这是 Python 的魔术方法，当你执行 dict[key] = value 时会自动调
    """

    def __setitem__(self, key, value):
        """
        实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key
        """
        containsKey = 1 if key in self else 0

        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)

        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))

        OrderedDict.__setitem__(self, key, value)


def test_dict():
    d = {'a': 1}
    print(d['a'])

    # KeyError: 'b'， Key不存在会报错
    # print(d['b'])

    """
    defaultdict 是一个 dict 的子类，在访问一个不存在的 key 的时候会返回一个默认值
    :return:
    """
    dd = defaultdict(lambda: 'N/A')
    dd['key1'] = 'abc'

    print(dd['key1'])
    print(dd['key2'])

    """
    OrderedDict的Key是有序的
    Key会按照插入的顺序排列，不是Key本身排序
    """
    od = OrderedDict([('a', 1), ('c', 2), ('b', 3)])
    print(od)


def test_counter():
    """
    统计字符出现的次数
    :return:
    """
    c = Counter('programming')
    print(c)

    c.update('hello')
    print(c)


def majority_vote_cn(votes: Dict[str, str]) -> tuple[str, int]:
    """中文版多数投票统计"""
    if not votes:
        return "无人", 0

    vote_counts = Counter(votes.values())  # 投票
    most_voted = vote_counts.most_common(1)[0]

    return most_voted[0], most_voted[1]


def test_counter_most_common():
    votes = {
        "张三": "Python",
        "李四": "Java",
        "王五": "Python",
        "赵六": "Go",
        "孙七": "Python",
        "周八": "Java"
    }
    print(majority_vote_cn(votes))


def test_last_updated_ordered_dict():
    fifo_dict = LastUpdatedOrderedDict(3)
    fifo_dict['a'] = 1
    fifo_dict['b'] = 2
    fifo_dict['c'] = 3

    print(fifo_dict)

    # 现在容量满了
    fifo_dict['d'] = 4

    # remove: ('a', 1)  ← 删除最旧的 'a'
    # add: ('d', 4)
    # 结果：{'b': 2, 'c': 3, 'd': 4}
    print(fifo_dict)

    # 先删除 'b' 再添加，'b' 变最新
    fifo_dict['b'] = 20
    # 结果：{'c': 3, 'd': 4, 'b': 20}
    print(fifo_dict)


def test_chain_map():
    # 构造缺省参数:
    defaults = {
        'color': 'red',
        'user': 'guest'
    }

    # 构造命令行参数:
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--user')
    parser.add_argument('-c', '--color')
    namespace = parser.parse_args()
    command_line_args = {k: v for k, v in vars(namespace).items() if v}

    # 组合成ChainMap:
    combined = ChainMap(command_line_args, os.environ, defaults)

    """
    打印参数:
    
    (py) PS C:\VsCode\py> uv run .\08lib\test_collections.py
    color=red
    user=guest
    
    (py) PS C:\VsCode\py> uv run .\08lib\test_collections.py -u lisi
    color=red
    user=lisi
    """
    print('color=%s' % combined['color'])
    print('user=%s' % combined['user'])


def _main():
    # test_name_tuple()
    # test_deque()
    # test_dict()
    # test_chain_map()
    # test_last_updated_ordered_dict()
    # test_counter()
    test_counter_most_common()


if __name__ == '__main__':
    _main()
