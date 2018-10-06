class Test1(object):
     __slots__ = ('attr1')
print('\nThis is Test1\n')

test1_a = Test1()
test1_a.attr1 = ["I'm instance test1_a"]
print('test1_a.attr1 = ', test1_a.attr1)

test1_b = Test1()
test1_b.attr1 = ["I'm instance test1_b"]
print('test1_a.attr1 = ', test1_a.attr1) #这里类未绑定属性，不发生改变           注释（1）
print('test1_b.attr1 = ', test1_b.attr1)

Test1.attr1 = ["Hello World"]
print('\nTest1 speak:Follow me change!') #这里添加类属型，实例属性发生改变   注释（2）
print('Test1.attr1 =', Test1.attr1)
print('test1_a.attr1 = ', test1_a.attr1)
print('test1_b.attr1 = ', test1_b.attr1)

test1_a.attr1.append("I have changed……")
print('\ntest1_a speak:Follow me change!') #这里实例修改属性，所有实例发生变化  注释（3）
print('Test1.attr1 =', Test1.attr1)
print('test1_a.attr1 = ', test1_a.attr1)
print('test1_b.attr1 = ', test1_b.attr1)

test1_b.attr1.append("I have changed……")
print('\ntest1_b speak:Follow me change!') #另一个实例改变属性值  注释（3）
print('Test1.attr1 =', Test1.attr1)
print('test1_a.attr1 = ', test1_a.attr1)
print('test1_b.attr1 = ', test1_b.attr1)



class Test2(object):
     def __init__(self):
          pass
print('\nThis is Test2\n')

test2_a = Test2()
test2_a.attr1 = "I'm instance test2_a" #修改无影响
Test2.attr1 = "I'm class Test2"
print('test2_a.attr1 = ', test2_a.attr1)
print('Test2_attr1 =', Test2.attr1)

print('\n')
test2_b = Test2()
test2_b.attr1 = "I'm instance test2_b" #修改实例属性无影响
print('test_a.attr1 = ', test2_a.attr1)
print('test_b.attr1 = ', test2_b.attr1)
print('Test2.attr1 = ', Test2.attr1)

print('\n')
Test2.attr1 = "Hello World" #修改类影响
print('Test2.attr1 =', Test2.attr1)
print('test2_a.attr1 = ', test2_a.attr1)
print('test2_b.attr1 = ', test2_b.attr1)
