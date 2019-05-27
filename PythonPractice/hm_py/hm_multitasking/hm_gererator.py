

def fib(n):
    x, y = 0, 1
    while n:
        arouse = yield x
        if arouse:
            print(arouse)
        x, y = y, x + y
        n -= 1
    return 'ok'


if __name__ == '__main__':
    '''
    f = fib(10)
    for i in range(10):
        print(next(f), end=', ')
    '''
    f = fib(10)
    x = f.send(None)
    print(x)
    while True:
        try:
            x = f.send('send ...')
            print(x)
        except StopIteration as stop:
            print(stop.value)
            break
