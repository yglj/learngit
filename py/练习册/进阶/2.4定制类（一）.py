#Python的class中还有许多有特殊用途的函数，可以帮助我们定制类。
#__str__()返回用户看到的字符串，
#__repr__()返回程序开发者看到的字符串，为调试服务的。
class A:
     def __init__(self,name):
          self.name = name
     def __str__(self):
           return "一个A类对象，名字为：%s"%self.name
          
     __repr__ = __str__
a = A('obj')
print(a)
print(a.__repr__())

'''
__iter__
如果一个类想被用于for ... in循环，类似list或tuple那样，
就必须实现一个__iter__()方法，该方法返回一个迭代对象，
然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，
直到遇到StopIteration错误时退出循环
'''
class Fib0:
     def __init__(self):
          self.a,self.b = 1,1
     def __iter__(self):
          return self   # 实例本身就是迭代对象，故返回自己
     def __next__(self):
          self.a,self.b = self.b,(self.a + self.b)
          if self.a > 1000:           # 退出循环的条件
               raise StopIteration
          return self.a
for i in Fib0():
     print(i)

#__getitem__
#1.要表现得像list那样按照下标取出元素，需要实现__getitem__()方法

class Fib1:
     def __getitem__(self,n):
          a,b = 1,1
          for i in range(n):
               a,b = b,a+b
          return a
          

for i in range(5):
     print('取【】下标',Fib1()[i])
print(Fib1()[100])


#2.实现切片方法，要传入一个切片对象(step,负数)
#（__getitem__()传入的参数是一个int，还是一个切片对象slice）

class Fib2:
     def __getitem__(self,n):
          if isinstance(n,int):
               a,b = 1,1
               for i in range(n):
                    a,b = b,a+b
               return a
          elif isinstance(n,slice):
               start = n.start
               stop = n.stop
               step = n.step
               if n.step == None:
                    step = 1
               if start == None:
                    start = 0
               list = []
               a,b = 1,1
               for i in range(stop):
                    if i >= start and i%step == 0 :
                         list.append(a)
                    a,b = b,a+b
               return list

f = Fib2()
print(f[:10])
print(f[2:5])
print(f[:10:3])

'''
如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str。

与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。
__delitem__()方法，用于删除某个元素。

通过上面的方法，自定义的类可以表现得和Python自带的list、tuple、dict没什么区别，
这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口
'''

