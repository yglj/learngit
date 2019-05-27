'''
继承
父类，基类，超类（super class，base class） 子类，派生类（Subclass）
子类获得父类的全部功能，也可新增方法，属性，改进父类代码（方法重写）
方法重写，子类方法会覆盖父类方法
根类（root class）Object
'''
'''
一个方法，其参数类型只要知道它的父类，不需要知道它的子类，就可以调用
由运行的对象的确切类型自行决定
“开闭原则”
对扩展开：增加子类
对修改封闭：不需要修改父类方法

静态语言的“鸭子类型”
一个对象只要看起来像鸭子，走起路来像鸭子”，就可以被看作是鸭子
“file_like object”
'''
class Vehicle:
      speed=0
      def __init__(self,s):
            self.speed=s
      def consume(self,distance):
          print('need %2f hours'%(distance/self.speed))

class Bike(Vehicle):
   pass


class Car(Vehicle):
    fuel = 0
    def __init__(self,s,fuel):
        Vehicle.__init__(self,s)
        self.fuel=fuel
    def consume(self,distance):
        Vehicle.consume(self,distance)
        print('need %2f fuel'%(distance*self.fuel))

#没有父类引用指向子类对象
a=Car(80.0,0.012)
a.consume(100.0)

b=Bike(15.0,)   #继承父类，调用父类构造函数
b.consume(100.0)  

class Planet:                                      
      def __init__(self,speed):
            self.speed = speed
      def consume(self,l):                       #与vehicle类的consume方法相似
            print("time=",l/self.speed)
  
def test(Vehicle):
      Vehicle.consume(800)     #鸭子类型，调用有consume方法的对象

c = Planet(100)
test(c)          #自动调用Plant类的consume方法
test(a)          #自动调用Car类的consume方法
            

