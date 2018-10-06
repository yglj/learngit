# 以.py结尾的python源代码文件都是一个模块
# 模块名就是标识符
# 模块定义的类，全局变量，函数都是直接提供给外部使用的工具
# 导入模块 import 、 from...import...
# as 指定别名

import os

# 模块的搜索顺序 1.先搜当前目录 2.再搜系统目录 __file__ 内置属性查看模块的路径
print(__name__)
print(__file__)
print(__package__)
print(__doc__)

# 导入文件时所有代码都会被执行
# 增加侧死代码，只在模块内使用，导入其他文件不需要执行
# __name__ 内置属性，字符串 如果是当前执行模块 __main__,如果是导入的模块就是导入的模块名


def main():
    pass


if __name__ == '__main__':
    print(os.__file__)
    print(os.__name__)
    main()