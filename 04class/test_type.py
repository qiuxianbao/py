#
import types
from class_extend import Animal
from class_extend import Dog


def test_attr():
    """
    测试该对象的属性
    """
    d = Dog()
    print(hasattr(d, 'run'))

    print(hasattr(d, 'eat'))
    setattr(d, 'eat', 'eat')

    print(hasattr(d, 'eat'))
    print(getattr(d, 'eat'))


def test_dir():
    """
    获取一个对象的所有属性和方法
    :return:
    ['__add__', '__class__', '__contains__', '__delattr__',
    '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
    '__getattribute__', '__getitem__', '__getnewargs__', '__gt__',
    '__hash__', '__init__', '__init_subclass__', '__iter__',
    '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__',
    '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__',
    '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
    'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs',
    'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii',
    'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace',
     'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition',
     'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition',
     'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase',
     'title', 'translate', 'upper', 'zfill']
    """
    print(dir("ABC"))


def test_instance():
    """
    判断class的类型

    :return:
    """
    d = Dog()

    print(isinstance(d, Dog))
    print(isinstance(d, Animal))

    print(type(d))  # <class 'sub_class.Dog'>

    # 基础类型
    print(isinstance(fn, types.FunctionType))

    # 判断一个变量是否是某些类型中的一种
    print(isinstance([1, 2, 3], (list, tuple)))
    print(isinstance((1, 2, 3), (list, tuple)))


def test_type():
    """
    判断对象类型

    :return:
    """

    # print(type(abs))  # <class 'builtin_function_or_method'>

    # <class 'function'>
    print(type(fn) == types.FunctionType)  # True
    print(type(fn) == types.BuiltinFunctionType)  # False
    print(type(abs) == types.BuiltinFunctionType)  # True

    print(type(lambda x: x) == types.LambdaType)  # True
    print(type((x for x in range(10))) == types.GeneratorType)  # True


def fn(self, name='world'):
    print('Hello, %s.' % name)


def test_type_create_obj():
    """
    type()函数既可以返回一个对象的类型，又可以创建出新的类型

    依次可以传入3个参数
    1.class的名称
    2.继承的父类集合
    3.class的方法名称与函数绑定

    说明:
    Python解释器遇到class定义时，扫描一下class定义的语法，也是调用 type() 函数创建出class
    type() 函数也允许我们动态创建出类来，也就是说，动态语言本身支持运行期动态创建类

    """
    Hello = type('Hello', (object,), dict(say=fn))  # 创建Hello class
    h = Hello()
    h.say()


def _main():
    # test_type()
    test_type_create_obj()
    # test_instance()
    # test_dir()
    # test_attr()


if __name__ == '__main__':
    _main()
