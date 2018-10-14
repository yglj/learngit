# 继承，多态，封装

# 重写子类方法覆盖父类同名方法，对父类的方法扩展
# super 父类引用,用于调用父类的方法


class Animal:
    def __init__(self):
        pass

    def eat(self):
        pass

    def drink(self):
        pass

    def run(self):
        pass

    def bark(self):
        pass


class Dog(Animal):
    def bark(self):
        print('汪汪叫～～')


class SmartDog(Dog):
    def bark(self):
        print('我是一只聪明的小狗')
        # super.bark()
        Dog.bark(self)  # 类名.方法名（self） 不推荐使用


xtq = SmartDog()
xtq.bark()