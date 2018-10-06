# 循环
# 程序的三大基本流程：顺序，分支（岔路），循环（重复）

"""
初始条件设置 - 通常是重复执行，计数器
while（条件）：
    重复特定代码
    处理条件
"""

# 关键字 break，continue 满足某一条件，退出循环/跳过本次循环


def s():
    result = 0
    i = 0
    while True:
        if i > 100:
            break
        if i % 2 != 0:
            i += 1
            continue
        result += i
        i += 1
    print('0~100所有偶数的和 = %d' % result)

# 输出5行*,依次递增


def print_xin():
    col = 0
    while col < 5:
        col += 1
        row = col
        # print('*' * col)
        while row > 0:
            row -= 1
            print('*', end=' ')
        print()

# 九九乘法表


def multiply():
    """
    九九乘法表
    :return: None
    """
    x, y = 1, 1
    while 0 < x <= 9:
        y = 1
        while 0 < y <= x:
            print('%d * %d = %d' % (x, y, x*y), end='\t')
            y += 1
        x += 1
        print('')

# 转义字符 \t 横向制表符 \' \" \\ \n \r回车符


if __name__ == '__main__':
    print_xin()
    print('callable')