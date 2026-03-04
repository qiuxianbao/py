class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        """
        动态属性
        :param path:
        :return:
        """
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        """
        支持for ... in 循环，类似list或tuple那样，就必须实现一个 __iter__() 方法，该方法返回一个迭代对象
        然后，Python的for循环就会不断调用该迭代对象的__next__() 方法拿到循环的下一个值，直到遇到 StopIteration 错误时退出循环
        :return:
        """
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        # Python中的赋值顺序是从右到左
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值

    def __getitem__(self, n):

        if isinstance(n, int):  # n是索引
            """
            支持 list[0]这种方式取单个值
            :param n:
            :return:
            """
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a

        if isinstance(n, slice):  # n是切片
            """
            支持 list[0:1] 这种方式取切片
            :param n:
            :return:
            """
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


class Student(object):
    def __init__(self, name):
        """
        实例方法
        :param name:
        """
        self.name = name

    def __len__(self):
        """
        len() 调用的是 __len__()
        :return:
        """
        return 1000

    def __str__(self):
        """
        print() 调用的是 __str__() ，交互环境下调用的是 __repr__()

        在 Python交互环境下，s显示的还是地址
        >> from class_feature import Student
        >> s = Student('Michael')
        >> s
        <class_feature.Student object at 0x00000219B1E6E560>

        :return:
        """
        return 'Student object (name: %s)' % self.name

    """
    调试方法
    """
    __repr__ = __str__


    def __getattr__(self, attr):
        """
        只有在没有找到属性的情况下，才调用 __getattr__ ，
        :param attr:
        :return:
        """
        if attr == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

    def __call__(self):
        """
        直接在实例本身上调用
        :return:
        """
        print('My name is %s.' % self.name)


def test_len():
    s = Student('Michael')
    print(len(s))


def test_str():
    s = Student('Michael')
    print(s)


def test_getattr():
    s = Student('Michael')
    print(s.name)
    print(s.age())
    # print(s.score)

    print(Chain("baidu.com").status.user.timeline.list)


def test_iter():
    for n in Fib():
        print(n)


def test_getitem():
    print(Fib()[2])
    print(Fib()[0:5])


def test_call():
    s = Student('Michael')
    s()


def test_callable():
    print(callable(Student("lisi")))  # True
    print(callable(max))  # True
    print(callable([1, 2, 3]))  # False
    print(callable(None))  # False
    print(callable('str'))  # False


def _main():
    # 支持len()
    # test_len()

    # 对象可视化
    # test_str()
    # test_call()
    # test_getattr()

    # 迭代器
    # test_iter()
    # test_getitem()

    test_callable()

if __name__ == '__main__':
    _main()
