"""
斐波那契数列迭代器
 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233，377，610，987，1597，2584，4181，6765，10946，17711，28657，46368
"""


class Fibonacci:
    def __init__(self, n):
        self.pre = 0
        self.next = 1
        self.n = n
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.n:
            self.index += 1
            res = self.pre
            self.pre, self.next = self.next, self.pre + self.next
            return res
        else:
            raise StopIteration


if __name__ == '__main__':
    f = Fibonacci(100)
    for i in f:
        print(i, end=', ')
