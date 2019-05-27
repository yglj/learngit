#特殊的__slots__变量，能限制class（实例）能添加的属性，而不是类
#注意: __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
from types import MethodType 
class A:
     __slots__ = ('a','ab','abc','set_a')


a = A()
a2 = A()
a.a = '1'
print(a.a)

def set_a(self,a):
     self.a = a

#把函数绑定到对象，对其他实例不起作用
a.set_a = MethodType(set_a,a) #MethodType（） 把函数变成类方法
#a.set_a = set_a  #只是函数换名
#a.set_a(a,2)
print(a.a)

A.set_a = set_a  #把方法绑定到class
a2.set_a(3)
print(a2.a)


class B(A):
     __slots__ = 'cc'
     pass

b = B()
b.c = 7
print(b.c)   #AttributeError: 'B' object has no attribute 'c'
