"""
类名大写单词开头
紧接着是(object) ，表示该类是从哪个类继承下来的
"""

class Student(object):

    count = 0

    """
    类属性
    类属性，也叫静态属性，它的用法和实例属性类似，也是定义在类级别的，但类属性是所有实例共享的
    """
    name = "Student"

    """
    实例方法
    和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量 self
    并且，调用时，不用传递该参数
    """
    def __init__(self, name, score):

        """
        实例属性
        :param name: 【私有属性】即添加两个下划线， __name
        ！！！如果非要访问，可以通过 _Student__name 访问（因为Python解释器对外把 __name 变量改成了 _Student__name）
        不建议用以上方式访问，不同的Python解释器解析的变量名会有区别

        说明：
        在Python中，变量名类似 __xxx__ 的，也就是以双下划线开头，并且以双下划线结尾的，是【特殊变量】，特殊变量是可以直接访问的，不是private变量
        有些时候，你会看到以一个下划线开头的实例变量名，比如 _name ，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”

        :param score:
        """
        self.__name = name
        self.score = score

        # 类属性
        Student.count += 1

    def print_score(self):
        print('%s: %s' % (self.__name, self.score))


if __name__ == '__main__':
    bart = Student('Bart Simpson', 59)
    lisa = Student('Lisa Simpson', 87)

    # print(bart)  # <__main__.Student object at 0x00000224A652FFD0>
    # print(lisa)  # <__main__.Student object at 0x00000224A652FEE0>

    # bart.print_score()
    # lisa.print_score()

    # print(bart.__name)  # AttributeError: 'Student' object has no attribute '__name'
    # print(bart._Student__name)

    print(bart.name)
    print(Student.name)

    bart.name = "Student_bart"
    print(bart.name)
    print(Student.name)

    # 说明：
    # 在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，
    # 因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性
    del bart.name
    print(bart.name)

    bart.gender = "male"
    print(bart.gender)

    del bart.gender
    print(hasattr(bart, "gender")) # False

    print(Student.count)
