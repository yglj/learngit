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

# is用于判断是不是引用同一个对象
# ==用于判断引用变量值是否相等

a = [1, 2]
b = [1, 2, 3]
print(id(a), id(b))
a.append(3)
print(a == b)
print(a is b)


class Soldier:
    def __init__(self, name):
        self.name = name
        self.gun = None

    def fire(self):
        if self.gun is None:
            print('%s 还没有枪' % self.name)
        else:
            print('%s 冲啊、、、' % self.name)
            print('[%s]....biu,biu,biu' % self.gun.name)


class Gun:

    def __init__(self, name):
        self.name = name
        self.num = 0

    def add_bullet(self, num):
        self.num = num
        print('装入%s颗子弹' % self.num)


gun = Gun('ak47')
xiao = Soldier('xiao')
xiao.gun = gun
xiao.fire()
