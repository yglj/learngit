
#__getattr__
'''
正常情况下，调用一个不存在类的方法或属性时，会报错
可以写一个__getattr__()方法，动态返回一个属性，避免错误
当调用不存在的属性时，比如score，
Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性，或方法
注意到任意调用如s.abc都会返回None,要按照约定，抛出AttributeError的错误：
'''
class S:
     def __getattr__(self,attr):
          if attr == 'number':
               return 25
          elif attr  == 'getNum':
               return lambda : 50
          else:
               raise AttributeError( ' \'S\' object has no attribute \'%s\' '%attr)

s = S()
print(s.number)
print(s.getNum())
#print(s.abc)
'''
这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。
这种完全动态调用的特性有什么实际作用呢？作用就是，可以针对完全动态的情况作调用
'''

'''
现在很多网站都搞REST API，比如新浪微博、豆瓣啥的，调用API的URL类似：

http://api.server/user/friends
http://api.server/user/timeline/list
如果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改。
'''
#利用完全动态的__getattr__，我们可以写出一个链式调用
class Chain(object):

    def __init__(self, path=''):
         
         print('cal __init__(%s)' % path)
         self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path)) #不是递归，而是返回格式化对象

    def __str__(self):
        return self._path

    __repr__ = __str__
print(Chain().status.user.timeline.list)



#__call__ 实例调用自身
#相当于重载了括号运算符
class M:
     def __init__(self,name):
          self.name = name

     def __call__(self):
          print('M类对象的名字是：%s'%self.name)
m = M('kk')
m()
'''
函数本身其实也可以在运行期动态创建出来，因为类的实例都是运行期创建出来的
对实例进行直接调用就好比对一个函数进行调用一样，
完全可以把对象看成函数，把函数看成对象
怎么判断一个变量是对象还是函数呢？判断一个对象是否能被调用，
能被调用的对象就是一个Callable对象
'''
#通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。
callable(S())
True
callable(max)
True
callable([1, 2, 3])
False
callable(None)
False
callable('str')
False
