'''
可以直接作用于for循环的对象统称为可迭代对象：Iterable
可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
可以使用isinstance()判断一个对象是否是Iterator对象

#生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。

把list、dict、str等Iterable变成Iterator可以使用iter()函数
Iterator甚至可以表示一个无限大的数据流，
例如全体自然数。而使用list是永远不可能存储全体自然数的

1.凡是可作用于for循环的对象都是Iterable类型；
2.凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
3.集合数据类型如list、dict、str等是Iterable但不是Iterator，
4.可以通过iter()函数获得一个Iterator对象。

可迭代对象（list...）>迭代器（next（）） > 生成器（yield）
Python的for循环本质上就是通过不断调用next()函数实现的

'''
for x in [1,2,3,4,5]:
    pass
#等价于
it=iter([1,2,3,4,5])  # 首先把list变成迭代器（iter（））
while True:
    try:
        x=next(it)   # 获得下一个值
    except StopIteration:  # 遇到StopIteration就退出循环
        break
