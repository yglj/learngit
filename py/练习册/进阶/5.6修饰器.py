'''
要增强now()函数的功能，比如，在函数调用前后自动打印日志，不希望修改now()函数的定义，
在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
本质上，decorator就是一个返回函数的高阶函数
'''

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kv):
        print("函数名：{}".format(func.__name__))
        return func()           #返回now()的调用
    return wrapper

@log          #等价于now = log(now) ，now = wrapper
def now():
    return "时间: 2018.1.1"

#now = log(now)
print(now())
print(now.__name__)


#decorator本身传入参数
def log(str):
    def decorator(func):
        @functools.wraps(func)  #func = now
        def wrapper(*args,**kv):
            print("{}:函数{}".format(str,func.__name__))
            return func #func()
        return wrapper
    return decorator


now = log('执行')(now)() #返回的函数名是'wrapper'，所以需要把原始函数的__name__等属性复制到wrapper()函数中，
                        #否则，有些依赖函数签名的代码执行就会出错。
print(now())

print(now.__name__) #Python内置的functools.wraps 把wrapper.__name__ = func.__name__
