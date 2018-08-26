'''
函数式编程（functional programming）：一种编程范式
面向过程程序设计，贴近数学计算
越抽象的语言接近计算，越低级的语言接近计算机硬件

纯粹的函数式编程没有变量，输入确定，输出确定
可以把函数本身作为参数传入另一个函数，还可以返回一个函数

'''
#高阶函数（HIght-order-function）：一个函数接受另一个函数做参数
#变量指向函数 即把函数本身赋给变量，可以通过变量名调用
f = abs(-24)
print(f)
f = abs  #把函数绑定另一个名字
print(f)
f = f(-6) #通过另一个函数名调用
print(f)
#函数名其实就是指向函数的变量
#abs = 10   # TypeError: 'int' object is not callable
print(abs(-9)) #变量abs已指向整数10

def func(a,b,f):
     return f(a)+f(b)
print(func(-3,-7,abs))
