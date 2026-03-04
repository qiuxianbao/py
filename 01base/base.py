#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python的语法比较简单，采用缩进方式
import os
from typing import Iterable, Iterator


def immutable_object():
    a = 'abc'

    # Return a copy with all occurrences of substring old replaced by new.
    replace = a.replace('a', 'A')
    print(replace)  # Abc

    print(a)  # abc

    pass


def dict_set():
    """
    和list比较，dict有以下几个特点：
    1. 查找和插入的速度极快，不会随着key的增加而变慢；
    2. 需要占用大量的内存，内存浪费多

    而list相反：
    1. 查找和插入的时间随着元素的增加而增加；
    2. 占用空间小，浪费内存很少

    :return:
    """
    d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
    print(d['Michael'])

    d['Adam'] = 100
    print(d)

    print(d.get('Thomas', -1))
    print('Thomas' in d)

    # 删除
    d.pop('Adam')
    print(d)

    # 需要牢记的第一条就是dict的key必须是不可变对象
    key = [1, 2, 3]
    # d[key] = 'a list'  # TypeError: unhashable type: 'list'

    s = {1, 2, 3}
    print(s)

    l = [1, 2, 4, 3]
    s = set(l)  # list转set
    print(s)

    s.add(5)
    print(s)

    s.remove(5)
    print(s)

    # 集合运算
    s1 = {1, 2, 3}
    s2 = {2, 3, 4}
    print(s1 & s2)
    print(s1 | s2)
    print(s1 - s2)

    pass


def for_while():
    """

    :return:
    """
    names = ['Michael', 'Bob', 'Tracy']
    for name in names:
        print(name)

    # 整数序列
    r = range(5)
    print(type(r))  # <class 'range'>
    print(list(range(5)))

    sum = 0
    n = 99
    while n > 0:
        sum = sum + n
        n = n - 2
    print(sum)

    pass


def if_match():
    """
    :return:
    """
    score = 'B'
    if score == 'A':
        print('score is A.')
    elif score == 'B':
        print('score is B.')
    elif score == 'C':
        print('score is C.')
    else:
        print('invalid score.')

    score = 'E'
    match score:
        case 'A':
            print('score is A.')
        case 'B' | 'D':
            print('score is B|D.')
        case 'C':
            print('score is C.')
        case _:  # _表示匹配到其他任何情况
            print('score is ???.')

    # 复杂匹配
    args = ['gcc', 'hello.c', 'world.c']
    # args = ['clean']
    # args = ['gcc']
    match args:
        # 如果仅出现gcc，报错:
        case ['gcc']:
            print('gcc: missing source file(s).')
        # 出现gcc，且至少指定了一个文件:
        case ['gcc', file, *files]:
            print('gcc compile: ' + file + ', ' + ', '.join(files))
        # 仅出现clean:
        case ['clean']:
            print('clean')
        case _:
            print('invalid command.')

    pass


def list_tuple():
    """
    列表与元组
    list和tuple是Python内置的有序集合，一个可变，一个不可变
    :return:
    """
    classmates = ['Michael', 'Bob', 'Tracy']
    # print(classmates[-1])  # 最后1个
    # print(classmates[-2])  # 倒数第2个

    # 插入
    # classmates.append('Adam')
    # print(classmates)

    # 删除
    # classmates.pop()
    # print(classmates)

    # 指定位置插入
    # classmates.insert( 1, 'Adam')
    # print(classmates)

    # 指定位置删除
    # classmates.pop(2)
    # print(classmates)

    classmates[1] = 'Adam'
    # print(classmates)

    # list里面的元素的数据类型可以不同
    l = ['Apple', 123, True]
    # print(l)

    s = ['python', 'java', ['asp', 'php'], 'scheme']
    # print(s)

    # 元组
    # classmates这个tuple不能变了，它也没有append()，insert()这样的方法
    classmates = ('Michael', 'Bob', 'Tracy')
    # print(classmates[-1])

    # 单个元素
    t = (1,)
    print(type(t))  # <class 'tuple'>

    t = (1)
    print(type(t))  # <class 'int'>

    # 可变的tuple，引用不可变
    # 引用指向的对象是可以修改的
    t = ('a', 'b', ['A', 'B'])
    t[2][0] = 'X'
    t[2][1] = 'Y'
    print(t)

    pass


