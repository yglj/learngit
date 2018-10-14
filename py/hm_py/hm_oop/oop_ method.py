# 面向过程： 逐步实现，封装函数 ，直接调用函数

# 面向对象： 对象中封装多个方法，让对象调用方法

# 类和对象 具有相同特征（属性）和行为（方法）的统一事物 ，类是模板，对象是类的实例

# 设计类->名词 ， 行为->动词

# 内置函数dir(),查看类的所有属性和方法

print(dir(object))
obj = object()
print(obj.__dir__())

# 一些特殊的方法
'''
__new__: 创建对象时自动调用
__init__:初始化对象时自动调用
__str__:返回 对象的描述信息
__del__:销毁函数时自动调用
'''

print(obj.__str__)


class Cat:

    def __init__(self, name):
        self.name = name
        print('%s被创建' % self.name)

    def eat(self):
        print('%s要吃鱼' % self.name)

    def drink(self):
        print('小猫要喝水')
        print(self)

    def __del__(self):
        print('%s的生命周期结束' % self.name)

    def __str__(self):
        return super.__str__(self) + '---小猫%s' % self.name


tom = Cat('Tom')
tom.drink()
tom.eat()

# 计算机常用16进制来输出内存地址 %x

# print(tom)
# print('%x' % id(tom))

# 在类的外部给对象增加属性,不推荐使用(隐患：找不到属性，调用方法时会报错)
tom.name = 'Tom-jack'
# print(dir(tom))
# print(tom.name)

# self参数，保存对象内存地址起始位置

# 初始化方法  使用类名（）创建对象时，会先分配空间，再设置初始值（__init__）
del tom
