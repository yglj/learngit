# 逻辑行（；\隔开）物理行
"""
import math
from math import sqrt
a=1#int(input())  #输入接受字符串 ， 要类型转换
b=3#int(input())
c=4#int(input())

s1=(-b - sqrt(abs(pow(b,2)-4*a*c)))/2*a  #求二阶方程的根  sqrt()值为非负数
s2=(-b + sqrt(abs(pow(b,2)-4*a*c)))/2*a
print(s1,' ',s2)

b= eval(input())  #把字符串变为变量
a = int(input())
print(a+b)


"""
#输出

str='i'
str2='you'
print(str+' and '+str2)  #字符串连接 must be str, not int
num=18
print('my age is %d'%num)
name='li'
age=5
print('%s age is %d'%(name,age))
print()
# 格式化输出
print("{1} is {0} years old".format(age,name))
print('{0:.3f}'.format(1.0 / 3))
print("{0:_^11}".format("hello"))
print("{who} eat {food}".format(who="hi",food="fish"))

print("a",end='->')
print("b")

str=int(input('birth:',))
if str>2000:
    print("00后")
else:
    print('00')
