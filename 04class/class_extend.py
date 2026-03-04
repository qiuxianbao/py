# 基类
class Animal(object):
    def run(self):
        print('Animal is running...')


# 继承
class Dog(Animal):
    def run(self):
        print('Dog is running...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


class Timer(object):
    def run(self):
        print('Start...')


"""
鸭子类型

它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起
路来像鸭子”，那它就可以被看做是鸭子。

也就是说调用 run_twice, 入参类型不是animal，只要被调用的对象有 run 方法就可以
"""


def run_twice(animal):
    animal.run()
    animal.run()


if __name__ == '__main__':
    dog = Dog()
    cat = Cat()
    timer = Timer()

    # dog.run()
    # cat.run()

    run_twice(dog)
    run_twice(cat)
    run_twice(timer)  # 鸭子类型
