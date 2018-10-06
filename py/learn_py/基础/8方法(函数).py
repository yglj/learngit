'''
#函数（Functions）是指可重复使用的程序片段 回调函数（Calling）
在定义函数 时给定的名称称作“形参”（Parameters），
在调用函数时你所提供给函数的值称作“实 参”（Arguments）
'''
def power(x,n=2): # 求x第平方 n为默认参数值 默认参数要在参数列表末尾
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s
print(power(6))

def end(l=None):
    if l is None:
      l=[]
      l.append('end')
    print(l)

end()


def say(some):

   print(some+'hello')
say('p')

x = 10
def plus(x):              #取正数
    x = -5
    if not isinstance(x, (int, float)): #判断x的类型是否是int，float
        pass
        raise TypeError('bad operand type!')  #抛异常
    if x>0:
        return x
    else:
        print("局部变量x：",x)
        return -x
    print(x)
print(plus(x))

#局部变量（Local）作用域是它们被定义的块不会以任何方式与身处函数之外但具有相同名称 的变量产生关系

#global语句 让局部变量作用域change全局
y = 2
def g(x):
    global y
    print("before",y)
    y += 20
    print("after",y)
    return y
g(y)
print("global:",y)
    
