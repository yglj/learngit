
import time
from collections.abc import Iterable, Iterator


class Students:
    def __init__(self):
        self.names = list()
        self.num = 0

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        return self

    def __next__(self):
        if self.num < len(self.names):
            res = self.names[self.num]
            self.num += 1
            return res
        else:
            raise StopIteration


'''
class ClassIterator:
    def __init__(self, obj):
        self.obj = obj
        self.index = -1

    def __iter__(self):
        pass

    def __next__(self):
        self.index += 1
        if self.index < len(self.obj.names):
            return self.obj.names[self.index]
        else:
            raise StopIteration('停止迭代')
'''

if __name__ == '__main__':
    stu = Students()
    stu.add('c++')
    stu.add('java')
    stu.add('c')

    print('判断stu对象是不是可迭代对象：', isinstance(stu, Iterable))
    iterator_stu = iter(stu)
    print('判断stu对象是不是迭代器：', isinstance(iterator_stu, Iterator))

    for name in stu:
        print(name)
        time.sleep(1)
