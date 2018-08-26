'''
生成器
通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
这样就不必创建完整的list，从而节省大量的空间。
在Python中，这种一边循环一边计算的机制，称为生成器：generator。
'''
#要创建一个generator，有很多种方法。
#第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
l=[x for x in range(11)]
g=(x for x in range(11))

print(type(l),type(g))
'''
try:
 for i in range(12):
   print(next(g))
except:
    pass
'''
next(g)
for n in g:
    print(n)
#generator保存的是算法,每次调用next(g)，就计算出g的下一个元素的值，
#直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误


#斐波拉契数列 第二种方法
def fibonacci(sum):
    n,a,b=0,0,1
    while n<sum:
        yield b    #函数定义中包含yield关键字，不再是普通函数，而是generator
        print('第%s个数'%(n+1))
 #       print(b,end=' ')
        a,b=b, a+b
        n+=1
    return 'done'
    
f=fibonacci(3)    #f指向：返回的一个生成器对象
print(type(f))
for i in range(3):
  next(f)

g=fibonacci(6)
while 1:
    try:
        x=next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generator return vlaue:',e.value)
        break

#想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中        
#循环过程中不断调用yield，就会不断中断
#generator 遇到 yield返回，再次执行从上次返回的yield 处继续
#赋值语句：a, b = b, a + b
#相当于：t = (b, a + b) # t是一个tuple a = t[0] b = t[1]