def list_slice():
    """
    知识点：切片
    :return:
    """
    L = list(range(100))  # 列表生成

    print(L[:3])  # 前3个
    print(L[-3:])  # 后3个
    print(L[-1])  # 最后1个

    print(L[:10:2])  # 每隔2个取一个（索引，包含头不包含尾）
    print(L[::5])  # 所有数，每5个取一个

    # 元组
    t = ('a', 'b', 'c', 'd')
    print(t[1:3])

    # 字符串（字符数组）
    str = 'ABCDEFG'
    print(str[:3])

    pass


def list_enumerable():
    l = [1, 2, 3, 4, 5]
    print(isinstance(l, Iterable))

    for i, value in enumerate(l):
        # print(str(i) + "=" + str(value))
        print(f"第{i}个元素是{value}")

    for x, y in [(1, 1), (2, 4), (3, 9)]:
        print(x, y)

    pass


def list_iterable():
    print(type([]))  # <class 'list'>
    print(isinstance([], Iterable))  # True

    print(type({}))  # <class 'dict'>
    print(isinstance({}, Iterable))  # True

    print(type('abc'))
    print(isinstance('abc', Iterable))  # True

    print(type((x for x in range(10))))  # <class 'generator'>
    print(isinstance((x for x in range(10)), Iterable))  # True

    print(type(100))
    print(isinstance(100, Iterable))  # False

    pass


def list_iterator():
    """
    迭代器： Iterator

    生成器不但可以作用于 for 循环，
    还可以被 next() 函数不断调用并返回下一个值，直到最后抛出 StopIteration 错误表示无法继续返回下一个值了。

    总结：
    1.凡是可作用于 for 循环的对象都是 Iterable 类型。
    2.凡是可作用于 next() 函数的对象都是 Iterator 类型，它们表示一个惰性计算的序列。

    :return:
    """
    print(isinstance((x for x in range(10)), Iterator))  # True

    print(type([]))  # <class 'list'>
    print(isinstance([], Iterator))  # False

    print(type({}))  # <class 'dict'>
    print(isinstance({}, Iterator))  # False

    print(type('abc'))
    print(isinstance('abc', Iterator))  # False

    # list, dict, str 转换成 Iterator 迭代器
    print(isinstance(iter([]), Iterator))
    print(isinstance(iter({}), Iterator))
    print(isinstance(iter('abc'), Iterator))

    pass


def list_gen():
    """
    列表生成式
    for前面的部分是一个表达式
    for后面的部分是筛选条件
    :return:
    """

    #
    l_double = [x * x for x in range(1, 11) if x % 2 == 0]
    # print(l_double)

    # 全排列
    p = [m + n for m in 'ABC' for n in 'XYZ']
    # print(p)

    dirs = [d for d in os.listdir('.')]
    # print(dirs)

    d = {'x': 'A', 'y': 'B', 'z': 'C'}

    for k, v in d.items():
        print(k, v)

    L = ['Hello', 'World', 'IBM', 'Apple']
    l_lower = [s.lower() for s in L]
    print(l_lower)


def list_generator():
    """
    生成器
    :return:
    """
    L = [x * x for x in range(10)]
    # print(type(L))  # <class 'list'>
    # print(L)

    g = (x * x for x in range(3))
    # print(type(g))  # <class 'generator'>
    # print(g)  # <generator object list_generator.<locals>.<genexpr> at 0x000001DB8F3F35E0>

    # next 每次获取一个值
    # print(next(g))  # 0
    # print(next(g))  # 1
    # print(next(g))  # 4
    # print(next(g))  # StopIteration

    # 使用for循环，因为generator也是可迭代对象
    # for i in g:
    #     print(i)

    #
    while True:
        try:
            x = next(g)
            print(x)
        except StopIteration as e:
            break

    pass


