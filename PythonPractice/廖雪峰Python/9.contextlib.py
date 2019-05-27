#上下文管理 实现上下文，用于with...as...

class Query:
     def __init__(self,name):
          self.name = name

     def __enter__(self):
          print('enter')
          return self   #返回对象本身

     def __exit__(self,Type,value,trackback):
          if Type:
               print(f'状态{Type}')
          else:
               print('exit')

     def say(self):
          print('say %s?'%self.name)

from contextlib import contextmanager

class q1:
     def __init__(self,name):
          self.name = name
     def say(self):
          print('xxx')

@contextmanager
def create_query(name):  #with方式执行方法
     print('Begin')
     q = q1(name)         #上文
     yield q              #利用yield中断,返回对象 ，as赋予别名引用
     print('end')        #with语法块内代码执行完毕，返回中断
                         #继续执行下文（收尾）

@contextmanager 
def tag(name):
     print('<%s>'%name)
     yield
     print('</%s>'%name)


@closing #把对象变为上下文对象
'''
@contextmanager
def closing(obj):
     try:
          yield obj
     finally:
          obj.close()

'''



if __name__ == '__main__':

##with Query('woo') as p:
##     p.say()
     with create_query('van') as q:
          q.say()

     with tag('select'):           #with的作用实际上是处理完中间内容，自动返回中断
          print('<option>1</option>')
          print('<option>2</option>')


#@contextmanager这个decorator接受一个generator，用yield语句把with ... as var把变量输出出去，然后，with语句就可以正常地工作了

#closing（）它的作用就是把任意对象变为上下文对象，并支持with语句
