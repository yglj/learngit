
class Parent(object):
    def __init__(self, *args, **kwargs): # 为了避免报错，使用不定长参数，接收参数
        print('Parent的__init__方法')

    def test(self):
        pass


class Son(Parent):
    def __init__(self, name, *args, **kwargs):
        print('Son的__init__方法')
        super().__init__(name, *args, **kwargs)
        self.name = name


class Daughter(Parent):
    def __init__(self, age,  *args, **kwargs):
        print('Daughter的__init__方法')
        super().__init__(age, *args, **kwargs)
        self.age = age


class GrandSon(Son, Daughter):
    def __init__(self, name, age):
        print('GrandSon的__init__方法')
        super(GrandSon, self).__init__(name, age)


if __name__ == '__main__':
    print(GrandSon.__mro__)
    g = GrandSon('aa', 18)
