

def test_student_slot():
    s = StudentSlot()
    s.age = 25
    # s.score = 100  # AttributeError: 'StudentSlot' object has no attribute 'score'

    print(s.age)
    # print(s.score)

    g = GraduateStudent()
    g.score = 100
    print(g.score)


class StudentSlot(object):
    """
    Python允许在定义 class 的时候，定义一个特殊的 __slots__ 变量，来限制该 class 实例能添加的属性
    仅对当前类实例起作用，对继承的子类是不起作用的
    """
    __slots__ = ('name', 'age')


class GraduateStudent(StudentSlot):
    pass


def test_student_addFunc():
    s = Student()
    s.name = 'Michael'
    print(s.name)

    # 给实例绑定方法
    from types import MethodType

    s.set_age = MethodType(set_age, s)

    #
    s.set_age(25)
    print(s.age)

    # 给所有的示例绑定方法
    Student.set_score = set_score
    s.set_score(100)
    print(s.score)


"""
正常情况下，当我们定义了一个 class ，创建了一个 class 的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性
"""


class Student(object):
    pass


def set_age(self, age):
    self.age = age


def set_score(self, score):
    self.score = score


def _main():
    # test_student_addFunc()
    test_student_slot()

    pass


if __name__ == '__main__':
    _main()
