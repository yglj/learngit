'''
1.默认参数值
2.关键字参数：使用命 名（关键字）而非位置指定
 不再需要考虑参数的顺序，可以对需要的参数赋值（其他默认）
3.可变参数  参数数量可变，
   *param的星号参数时，从此处开始直到结束的所有位置参数（Positional Arguments）
    都将被收集并汇集成一个称为“param”的元组（Tuple）
    	**param	的双星号参数时，从此处开始直至结束的所有关键字
    	参数都将被收集并汇集成一个名为param的字典（Dictionary
4.return 语句 返回值，结束函数
5.None（虚无） 指变量没有值
6.pass语句用于指示一个没有内容的语句块
'''
def fun(a , b = 0, c= 1):
    print("a=",a,"b=",b,"c=",c)
a = 1
b = 2
c = 3
fun(a,b,c)
fun(2,3,4)
fun(c = 100,a = c) # 指定关键字a,c ，而非位置

def f(a,b,c=0,*args,**kw):
    print('a=',a,'b',b,'c=',c,'args=',args,'kw=',kw)

args=(1,2,3)   #从左到右按顺序指定 a=1, b= 2, c=3
kw={
    'x':'X',
    'y':'Y'
    }
f(*args,**kw)
def f1(a,b,c=0,*,y,**kw):
    print('a=',a,'b',b,'c=',c,'y=',y,'kw=',kw)

args=(1,2,3)
kw={
    'x':'X',
    'y':'Y'
    }
f1(*args,**kw)
