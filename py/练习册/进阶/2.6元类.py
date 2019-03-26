#动态语言和静态语言最大的不同，就是函数和类的定义，
#不是编译时定义的，而是运行时动态创建的

class H:
     pass
h = H()
print(type(H))  #H是个class  类型是type
print(type(h))  #h是个实例   类型是class H(object)


#当Python解释器载入hello模块时，就会依次执行该模块的所有语句
#执行结果就是动态创建出一个Hello的class对象

#动态创建类
'''
一 type（）：
class的定义是运行时动态创建的，而创建class的方法就是使用type()函数
type()函数既可以返回一个对象的类型，又可以创建出新的类型
三个参数：
1.class的名称；
2.继承的父类集合，注意Python支持多重继承，
如果只有一个父类，别忘了tuple的单元素写法；
3。class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上
'''
def Hello(self): #定义函数
     print("this is a function,name = Hello")

H2 = type("Hey",(object,),dict(fn=Hello))  #创建类

h2 = H2()
print(H2,h2)
h2.fn()

'''
二 metaclass(元类):
除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass
先定义metaclass，就可以创建类，最后创建实例。
所以，metaclass允许你创建类或者修改类。
可以把类看成是metaclass创建出来的“实例”
'''
#例：给自定义list类加个add方法

class ListMetaClass(type): #metaclass是类的模板，所以必须从“type”类型派生
     def __new__(cls,name,bases,attr):
          attr["add"] = lambda self,values:self.append(values)
          return type.__new__(cls,name,bases,attr)
class MyList(list,metaclass=ListMetaClass):
     pass

mylist = MyList()
mylist.add(2)
print(mylist)
'''
__new__()方法接收到的参数依次是：
当前准备创建的类的对象；
类的名字；
类继承的父类集合；
类的方法集合
'''

