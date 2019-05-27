#隐式定义函数，不需要函数名
#只能有一个表达式，返回该式结果，不用return
#匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数
#也可以把匿名函数作为返回值返回
#!/usr/bin/python
# -*- coding utf-8 -*-
name='小明'#input()
a1=(72)
a2=(85)
t=lambda a1,a2 :a1-a2
p= t(a2,a1)/a1*100
print('%s的成绩提高了%.1f%%'%(name,p))


print(list(map(lambda x:x*x,[1,2,3,4,5,6,7,8,9])))

def fun(x,y):
     return lambda : x*x+y*y

'''
def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
'''
L = list(filter(lambda x: x%2 == 1 , range(1,20)))
print(L)
