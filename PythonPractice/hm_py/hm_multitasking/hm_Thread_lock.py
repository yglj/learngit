
import threading
import time

gl_num = 0  # 多线程访问全局变量会发生资源竞争，影响数据安全
lock = threading.Lock()  # 创建互斥锁对象，解决线程同步问题


def sum1(n):
    global gl_num
    print('Thread:%s' % threading.current_thread())
    for i in range(n):
        lock.acquire()  # 上锁
        gl_num += 1
        lock.release()  # 释放锁


def sum2(n):
    global gl_num
    print('Thread:%s' % threading.current_thread())
    for i in range(n):
        lock.acquire()
        gl_num -= 1
        lock.release()



def main():
    n = 1000000
    one = threading.Thread(target=sum1, args=(n,), name='tom')
    two = threading.Thread(target=sum2, args=(n,))
    one.start()
    two.start()
    one.join()
    two.join()
    print('执行%s次后gl_num的值：%s' % (n, gl_num))


if __name__ == '__main__':
    main()


