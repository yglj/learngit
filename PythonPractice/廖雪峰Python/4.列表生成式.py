
list(range(0,10,2))
[x*x for x in range(1,11)if x % 2 ==0] #生成[1x1, 2x2, 3x3, ..., 10x10]
[m+n for m in 'abc' for n in 'abc']  #嵌套，两层循环
import os
[d for d in os.listdir()] # os.listdir可以列出文件和目录

d={'x':'a','y':'b','v':'c'}  #使用两个变量来生成list
[k+'='+v for k,v in d.items()]

#把一个list中所有的字符串变成小写：

L = ['Hello', 'World', 'IBM', 'Apple']
[s.lower() for s in L]
['hello', 'world', 'ibm', 'apple']

#字典  生成式
t={k:L[k]  for k in range(len(L))}
print(t)
