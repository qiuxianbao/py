import functools
from functools import reduce
from operator import itemgetter

def test_functools_partial():
    """
    偏函数
    functools.partial 的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数

    场景：
    当函数的参数个数太多，需要简化时，使用 functools.partial 可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
    :return:
    """
    int2 = functools.partial(int, base=2)
    print(int2('100'))


def int2(x, base=2):
    """
    二进制数转10进制

    :param x:
    :param base:
    :return:
    """
    # base 默认是10进制
    return int(x, base)


def log_enhance(text):
    """
    知识点：三层嵌套
    :param text:
    :return:
    """
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


def log(func):
    """
    知识点：日志装饰器
    :param func:
    :return:
    """
    @functools.wraps(func)  # 没有这句话，会丢失函数名。调用 now.__name__ 函数名变为 wrapper
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper



"""
知识点：装饰器
"""
@log    # 相当于 now = log(now)
@log_enhance('execute') # 相当于 now = log('execute')(now)
def now():
    print('2026-02-24')



def anonymous_lambda_func():
    """
    匿名函数
    关键字 lambda 表示匿名函数，冒号前面的 x 表示函数参数
    :return:
    """
    print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


def test_return_count_func():
    f1, f2, f3 = return_count_func()

    # 全部都是 9 ！原因就在于返回的函数引用了变量 i ，但它并非立刻执行。等到3个函数都返回
    # 时，它们所引用的变量 i 已经变成了 3 ，因此最终结果为 9
    print(f1())  # 9
    print(f2())  # 9
    print(f3())  # 9


def return_count_func(*args):
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


def test_return_sum_func():
    sum = return_sum_func(1, 2, 3, 4, 5)
    print(sum)  # <function return_sum_func.<locals>.sum at 0x0000020A2D4130A0>

    # 调用函数时，才真正计算求和的结
    print(sum())


def return_sum_func(*args):
    """
    闭包是指当一个函数返回了一个函数后，其内部的局部变量还被新函数引用
    返回的函数并没有立即执行，而是直到被调用才会执行
    :return:
    """

    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    # 返回的是函数
    return sum


def test_sorted():
    print(sorted([36, 5, -12, 9, -21]))

    # (projects) PS C:\VsCode> python -c 'help(sorted)'
    print(sorted([36, 5, -12, 9, -21], key=abs))

    # 按照小写字母排序
    l = ['bob', 'about', 'Zoo', 'Credit']
    print(sorted(l, key=str.lower))
    print(sorted(l, key=str.lower, reverse=True))

    # 元组排序
    students = [("Bob", 75), ("Adam", 92), ("Bart", 66), ("Lisa", 88)]

    print(sorted(students, key=lambda t: t[1]))
    print(sorted(students, key=itemgetter(0)))
    print(sorted(students, key=itemgetter(1), reverse=True))


def test_primes(limit=100):
    """
    打印指定范围内的素数
    :param limit: 上限值
    :return: None
    """
    print(f"小于 {limit} 的素数：")
    for prime in primes():
        if prime < limit:
            print(prime, end=' ')
        else:
            break


def primes():
    """
    生成素数序列
    :return: 素数生成器
    """

    # 当执行到 yield 语句时，函数会暂停执行并返回值
    # 下次调用 next() 或迭代时，从上次暂停的位置继续执行
    # 这不是线程中断，而是协程式的协作式多任务
    yield 2  # 2是第一个素数
    it = _odd_iter()  # 从3开始的奇数序列

    while True:
        n = next(it)  # 获取下一个候选数
        yield n
        # 用当前找到的素数n过滤掉所有n的倍数
        it = filter(_not_divisible(n), it)


def _not_divisible(n):
    return lambda x: x % n > 0


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def test_filter():
    """
    用于过滤序列
    和 map() 不同的是， filter() 把传入的函数依次作用于每个元素，然后根据返回值是 True 还是 False 决定保留还是丢弃该元素

    :return:
    """
    return list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))


def is_odd(n):
    return n % 2 == 1


DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int_lambda(s):
    def char2num(s):
        return DIGITS[s]

    # f = (lambda x, y: x * 10 + y)
    # print(type(f))  # <class 'function'>
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return DIGITS[s]

    return reduce(fn, map(char2num, s))


def test_reduce():
    """
    汇总累积
    reduce 把结果继续和序列的下一个元素做累积计算
    :return:
    """
    print(reduce(reduce_func, [1, 3, 5, 7, 9]))


def reduce_func(x, y):
    return x * 10 + y


def test_map():
    """
    各自计算
    将传入的函数依次作用到序列的每个元素

    第1个参数是 func
    第2个参数是 *iterables
    :return:
    """

    r = map(map_func, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(type(r))  # <class 'map'>
    print(r)  # <map object at 0x000001D869DE4160>

    print(list(r))  # [1, 4, 9, 16, 25, 36, 49, 64, 81]


def map_func(x):
    return x * x


def _main():
    # test_map()
    # test_reduce()

    # print(str2int('13579'))
    # print(str2int_lambda('13579'))

    # print(test_filter())
    # test_primes(100)

    # test_sorted()

    # test_return_sum_func()
    # test_return_count_func()

    # anonymous_lambda_func()

    # print(now)
    # now()

    #
    # print(now.__name__)

    print(int2('100'))
    test_functools_partial()

    pass


if __name__ == '__main__':
    _main()
