#map()函数接收两个参数，一个是函数，一个是Iterable
#map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
a=[1,2,3,4,5,6]
b=[7,8,9,0]   
c=map(None,a,b)
d=map(lambda x:x+1,a) #匿名函数作参
print(d)
print(next(c))
for i in d:
     print(i)

     
def m(x):
     return x*x
for i in map(m,b):
     print(i)
#d = map(m,a)  #返回一个迭代器 Iterator是惰性序列
#print(next(d))
'''
#等价于
l = []
for i in a:
     print(l.append(m(i)))
print(l)
'''
b = list(map(str,b))
print(b)


'''
def f(x):
    return x*x
r=map(f,[1,2,3,4,5,6,7,8,9])
print(list(r))

#map()作为高阶函数，事实上它把运算规则抽象了

s=list(map(str,[1,2,3,4,5,6,7,8,9]))
print(s)
'''