def list_generator_yield(max):
    """
    如果一个函数定义中包含 yield 关键字，那么这个函数就不再是一个普通函数，而是一个generator函数

    :param max:
    :return:
    """
    n, a, b = 0, 0, 1
    while n < max:
        # print(b)
        yield b
        # 同时赋值的经典用法
        # 右侧计算：先计算 b 和 a + b 的值
        # 左侧赋值：然后同时将这两个值分别赋给 a 和 b
        a, b = b, a + b
        n = n + 1

    return 'done'


def string():
    """
    字符串

    常见的占位符有：
    %d: 数字
    %s: 字符串
    %f: 浮点数
    %x: 16进制

    :return:
    """

    # 格式化整数和浮点数还可以指定是否补0和整数与小数的位数
    print('%2d-%02d' % (3, 1))
    print('%.2f' % 3.1415926)

    # 调试神器：在Vs Code、PyCharm、Jupyter编辑其中，【# %%】 可以把代码切成一块一块可单独执行的单元
    print('growth rate: %d %%' % 7)  # 转义%% 来表示1个 %

    # f-string
    r = 2.5
    s = 3.14 * r ** 2
    print(f'The area of a circle with radius {r} is {s:.2f}')

    incr = (85 - 72) / 72 * 100
    print(f'{incr:.1f}%')

    pass


def encode():
    """
    字符串和编码
    最早只有127个字符被编码到计算机里，也就是大小写英文字母、数字和一些符号，这个编码表被称为 【ASCII】 编码。
    比如大写字母 A 的编码是 65

    中国制定了 GB2312 编码，用来把中文编进去
    日本把日文编到 Shift_JIS 里
    ... 后来，【Unicode】把所有语言都统一到一套编码里。

    ASCII编码是1个字节，而Unicode编码通常是2个字节。

    为了节省空间，又出现了把Unicode编码转化为“可变长编码”的 【UTF-8】 编码
    UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节：
    常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节

    总结：
    在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。

    :return:
    """

    # ord() 函数获取字符的整数表示
    print(ord('A'))
    print(ord('中'))

    # chr() 函数把编码转换为对应的字符
    print(chr(65))
    print(chr(20013))

    # 编码
    # Python对 bytes 类型的数据用带 b(bytes) 前缀的单引号或双引号表示
    print('ABC'.encode('ascii'))  # 纯英文的 str 可以用 ASCII 编码为 bytes ，内容是一样的
    print('中文'.encode('utf-8'))  # 含有中文的 str 可以用 UTF-8 编码为 bytes

    # 解码
    print(b'ABC'.decode('ascii'))
    print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

    # 字符长度
    print(len('ABC'))
    # 字节长度
    print(len('ABC'.encode('ascii')))

    print(len('中文'))
    print(len('中文'.encode('utf-8')))

    pass


def data_type_varible():
    """
    数据类型和变量
    :return:
    """

    # 变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言
    a = 1  # a是整数
    a = "abc"  # a变为字符串

    # 常量
    # print(math.pi)

    # 地板除
    # print(10/3)
    print(10 // 3)  # 取整数部分

    s = r'Hello, "Bart"'  # r'' 表示 '' 内部的字符串默认不转义
    print(s)

    s = r'''Hello,
    Bob!'''  # ''' 表示多行
    print(s)

    pass


def _main():
    # data_type_varible
    # encode()
    # string()

    # list_tuple()
    # list_slice()
    # list_enumerable()
    # list_iterable()
    # list_iterator()

    # list_gen()
    list_generator()
    # g = list_generator_yield(5)
    # print(type(g))  # <class 'generator'>

    # if_match()
    # for_while()
    # dict_set()

    # immutable_object()

    pass


if __name__ == '__main__':
    _main()
