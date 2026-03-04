from datetime import datetime


def test_property():
    s = Student()

    #
    # s.set_score(100)
    # print(s.get_score())

    # s.set_score(9999)

    s.score = 100  # 实际转化为s.score(100)
    print(s.score)

    # s.score = 9999  # 实际转化为s.score()
    # print(s.score)

    s.birth = 2006
    print(s.age)

    # s.age = 2006  # AttributeError: can't set attribute 'age'


class Student(object):
    """
    Python内置的 @property装饰器可以把一个方法变成属性
    @property 本身又创建了另一个装饰器 @score.setter ，负责把一个setter方法变成属性赋值
    """

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            # 知识点：raise用于抛出异常
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')

        self._score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    """
    知识点：
    只定义getter方法，不定义setter方法就是一个只读属性
    """

    @property
    def age(self):
        return datetime.now().year - self._birth

    """
    要特别注意：属性的方法名不要和实例变量重名
    调用 s.gender 时，首先转换为方法调用，在执行 return self.gender 时，又视为访问self 的属性，
    于是又转换为方法调用 self.gender() ，造成无限递归，最终导致栈溢出报错RecursionError
    """
    @property
    def gender(self):
        return self.gender


class Student0(object):
    """
    有属性，但是相对属性进行数据校验
    """

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            # 知识点：raise用于抛出异常
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')

        self._score = value


def _main():
    test_property()


if __name__ == '__main__':
    _main()
