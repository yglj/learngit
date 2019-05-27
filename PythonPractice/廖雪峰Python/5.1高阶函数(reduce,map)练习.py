#规范英文名
#n=eval(input())
#print(n,type(n))
def normalize(name):
    #name = name.capitalize()
    #name = name.title()
    print(name)
    return name

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

#第二题：累积求积
from functools import reduce
def prod(list):
    return reduce(lambda x,y:x*y,list)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
    
#第三题：把字符串变成浮点数
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def char2num(s):
    return DIGITS[s]  #可用ord（s）-ord（'0'）代替

def str2float(s):
    a = (s.split('.'))[0]
    b = (s.split('.'))[1]  
    c = reduce(lambda x, y: x * 10 + y, map(char2num, b)) / (10**len(b))
    return reduce(lambda x, y: x * 10 + y, map(char2num, a))+c

#    return eval(s)
print('str2float(\'123.456\') =', str2float('123.456'))

if abs(str2float('123.456') - 123.456) < 0.00001: #涉及到浮点数在计算机中的储存
    print('测试成功!')
else:
    print('测试失败!')
