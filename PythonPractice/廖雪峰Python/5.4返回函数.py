#函数作返回值
#可变参求和函数
def sum(*args):  #*args可变参，一个参数元组
     #print(type(args))
     t = 0
     for i in args:
          t = t + i
     return t
print(sum(1,2,4,5))


def lazy_num(*args): 
     def sum():     #在函数lazy_sum中又定义了函数sum
          t = 0
          for i in args:   #内部函数sum可以引用外部函数lazy_sum的参数和局部变量
               t = t + i
          return t  
     return sum
print(lazy_num(1,3)) #当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中
f = lazy_num(1,2,4)  #把sum函数作为结果值返回 赋给变量f
print(f())                    # 调用f 等价于调用sum函数

#注意：
#每次调用都会返回一个新的函数，即使传入相同的参数
f1 = lazy_num(1,2,4)
print(f,f1,f == f1)

print("###########################")
#“闭包（Closure）”的程序结构

def count():
     fs = []
     for i in range(1,4):  #函数返回了一个函数后，内部的局部变量还被新函数引用
          def f():
               return i*i
          fs.append(f)  
     return fs          #返回一个函数列表

f1,f2,f3 = count() #等价于（f1,f2,f3）or [f1,f2,f3]
print(f1())       #返回的函数并没有立刻执行，而是直到调用了f()才执行
print(f2())
print(f3())

'''
原返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，
它们所引用的变量i已经变成了3，因此最终结果为9
'''
print('########################################')
#返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
def count1():
     def f(i):    #用函数f的参数绑定循环变量当前的值
          return lambda :i*i
          #return lambda i :i*i
##          def g():
##               return i*i
##          return  g   
     fs =[]
     for i in range(1,4):
          print(f(i))
          fs.append(f(i))  #追加f（i）返回值为函数g
     return fs

f3,f4,f5 = count1()
print(f3(),f4(),f5())
#print(f3(1),f4(2),f5(3))
