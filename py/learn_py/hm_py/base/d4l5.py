# 递归  函数自己调用自己
# 计算数字累加
import time


def total(n):
    if n == 1:
        return 1
    else:
        return n + total(n - 1)


def total2(n):
    return 1 if n == 1 else n + total2(n - 1)


def total3(n):
    return n == 1 and 1 or n + total3(n - 1)


def total4(n, num=0):
    if n == 0:
        return num
    else:
        return total4(n - 1, num + n)


def total5(num):
    for i in range(101):
        num += i
    return num


def spend(func):
    start = time.time()
    func(100)
    end = time.time() - start
    # print(end)
    print('%s耗时:%s' % (func.__name__, end))


spend(total)
spend(total2)
spend(total3)
spend(total4)
spend(total5)
# print(total(100))
# print(total2(100))
# print(total3(100))
# print(total4(100))
