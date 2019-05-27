"""
封装yield，来并发完成多任务
"""
from greenlet import greenlet
import time


def test1():
    while True:
        print('--A--')
        time.sleep(1)
        t2.switch()  # 切换到t2


def test2():
    while True:
        print('--B--')
        time.sleep(1)
        t1.switch()


t1 = greenlet(test1)
t2 = greenlet(test2)
t2.switch()
