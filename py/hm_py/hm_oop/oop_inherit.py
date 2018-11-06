# 多继承


class A:
    def test(self):
        print('A test')

    def demo(self):
        print('A test')


class B:
    def test(self):
        print('B test')

    def demo(self):
        print('B test')


class C(B, A):
    pass


c = C()
c.test()
c.demo()
print(C.__mro__)  # MRO方法搜索顺序， 用于多继承判断方法，属性调用路径


# object 是所有对象的默认基类  新式类