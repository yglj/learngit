
# 函数 独立功能的代码块 、封装、重用
# 定义、调用
# 解释性语言，调用写在不能在定义前
# 文档注释""" """
# 函数参数: 形参（定义）接受数据，实参（调用）传递数据
# return （函数出口）返回值，结束函数
# 函数的嵌套调用

from d2 import l5

# l5.multiply()


def print_line(char, items):
    print(char * items)


def print_lines(row):
    """
    打印多行分隔符
    :param row: 行数
    """
    while row > 0:
        row -= 1
        print_line('+', 50)


if __name__ == '__main__':
    print_lines(5)