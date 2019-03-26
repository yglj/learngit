'''
类（class）与对象(实例：instance)
Object Oriented Programming(oop) Property(属性) Method(方法)
类是实例的模板 实例间数据独立
方法就是实例绑定的函数

'''
class M:
    name='sam'   #类变量
    i = 999
    def __init__(self,name):     # __intit__构造函数
         self.name = name        #self.name对象变量，name局部变量
         print(name,self.name,"construction")

    def sayhi(self):
        print('%s say hello'%self.name)
print("直接用类名调用静态变量",M.name,M.i)

mx=M("x")   #实例化
n = mx.sayhi()          #方法默认返回None
print(n)
print("对象调用实例变量",mx.name)
print("对象调静态变量",mx.i)
mx.sayhi()
print(M)
print(mx)

class Car:
    #speed=0x

    def t(a,distance):
          time=distance/a.speed
          return time

c1=Car()
c1.speed=60        #在外部 给实例绑定属性
#c11=Car()
#print(c11.speed)   #'Car' object has no attribute 'speed'同类实例属性不同
#print(Car.speed)    # type object 'Car' has no attribute 'speed'
print(c1.t(100.0))
print(c1.t(200.0))

c2=Car()
c2.speed=150
print(c2.t(100.0))
print(c2.t(200.0))

