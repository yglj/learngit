
def test1(a, b, *args, c=888, **kwargs):
    print('*' * 50)
    print(a)
    print(b)
    # print(c)
    print(args)
    print(kwargs)


def test2(a, b, *args, **kwargs):
    print(a)
    print(b)
    # print(c)
    print(args)
    print(kwargs)
    test1(a, b, args, kwargs)
    test1(a, b, *args, kwargs)
    test1(a, b, args, **kwargs)


if __name__ == '__main__':
    test2(1, 2, 3, 4, 5, 6, 7, 8, {'1': 'a', '2': 'b'}, x='a', y='b')
    # test1(1, 2, 3, 4, 5, 6, 7, 8, x='a', y='b')
