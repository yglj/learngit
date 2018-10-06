# 私有属性，私有方法 （不是真正意义的私有，而是作改名处理 _类名__私有方法名）
# 不通过对象直接访问，而是通过对象的方法访问


class Women:
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def __secret(self):
        print('%s今年%d岁' % (self.name, self.__age))

    def allow(self):
        return self.__secret()


x = Women('x小姐')  # type: Women
# print(x.__secret()) 错误的访问方式
x.allow()
# 伪私有方法，属性
x._Women__secret()
print(x._Women__age)