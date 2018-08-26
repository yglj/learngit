# 遍历（iteration）可以通过for循环遍历一个可迭代对象
# 判断一个对象是否可迭代
from collections import Iterable
s=isinstance('abc',Iterable)
print(s)           
s=isinstance([1,2,3],Iterable)
print(s)
s=isinstance(123,Iterable)
print(s) 

#内置函数enumerate可以把list变成索引—元素对
for i,value in enumerate(['a','b','v']):
    print(i,value)

def findMinAndMax(L):
    if L==[]:
        return (None,None)
    min = max = L[0]
    for i in L:
        min = min < i and min or i
        max = max > i and max or i
    return (min,max)


if findMinAndMax([])!=(None,None):
    print('测试失败')
elif findMinAndMax([7])!=(7,7):
    print('测试失败')
elif findMinAndMax([7,1])!=(1,7):
    print('测试失败')
elif findMinAndMax([7,1,3,9,5])!=(1,9):
    print('测试失败')
else:
    print('测试成功！')

#插入排序
list=[1,3,2,5,6]

def findMinAndMax(list):
    for i in range(len(list)):
        for j in range(i):
            if list[i]<list[j]:
                #print(list)
                list.insert(j, list.pop(i))
                #print(list)
    return(list[-1],list[0])

print(findMinAndMax(list))
#print(list.pop(2),list)


