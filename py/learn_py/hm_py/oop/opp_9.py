# 单例设计模式
# 类只有创建唯一个对象实例
# 应用场景： 打印机，回收站，音乐播放对象
# __new__() object提供的内置静态方法，作用：为对象分配空间，返回对象引用


class MusicPlayer:
    __init_flag = False
    instance = None

    def __new__(cls, *args):
        if cls.instance is None:  # 利用__new__只分配一次对象空间,来实现单例
            print('创建对象时，自动分配空间')
            cls.instance = super().__new__(cls)
            # print(instance)
            return cls.instance   # 返回对象引用
        return cls.instance

    def __init__(self):  # 让初始化动作只执行一次：利用标志位控制
        if MusicPlayer.__init_flag:
            return
        print('初始化对象，分配实例对象属性')
        MusicPlayer.__init_flag = True


m = MusicPlayer()
print('-' * 30)
m2 = MusicPlayer()

