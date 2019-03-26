#判断类型
#type()
'''
def f():
     pass
print(type(f))
print(type(abs))
print(type(lambda x:x))
print(type( (i for i in range(5)) ))

import types
print(type(lambda x:x) == types.LambdaType)
'''
#isinstance()  判断对象类型

#dir() 获得对象所有属性和方法
  #__len()__ len()函数内部会自动调用__len()__
#操作对象状态,不知道对象信息时使用
#hasattr(obj,"x")  有属性x？
#setattr(obj,x,value)  设置属性
#getattr(obj,x,default) 获取属性，方法
 

class A:
     pass
a = A()
print(hasattr(a,"x"))
setattr(a,'x','1')
print(getattr(a,'x',404))
print(type(a.x))


