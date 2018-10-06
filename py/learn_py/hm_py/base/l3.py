# 局部变量，全局变量

g_num = 99
a = []


def demo1():
    num = 90
    print('全局变量num：%d' % num)


def demo2():
    # 在函数内部不能给全局变量赋值语句,如果使用全局变量的赋值语句，会定义同名局部变量
    # 如果要修改全局变量，使用关键字global申明变量名
    a.append(1)
    global g_num
    g_num = 0
    print(id(g_num))
    print('全局变量：%d' % g_num)


demo1()
demo2()
print(id(g_num))