#模块
import sys
print('arguments:')
for i in sys.argv:
     print(i)
print("path:",sys.path)
import random
dir(random)

from math import pi as  pai
print(pai)

#按字节码编译的.pyc文件
#.pyc为其扩展 名，是将Python转换成中间形式的文件
# from..import语句

from math import sqrt
#模块的__name__
import 9模块（Modules）
if __name__ = '__main__':
     print("独立运行")
else:
     print("import another module")
#内置的	dir()函数能够返回由对象所定义的名称列表
#del删除一个名称

#（Packages）包是指一个包含模块与一个特殊的__init__.py文件的文件夹
