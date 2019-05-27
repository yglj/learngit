

import copy


def test(*args):
    # a = args
    c = copy.copy(args)
    d = copy.deepcopy(args)
    print('原始数据：%s -> %s' % (id(args), args))
    print('深拷贝：%s -> %s' % (id(d), d))
    print('浅拷贝：%s -> %s' % (id(c), c))
    print('--' * 39)


if __name__ == '__main__':
    a = 1
    b = 2
    n1 = [a, b]
    n2 = [1, 2]
    print('n1:', id(n1))
    print('n2:', id(n2))
    test(n1)
    test(n2)
    # test((a, b))  # 深，浅拷贝指向相同

    # test((1, 2))  # 深，浅拷贝指向相同



