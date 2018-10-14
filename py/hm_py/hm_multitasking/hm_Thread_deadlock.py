
import threading
import time

lockA = threading.Lock()
lockB = threading.Lock()


class MyThread1(threading.Thread):
    def run(self):
        lockA.acquire()
        print(self.name, '执行partA...')
        lockB.acquire()  # 线程获得partA的锁,阻塞在partB

        print(self.name, '执行partB...')

        lockA.release()
        print(self.name, '执行partA...')
        lockB.release()


class MyThread2(threading.Thread):
    def run(self):
        lockB.acquire()
        print(self.name, '执行partB...')
        lockA.acquire()  # 线程获得partB的锁,阻塞在partA

        print(self.name, '执行partA...')

        lockB.release()

        print(self.name, '执行partB...')
        lockA.release()


def main():  # 发生死锁
    one = MyThread1()
    two = MyThread2()
    one.start()
    two.start()


if __name__ == '__main__':
    main()
