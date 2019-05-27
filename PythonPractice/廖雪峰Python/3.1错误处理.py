
'''
￥在程序运行的过程中，如果发生了错误，可以事先约定返回一个错误代码，
这样，就可以知道是否有错，以及出错的原因
(如果不处理错误，程序就会停止运行)

￥打开文件的函数open()，成功时返回文件描述符（就是一个整数），出错时返回-1

'''
##n = 9
##n -= 10
##def Assert():
##     assert n>0
##     print(n)
##
##Assert()

#用错误码来表示是否出错十分不便，因为函数本身应该返回的正常结果和错误码混在一起，
#造成调用者必须用大量的代码来判断是否出错
def foo():  
    r = some_function()  #检查函数的返回值
    if r==(-1):
        return (-1)
    return r

def bar():         #处理错误，打印错误信息
    r = foo()
    if r==(-1):
        print('Error')
    else:
        pass


'''
￥一旦出错，还要一级一级上报，直到某个函数可以处理该错误
（比如，给用户输出一个错误信息）
'''

def test(n):
     try:
          if type(n) == str:
               n = int(n)
          print('result: ',10 / n)
     except ValueError as e:
          print('error: invalid vallue') 
     except ZeroDivisionError as e:
          print("error: 分母不能为零")
     except UnicodeError as e:                 #???
          pirnt("error: Unicode 字符串错误")
     else:
          print("not error")
     finally:
          print("有无错误，都会到这里","\nEnding\n")

##test(0)
##test(2)
##test('a')

#try...except...finally
'''
￥所以高级语言通常都内置了一套try...except...finally...的错误处理机制
try 运行，若执行出错，会跳转到错误处理代码块except，执行完except后，有finally语句块，则执行

￥如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句

￥Python的错误其实也是class，所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”

￥使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用
也就是说，不需要在每个可能出错的地方去捕获错误，只要在合适的层次去捕获错误就可以了
'''

def test2():
     def middle():
          def content():
               3 / 0
               print("finish")
               return content
          return content()
     return  middle()
     

##test2()
#调用栈
'''
如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出
（没有错误处理，程序报错的一般情况）
出错并不可怕，可怕的是不知道哪里出错了。解读错误信息是定位错误的关键
 错误信息第1行：
Traceback (most recent call last):
告诉我们这是错误的跟踪信息。
 出错的时候，一定要分析错误的调用栈信息，才能定位错误的位置。
 '''
import logging
def test3():
     try:
          4/0
     except Exception as e:
          print("division by zero\nlogging begin:\n")
          logging.exception(e)
     print('continue:')
     print(100 - 4)
     print("ending....")

##test3()
#记录错误
'''
正常情况;不捕获错误，python解释器打印错误堆栈，程序结束
内置logging模块
能捕获错误，把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去。
通过配置，logging还可以把错误记录到日志文件里，方便事后排查

'''
class my_ValueError(ValueError):
     pass
    
def test4(n):
     def m():
          def c():
               if n == 2:
                    print('bad value',n)
                    raise my_ValueError("division must equals zero") #使用自定义类
          return c()
     m() #1.抛出给python解释器处理
##     try:
##          m()
##     except Exception as e:
##          pass    #2.捕获，不处理
####          print(e,"/token raise error")  #3.捕获，给错误信息
##     finally:
##          print('end')
     
          

test4(2)              
#抛出错误
'''
因为错误是class，捕获一个错误就是捕获到该class的一个实例。
因此，错误并不是凭空产生的，而是有意创建并抛出的。Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。

raise 手动抛错（设置错误条件）
自定义错误（继承内置错误类型 valueError，TypeError等）

其实这种错误处理方式不但没病，而且相当常见。捕获错误目的只是记录一下，便于后续追踪。但是，由于当前函数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理。好比一个员工处理不了一个问题时，就把问题抛给他的老板，如果他的老板也处理不了，就一直往上抛，最终会抛给CEO去处理。

raise语句如果不带参数，就会把当前错误原样抛出。此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：

try:
    10 / 0
except ZeroDivisionError:
    raise ValueError('input error!')
'''
