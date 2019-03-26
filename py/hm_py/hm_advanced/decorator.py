"""
装饰器
多个装饰器对同一个函数装饰，从下到上开始，结果由上到下扩展
添加标签<h1><p></p></h1>
类装饰器
"""

# 通用装饰器


def dec(func):
    print('装饰函数: %s' % func)

    def call_func(*args, **kwargs):
        print('--预处理--')
        ret = func(*args, **kwargs)
        print('--末处理--')
        return '<h1>' + ret + '</h1>'
    return call_func


def dec2(func):
    print('装饰函数: %s' % func)

    def call_func(*args, **kwargs):
        print('--预处理--')
        ret = func(*args, **kwargs)
        print('--末处理--')
        return '<p>' + ret + '</p>'
    return call_func


@dec
@dec2
def test1(num):
    return '--test1--: %d' % num


def test2(num):
    return '--test2--: %d' % num


test2 = dec(test2)
print(test1(10))
print(test2(10))


class Dec:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('----测试类装饰器-----')
        return self.func(*args, **kwargs)


@Dec
def test3(num):
    return '--test3--: %d' % num


print(test3(10))
