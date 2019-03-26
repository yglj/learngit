# property把实例方法变为属性
##x = [1]
##class F:
##     @property
##     def pro(self):
##          # global x
##          print('@property 修饰器')
"""
2018.11.6
"""
##          return lambda x: x.append(2)
##
##f = F()
##f.pro
##f.pro(x)
##print(x)


"""
2018.11.7
"""
# 打印菱形
##i = 0
##n = 6
##while True:
##     i += 1
##     print(' ' * (n - i), end='*' * (2 * i - 1))
##     print()
##     if i >= n:
##          break
##i = 0     
##while True:
##     n -= 1
##     i += 1
##     print(' ' * i, end='*' * (2 * n - 1))
##     print()
##     if n <= 0:
##          break

# property属性及应用
# 1.私有属性添加getter和setter方法
##class Money:
##     def __init__(self):
##          self.__money = 0
##
##     def getMoney(self):
##          return self.__money
##
##     def setMoney(self, value):
##          if isinstance(value, int):
##               self.__money = value
##          else:
##               print('error:不是整数')

#2.使用property升级getter和setter方法
##class Money:
##     def __init__(self):
##          self.__money = 0
##
##     def getMoney(self):
##          return self.__money
##
##     def setMoney(self, value):
##          self.__money = value
##
##     money = property(getMoney, setMoney)
##
##m = Money()
##m.money = 888
##print(m.money)
          
#3.使用property取代getter和setter方法 
##class Money:
##     def __init__(self):
##          self.__money = 0
##
##     # 注意 @property要在@money.setter前定义
##     @property   
##     def money(self):
##          return self.__money
##     
##     @money.setter
##     def money(self, value):
##          if isinstance(value, int):
##               self.__money = value
##          else:
##               print('error:invaild, this parameter must is a Integer')
##               
##
##m = Money()
##m.money = 999
##print(m.money)

"""
2018.11.8
"""
#with 与 "上下文管理器"
#对于系统资源如文件、数据库连接、socket 而言，应用程序打开这些资源并执行完业务逻辑之后，必须做的一件事就是要关闭（断开）该资源。
#上下文管理器（Context Manager）
#任何实现__enter__()和__exit__()方法的对象都可以称之为上下文管理器

#1.
##class File:
##     def __init__(self, filename, mode):
##          self.filename = filename
##          self.mode = mode
##
##     def __enter__(self):
##          print('------- enter ----------')
##          self.file = open(self.filename, self.mode)
##          return self.file
##
##     def __exit__(self, *args):
##          self.file.close()
##          print('-------- exit -----------')
##          
##
##with File(r'C:\Users\Administrator\Desktop\git学习.txt', 'r') as f:
##     content = f.read()
##     print(content)

#2.
##from contextlib import contextmanager
##@contextmanager
##def my_open(path, mode):
##     f = open(path, mode)
##     yield f
##     f.close()
##
##with my_open(r'C:\Users\Administrator\Desktop\git学习.txt', 'r') as f:
##     print(f.read())

##class MagicMethod(object):
##     """
##     类名/对象名.__doc__   显示类的描述文档
##     """
##     def __init__(self):
##          print('初始化方法')
##
##     def __del__(self):
##          print('析构方法')
##
##     def __call__(self):
##          print('使对象可以用（）调用')
##
##     def __setitem__(self, key, value):
##          print('{%s:%s}' % (key, value))
##
##     def __getitem__(self, key):
##          print(key)
##
##     def __delitem__(self, key):
##          print(key)
##
##     def __setslice__(self, i, j, seq):
##          print(i, j, seq)
##
##     def __getslice__(self, i, j, step):
##          print('getslice:', i, j)
##
##     def __delslice__(self, i, j):
##          print(i, j)
##
##     def __str__(self):
##          return '魔法属性'
##
##     def __repr__(self):
##          return '魔法属性。。。'

##magic = MagicMethod()
##magic['x'] =  'xxx'
##magic['x']
##magic[0:3] = [1, 2, 3]
##magic[-1:2]
##del magic[0:1]
##print(MagicMethod.__doc__)
##print(magic.__module__)
##print(magic.__class__)
##print(MagicMethod.__dict__)
##magic()
##del magic
##print(magic)
##print(magic.__repr__())

