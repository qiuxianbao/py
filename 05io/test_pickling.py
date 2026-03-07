# 序列化: 我们把变量从内存中变成可存储或传输的过程称之为序列化
import json
from pathlib import Path

current_dir = Path(__file__).parent


def test_pickle():
    import pickle

    d = dict(name='Bob', age=20, score=88)
    # 把任意对象序列化成一个 bytes
    # print(pickle.dumps(d))

    file_path = current_dir / 'dump.txt'
    with open(file_path, 'wb') as f:
        # 把对象序列化后写入一个file-like Object：
        pickle.dump(d, f)

    with open(file_path, "rb") as f:
        print(pickle.load(f))


def test_json():
    import json
    d = dict(name='Bob', age=20, score=88)
    # dumps() 方法返回一个 str ，内容就是标准的JSON。
    json_str = json.dumps(d)
    print(json_str)

    print(json.loads(json_str))


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


def test_student_json():
    s = Student('Bob', 20, 100)

    # json.dumps(s)  # ypeError: Object of type Student is not JSON serializable
    print(json.dumps(s, default=student2dict))
    # print(json.dumps(s, default=lambda obj: obj.__dict__))

    json_str = '{"age": 20, "score": 88, "name": "Bob"}'
    print(json.loads(json_str, object_hook=dict2student))  # <__main__.Student object at 0x0000021D7A4E5600>


def _main():
    # test_pickle()
    # test_json()
    test_student_json()


if __name__ == '__main__':
    _main()
