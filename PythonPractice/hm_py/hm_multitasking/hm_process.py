import multiprocessing
import time
import os


def task1():
    print('%s开始执行' % multiprocessing.current_process())
    print('pid:%s, ppid:%s, module:%s' % (os.getpid(), os.getppid(), __name__))
    for i in range(100):
        print('进程1执行中...')
        time.sleep(1)
    print('process one over')


def task2():
    print('%s开始执行' % multiprocessing.current_process())
    print('pid:%s, ppid:%s, module:%s' % (os.getpid(), os.getppid(), __name__))
    for i in range(100):
        print('进程2执行中...')
        time.sleep(1)
    print('process two over')


def main():
    print('main pid: %s,创建两个子进程' % os.getpid())
    one = multiprocessing.Process(target=task1, name='子进程1')
    two = multiprocessing.Process(target=task2, name='子进程2')
    one.start()
    two.start()
    one.join()
    two.join()
    print('执行结束')


if __name__ == '__main__':
    main()
