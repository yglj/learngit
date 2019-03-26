from functools import reduce
'''
reduce
参数1：函数or匿名函数（必须接收两个参数）
参数2：:一个序列[x1, x2, x3, ...]，

把序列上的元素作参作用于函数，把返回结果继续和序列的下一个元素做累积计算
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
'''
#累加
def add(x,y):
    return x+y
a=reduce(add,[1,3,5,7,9])  #等价于sum([1,3,5,7,9]) 
print(a)
a=reduce(lambda x,y:x+y,list(range(101))) #用匿名函数简化


#把序列[1, 3, 5, 7, 9]变换成整数13579
b=reduce(lambda x,y: x*10+y,[1,3,5,7,9])
print(b)


# 把str转换成int
def char(s):
    digtal={'0': 0, '1': 1,'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digtal[s]
def shi(x,y):
    return x*10+y
c=reduce(shi,map(char,'13579'))
print(c)

def str2int(s):  #简化为一个函数
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))
print("###################################")



'''
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s)) #用匿名函数再次简化
'''
