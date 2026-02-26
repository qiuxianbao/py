import math




def named_kw_args(name, age, *, city):
    """
    命名关键字参数
    和关键字参数 **kw 不同，命名关键字参数需要一个特殊分隔符 *， * 后面的参数被视为命名关键字参数

    Python解释器把前两个参数视为位置参数，后两个参数传给 *args ，但缺少命名关键字参数导致报错

    说明：
    如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了

    :param name:
    :param age:
    :param city:
    :return:
    """
    print('name:', name, 'age:', age, 'city:', city)


def kw_args(name, age, **kw):
    """
    关键字参数
    而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个【dict】

    :param name:
    :param age:
    :param kw:
    :return:
    """
    print('name:', name, 'age:', age, 'other:', kw)


def variable_args(*numbers):
    """
    可变参数
    允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个【tuple】
    :param numbers:
    :return:
    """
    sum = 0
    print(type(numbers))  # <class 'tuple'>

    for n in numbers:
        sum = sum + n * n
        return sum


def add_end(L=None):
    """
    定义默认参数要牢记一点：默认参数必须指向不变对象！
    :param L:
    :return:
    """
    if L is None:
        L = []  # 每次调用进行初始化
    L.append('END')
    return L


def add_end0(L=[]):
    """
    现象：默认参数是 [] ，但是函数似乎每次都“记住了”上次添加了 'END' 后的list

    原因解释如下：
    Python函数在定义的时候，默认参数 L 的值就被计算出来了，即 [] ，因为默认参数 L 也是一个变量，它指向对象 [] ，
    每次调用该函数，如果改变了 L 的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的 [] 了。

    【特别注意】：
    定义默认参数要牢记一点：默认参数必须指向不变对象！
    :param L:
    :return:
    """
    L.append('END')
    return L


def default_value(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


def power(x, n=2):
    s = 1
    while n > 0:
        s *= x
        n -= 1
    return s


def multi_return(x, y, step, angle=0):
    """
    返回多个值

    :param x:
    :param y:
    :param step:
    :param angle:  默认值
    :return:
    """
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


def _call():
    # print(my_abs(-1))
    # print(my_abs('abc'))

    result = multi_return(100, 100, 60, math.pi / 6)
    print(type(result)) # <class 'tuple'>
    # print(result)

    # x^n
    # print(2**3)
    # print(power(5))
    # print(power(5, 3))

    # default_value('Michael', 'M', city='Beijing')  # 当不按顺序提供部分默认参数时，需要把参数名写上

    """
    默认参数是 []
    Python函数在定义的时候，默认参数 L 的值就被计算出来了，即 [] ，因为默认参数 L 也
是一个变量，它指向对象 [] ，每次调用该函数，如果改变了 L 的内容，则下次调用时，默认
参数的内容就变了，不再是函数定义时的 [] 了

    :return:
    """
    print(add_end0())
    print(add_end0())  # ['END', 'END']
    # print(add_end0())  # ['END', 'END', 'END']

    # print(add_end())  # 不可变对象
    # print(add_end())

    print(variable_args(1, 2, 3))

    nums = [1, 2, 3]
    # print(variable_params(nums))  # TypeError: can't multiply sequence by non-int of type 'list'
    print(variable_args(*nums))  # Python允许你在list或tuple前面加一个 * 号，把list或tuple的元素变成可变参数传进去


    # name: Michael age: 5 other: {'city': 'Beijing', 'gender': 'M'}
    kw_args('Michael', 5, city='Beijing', gender='M')


    extra = {'city': 'Beijing', 'job': 'Engineer'}
    """
    **extra 表示把 extra 这个dict的所有key-value用关键字参数传入到函数的 **kw 参数
    kw 将获得一个dict，注意 kw 获得的dict是 extra 的一份拷贝，对 kw 的改动不会影响到函数外的 extra
    """
    kw_args('Michael', 5, **extra)


    # named_kw_args('Michael', 5, 'Beijing')  # named_kw_args() takes 2 positional arguments but 3 were given
    named_kw_args('Michael', 5, city='Beijing')  #




    pass


if __name__ == '__main__':
    _call()
