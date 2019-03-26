'''
偏函数（Partial function
作用把一个函数的某些参数给固定住（也就是设置默认值），
当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，
这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
'''
import functools

print(int('15',base =16))#base关键字参数规定传入字符为n进制数

def int2(x):
     return  int(x,base = 2)   #方便转换大量的二进制字符串
print(int2('1111'))

f = functools.partial(int,base = 2) #
print(f('101001'))

#创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数
print(int2('100010'))
# 等价于 kw = {'base':2}   int('10010',**kw)

max2 = functools.partial(max,10)
#实际上会把10作为*args的一部分自动加到左边
print(max2(2,4,7))
