"""
函数：
匿名函数：
闭包：
对象：
"""

k = 2
b = 11
x = 3
print(k * x + b)


def line2(k, x, b):
    print(k * x + b)


def line3(x):
    print(k * x + b)


def line4(x, k=2, b=11):
    print(k * x + b)


class Line:
    def __init__(self, k, b):
        self.k = k
        self.b = b

    def __call__(self, x):
        print(self.k * x + self.b)


line2(2, 3, 11)
line3(3)
line4(3)
line5_1 = Line(2, 11)
line5_1(3)


def line6(k, b):
    def line(x):
        print(k * x + b)
    return line


line6_1 = line6(2, 11)
line6_1(3)


n = 300


def test1():
    n = 200

    def test2():
        nonlocal n
        print('pre--->', n)
        n = 100
        print('end-->', n)
    return test2


test = test1()
test()
