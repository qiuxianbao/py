#
# from socketserver import TCPServer, ForkingMixIn, UDPServer, ThreadingMixIn


class Animal(object):
    pass


# 大类:
class Mammal(Animal):
    pass


class Bird(Animal):
    pass


# 能力
class RunnableMixIn(object):
    def run(self):
        print('Running...')


class FlyableMixIn(object):
    def fly(self):
        print('Flying...')


# 各种动物
class Dog(Mammal, RunnableMixIn):
    """
    知识点：多重继承
    这种设计称为MixIn
    它的核心思想是：将一些通用的、独立的功能封装在一个小类（即 Mixin 类）中，然后通过多继承的方式，让其他业务类“按需混入”这些功能，就像搭积木一样组合类的能力。
    MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系
    """
    pass


class Bat(Mammal, FlyableMixIn):
    pass


class Parrot(Bird):
    pass


class Ostrich(Bird):
    pass


# 内置类
# class MyTCPServer(TCPServer, ForkingMixIn):
#     pass


# class MyUDPServer(UDPServer, ThreadingMixIn):
#     pass


def _main():
    pass


if __name__ == '__main__':
    _main()
