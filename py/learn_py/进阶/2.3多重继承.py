#通过多重继承，一个子类就可以同时获得多个父类的所有功能
class Animal:
     pass
class Mammal:
     pass
class Bird:
     pass

class Runable:
     def run():
          print('running ...')

class Flyable:
     def fly():
          print('fly....')


class dog (Mammal,Runable):
     pass

class little_bird(Brid,Flyable):
     pass

'''
#MixIn 一种设计模式
MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，
我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。


Python自带了TCPServer和UDPServer这两类网络服务，
而要同时服务多个用户就必须使用多进程或多线程模型，
这两种模型由ForkingMixIn和ThreadingMixIn提供。
通过组合，我们就可以创造出合适的服务来
'''
#编写一个多进程模式的TCP服务，定义如下：
class MyTCPServer(TCPServer, ForkingMixIn):
    pass
#编写一个多线程模式的UDP服务，定义如下：

class MyUDPServer(UDPServer, ThreadingMixIn):
    pass
#如果你打算搞一个更先进的协程模型，可以编写一个CoroutineMixIn：

class MyTCPServer(TCPServer, CoroutineMixIn):
    pass
