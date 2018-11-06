"""
实例属性，实例方法 ---- 类属性，类方法
每一个对象的方法属性，保存在各自独立的内存空间，调用方法时要传入对象的引用地址
类是特殊的对象 class xxx 定义的是类对象 ，在内存中只有一份， 可以创建多个实例对象
类对象拥有自己的属性，对_in象
"""


class Test:

    count = 0  # 类属性

    def __init__(self, name):
        self.name = name
        Test.count += 1

    @classmethod   # 修饰器，告诉解释器这是类方法
    def func(cls):  # cls，类的引用地址
        print('创建的对象数量： %s' % cls.count)

    @staticmethod  # 静态方法 不需要指定self参数
    def static():  # 不访问实例属性，方法 ， 类属性，类方法， 应该封装成静态方法
        print('{}'.format(1))


Test.static()
t1 = Test(1)
t2 = Test(2)
t3 = Test(3)
print(t3.count)  # 不建议用对象访问类方法， 访问属性时会先从对象属性中找，再从类方法中找
Test.func()


class Player:

    top_score = 9

    def __init__(self, name):
        self.name = name

    @staticmethod
    def show_help():
        print('帮助指南 ....')

    @classmethod
    def show_top(cls):
        print('历史最高分:%s' % cls.top_score)

    def start_game(self):
        print('%s,欢迎进入游戏...' % self.name)


Player.show_help()
Player.show_top()
p = Player('xxx')
p.start_game()
