import time

gl_x = 0
gl_y = 0


def run1(x):
    while True:
        print(x)
        x += 1
        time.sleep(0.1)
        yield


def run2(y):
    while True:
        print(y)
        y -= 1
        time.sleep(0.1)
        yield


def main():
    test1 = run1(gl_x)
    test2 = run2(gl_y)
    while True:
        next(test1)
        test2.send(None)
        print('-' * 30)


if __name__ == '__main__':
    main()
