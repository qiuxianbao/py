# metaclass是类的模板，所以必须从`type`类型派生
class ListMetaclass(type):
    """
    __new__() 方法接收到的参数依次是
    1.当前准备创建的类的对象
    2.类的名字
    3.类继承的父类集合
    4.类的方法集合
    """

    def __new__(cls, name, bases, attrs):
        # 这个metaclass可以给我们自定义的MyList增加一个 add 方法
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


"""
当我们传入关键字参数 metaclass 时，
它指示Python解释器在创建 MyList时，要通过 ListMetaclass.__new__() 来创建，
在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义

ListMetaclass#__new__()会被自动调用

"""


class MyList(list, metaclass=ListMetaclass):
    pass


def test_metaclass():
    l = MyList()
    l.add(1)
    print(l)


def _main():
    test_metaclass()


if __name__ == '__main__':
    _main()
