import os
import multiprocessing


def rw(q, oldpath, newpath, filename):  # 子进程出错不会报错
    with open(os.path.join(oldpath, filename), 'r') as f:
        content = f.read()
    with open(os.path.join(newpath, filename), 'w') as f:
        f.write(content)
    q.put(filename)


def copy():
    # 输入要copy的目录
    inp = os.getcwd()
    old_path = os.path.join(inp, 'test')
    # 创建要复制的目录
    new_path = old_path + '[副件]'
    if not os.path.exists(new_path):
        os.mkdir(new_path)

    # 创建进程池
    pool = multiprocessing.Pool(3)
    queue = multiprocessing.Manager().Queue()
    # 开启多任务，执行copy
    for filename in os.listdir(old_path):
        pool.apply_async(rw, (queue, old_path, new_path, filename))

    # 打印进度
    copy_sum = 0
    total: int = len(os.listdir(old_path))
    # print(total)
    while True:
        copy_sum += 1
        filename = queue.get()
        # print('%s already copy' % filename)
        print('\rprogress bar: %.2f %% ...' % (copy_sum * 100 / total), end='')
        if copy_sum >= total:
            break

    pool.close()
    print('-----end------')


if __name__ == '__main__':
    copy()
