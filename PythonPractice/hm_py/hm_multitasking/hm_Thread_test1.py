

import threading
import time


def sing():
    for i in range(10):
        print('唱歌...')
        time.sleep(1)


def dance():
    for i in range(10):  # 函数执行结束，线程结束
        print('跳舞...')
        time.sleep(1)


if __name__ == '__main__':
    sing_thread = threading.Thread(target=sing)
    dance_thread = threading.Thread(target=dance)
    sing_thread.start()  # 启动线程，开始执行程序
    dance_thread.start()

    # 主线程线程结束，子线程随之结束
