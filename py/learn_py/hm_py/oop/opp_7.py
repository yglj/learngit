# 多态 不同的子类对象调用父类方法，执行结果不同 ，以继承和重写为前提


class Dog:
    def __init__(self, name):
        self.name = name


class FlyDog(Dog):
    pass


class LazyDog(Dog):
    pass


class Person:
    def __init__(self, name):
        self.name = name

    def liu_gou(self, dog):  # 不用关心具体的狗的类型
        print('%s and %s play patch game' % (self.name, dog.name))


f = FlyDog('废狗')
l = LazyDog('懒狗')

p = Person('小明')
p.liu_gou(f)
p.liu_gou(l)