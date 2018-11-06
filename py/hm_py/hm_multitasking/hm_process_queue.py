import time
import multiprocessing
from multiprocessing import Queue

queue: Queue = Queue()  # 进程间通信 Queue对象
# 通过主进程中queue, 为两个子进程传递消息


def download(q):
    print('%s中queue的内存地址:%s，q的内存地址:%s' % (multiprocessing.current_process(), queue, q))
    print('传输数据...')
    down_data = [1, 2, 3, 4, 5, 6, 7, 8]
    for data in down_data:
        q.put(data)  # 发数据
        print('waiting...', data)
        # time.sleep(1)
    print('传输完毕...')


def get_data(q):
    print('%s中queue的内存地址:%s，q的内存地址:%s' % (multiprocessing.current_process(), queue, q))
    get_list = list()
    print('开始接收数据...')
    while not q.empty():  # 判断队列是否为空
        data = q.get()  # 收数据
        # time.sleep(1)
        print('shodao', data)
        get_list.append(data)
        assert not q.full()  # 断言，queue未装满
    print(f'处理完成 \n --> {get_list}')


def main():
    print(queue)
    print('开始进程间通信...')
    # queue: Queue = Queue()
    one = multiprocessing.Process(target=download, name='one', args=(queue,))
    # 进程间各有一套程序代码，若不在执行函数中传入参数，会使用各自的变量
    two = multiprocessing.Process(target=get_data, name='two', args=(queue,))
    one.start()
    two.start()
    one.join()
    two.join()
    print('ending...')


if __name__ == '__main__':
    main()
