from enum import Enum, unique

"""
@unique 装饰器可以帮助我们检查保证没有重复值
"""


@unique
class Weekday(Enum):
    """
    自定义枚举类
    """
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
                       'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))


def test_enum():
    for name, member in Month.__members__.items():
        """
        Jan => Month.Jan , 1
        
        说明：
        value 属性则是自动赋给成员的 int 常量，【默认从 1 开始计数】
        """
        print(name, '=>', member, ',', member.value)


def test_month():
    print(Month.Jan)  # Month.Jan
    print(Month.Jan.name)  # Jan
    print(Month.Jan.value)  # 1


def test_weekday():
    # 成员名称
    print(Weekday.Mon)
    print(Weekday.Mon.name)
    print(Weekday.Mon.value)

    #
    print(Weekday['Mon'])
    print(Weekday(1))

    #
    for name, member in Weekday.__members__.items():
        print(name, '=>', member, ',', member.value)


def _main():
    # test_enum()
    # test_month()
    test_weekday()


if __name__ == '__main__':
    _main()
