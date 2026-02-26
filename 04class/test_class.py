
"""
简单定义类
"""
print("######### demo1：类的构造方法__init__; def定义方法 #########")
class Man:
    def __init__(self, name):
        self.name = name
        print("initialized")

    def hello(self):
        print("hello, my name is %s" % self.name)

    def goodbye(self):
        print("goodbye, my name is %s" % self.name)

m = Man("mike")
m.hello()
m.goodbye()


# https://www.cnblogs.com/bigberg/p/7182741.html

"""
继承
"""
print("######### demo2：类的继承, 类.__init__;#########")
class Person(object):
    # 构造函数
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.weight = "weight"

    # 定义函数
    def talk(self):
        print("person is talking")

class Chinese(Person):
    def __init__(self, name, age, language):
        Person.__init__(self, name, age)
        self.language = language
        print(self.name, self.age, self.weight, self.language)

    # 重写
    def talk(self):
        print("%s is speaking %s" % (self.name, self.language))

    def walk(self):
        print("%s is walking" % self.name)


class America(Person):
    pass #该类没有额外的方法或属性定义

c=Chinese("zhangsan", 22, "english")
c.talk()

print("######### demo3：析构方法，用于在对象被销毁时执行一些清理操作 #########")
print("-------析构方法__del__----------")
class SchoolMember(object):
    """学习成员基类"""
    member = 0

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.enroll()

    def enroll(self):
        """注册"""
        print('just enrolled a new school member [%s].' % self.name)
        SchoolMember.member += 1

    def tell(self):
        print('----%s----' % self.name)
        # 遍历成员
        for k, v in self.__dict__.items():
            print(k, v)
        print('----end-----')

    # 析构方法__del__，用于在对象被销毁时执行一些清理操作
    def __del__(self):
        print('开除了[%s]' % self.name)
        SchoolMember.member -= 1


class Teacher(SchoolMember):
    """教师"""
    def __init__(self, name, age, sex, salary, course):
        super().__init__(name, age, sex)
        self.salary = salary
        self.course = course

    def teaching(self):
        print('Teacher [%s] is teaching [%s]' % (self.name, self.course))


class Student(SchoolMember):
    """学生"""
    def __init__(self, name, age, sex, course, tuition):
        super().__init__(name, age, sex)
        self.course = course
        self.tuition = tuition
        self.amount = 0

    def pay_tuition(self, amount):
        print('student [%s] has just paied [%s]' % (self.name, amount))
        self.amount += amount


t1 = Teacher('Wusir', 28, 'M', 3000, 'python')
t1.tell()

s1 = Student('haitao', 38, 'M', 'python', 30000)
s1.tell()

s2 = Student('lichuang', 12, 'M', 'python', 11000)


"""
此处虽然只删除了s2，但是运行结果中，s1和t1对象也一并被删除了
原因：在程序结束时，Python 解释器会自动销毁所有未被引用的对象，并调用它们的 __del__ 方法。
这是 Python 的垃圾回收机制的一部分

3
开除了[lichuang]
2
开除了[Wusir]
开除了[haitao]
"""
print(SchoolMember.member)
del s2
print(SchoolMember.member)
