import multiprocessing
import time
from multiprocessing import Pool
import random


def worker(n):
    print('%s run... ' % multiprocessing.current_process())
    start_time = time.time()
    time.sleep(random.random() * 3)
    print('worker %s quit, spend time %s:' % (n, time.time() - start_time))


if __name__ == '__main__':
    print('--start--')
    pool = Pool(3)  # 创建进程池，最大3进程
    for i in range(10):
        pool.apply_async(worker, args=(i,))  # 创建异步进程，等待进程处理完毕，处理新的请求
    pool.close()
    pool.join()  # 等待子进程结束，与主进程同步
    print('--end--')
