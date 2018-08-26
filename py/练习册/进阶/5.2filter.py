'''
内建的filter()函数用于过滤序列  (对序列作筛选，保留符合要求的)
接收一个函数和一个序列

filter()把传入的函数依次作用于每个元素，
#然后根据返回值是True还是False决定保留还是丢弃该元素。


返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，
需要用list()函数获得所有结果并返回list。
'''
'''

#在一个list中，删掉偶数，只保留奇数

def is_odd(list):
    return list% 2 ==1

print(list(filter(is_odd,[1,2,3,4,56,74])))

#把一个序列中的空字符串删掉，可以这么写：

def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

'''

#用filter求素数,计算素数的一个方法是埃氏筛法
def _odd_iter():  #奇数生成器，无限序列
    n = 1
    while True:
        n = n + 2
        yield n
##        if n > 1000:
##            break
        
def _not_divisible(n):  #筛选函数
    return lambda x: x % n >0   #等价于 x%3！=0 排除能被n整除的数

def primes():   # 无限序列
    yield 2
    it = _odd_iter() # 初始序列，从3开始的奇数列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        #print("list:",list(it)) #不能输出一个无限序列（生成器），电脑爆炸
        it = filter(_not_divisible(n), it) #传n到高阶函数返回一个匿名函数作函数参数
        #返回值为排除n的倍数后的无限奇数列（生成器）

a=primes()
for i in range(10):
  print(next(a))


for n in primes():
    if n < 1000:
        print(n)
    else:
        break


