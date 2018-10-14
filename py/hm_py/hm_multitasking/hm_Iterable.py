
import time
from collections.abc import Iterable, Iterator


class Students:
    def __init__(self):
        self.names = list()

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        return ClassIterator(self)


class ClassIterator:
    def __init__(self, obj):
        self.obj = obj

    def __iter__(self):
        pass

    def __next__(self):
        return self.obj.names


if __name__ == '__main__':
    stu = Students()
    stu.add('湖吧')
    stu.add('java')
    stu.add('c')

    print('判断stu对象是不是可迭代对象：', isinstance(stu, Iterable))
    iterator_stu = iter(stu)
    print('判断stu对象是不是迭代器：', isinstance(iterator_stu, Iterator))

    for name in stu:
        print(name)
        time.sleep(1)
