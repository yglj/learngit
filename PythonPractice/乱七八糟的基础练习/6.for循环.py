'''
#for...in循环语句，在一系列对象上进行迭代（Iterates），遍历序列中的每一个项目

for i in range(0,5):
    for j in range(0,i+1):
        print('*',end=' ')
    print()

i=bool('False')
#Returns True when the argument x is true, False otherwise(0,None,False),
#is a subclass of the class int
print(i)
a=input('moolk')
print(a)
'''
for i in range(1,10):   #range()生成数字序列 左开右闭
    for j in range(1,i+1):
        print(i,'*',j,end=" ")  #语句用（‘ ’）隔开
    print()            #换行

else:
    print("九九乘法表")
