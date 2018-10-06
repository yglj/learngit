'''
1.无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。
如果是数字，我们可以直接比较，


2.但如果是字符串或者两个dict呢？直接比较数学上的大小是没有意义的，
因此，比较的过程必须通过函数抽象出来。
'''

#1.Python内置的sorted()函数就可以对list进行排序：
print(sorted([36, 5, -12, 9, -21]))    #[-21, -12, 5, 9, 36]


#sorted()函数也是一个高阶函数
#它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
print(sorted([36, 5, -12, 9, -21], key=abs))   #[5, 9, -12, -21, 36]

#给sorted传入key函数，即可实现忽略大小写的排序：

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)) #['about', 'bob', 'Credit', 'Zoo']


#2.要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)) #['Zoo', 'Credit', 'bob', 'about']

#用sorted()排序的关键在于实现一个映射函数    按照某种方法来排序
