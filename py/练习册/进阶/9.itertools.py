#itertools 迭代器工具
import itertools

#>>>无限迭代器， 计数器
##count = itertools.count(2,2)  
##print(count)
##for n in count:
##     print(n)


#>>>cycle（） 把一个序列无限循环重复
##d = itertools.cycle(['a','b','c'])
##for o in d:
##     print(o)


#>>>repeat() 把一个元素无限重复下去，可限定次数
##r = itertools.repeat('xp',100)  #yield , 递归
##print(r)
##for i in r:
##     print(i)

#>>>takewhile() 参数：条件表达式，迭代器对象 ,返回一个序列
##print(list(itertools.takewhile(lambda x:x<=20 ,itertools.count(0))))

#chain() 串联迭代对象
for ch in itertools.chain('abc',('x','y','z')):
     print(ch)

#groupby() 把（相邻元素）分组 重复值:迭代对象
#参数：iterator 条件表达式
for k,v in itertools.groupby('abcAaalddxdD',lambda x:x.upper()): 
     print(k,list(v))

##练习
##计算圆周率可以根据公式：
##
##利用Python提供的itertools模块，我们来计算这个序列的前N项和：

# -*- coding: utf-8 -*-
import itertools,functools


def pi(N):
    #' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
     odd0 = itertools.count(1,2)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
     odd1 = itertools.takewhile(lambda x:x<=2*N-1 ,odd0)
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
     odd2 = map(lambda i : (-1)**(i//2)*4/i,odd1)
    # step 4: 求和:
     return sum(odd2)


# 测试:
print(pi(10))
##print(pi(100))
##print(pi(1000))
##print(pi(10000))
assert 3.04 < pi(10) < 3.05
##assert 3.13 < pi(100) < 3.14
##assert 3.140 < pi(1000) < 3.141
##assert 3.1414 < pi(10000) < 3.1415
print('ok')

##itertools模块提供的全部是处理迭代功能的函数，
##它们的返回值不是list，而是Iterator，只有用for循环迭代的时候才真正计算。
