# 函数参数和返回值

# 函数返回多个值时是一个tuple

# 两数交换

a = 1
b = 3

# 解法一
c = a
a = b
b = c
print(a, b)

# 解法二
a = a + b
b = a - b
a = a - b
print(a, b)

# 解法三（利用元组）
a, b = b, a
print(a, b)

# 函数内部参数赋值不会影响外部实参
# 在函数内部使用方法可以修改全局的可变数据类型（dict，list）
gl_n = 9
gl_list = [1, 2, 3]


def demo(n):
    print(id(n))
    # n = 99
    gl_list.append(1)
    print(n, id(n))


# print(id(gl_n))
# demo(gl_n)
demo(gl_list)
print(gl_list)

# 列表 += 本质是调用.extend方法
num_list = ['a', '2']


def test(num=gl_n):
    num += num  # 本质是调用extend方法，影响外部数据


test(num_list)
print(num_list)
test()
print(gl_n)
# 函数的缺省参数,缺省参数必须在元组末尾（未缺省参数后面）

print(num_list.sort(reverse=True))  # 默认升序，传入reverse参数降序


def info(name, gender=True):
    gender_text = '男生'
    if not gender:
        gender_text = '女生'
    print('%s是%s' % (name, gender_text))


info('a')

# 多值参数  *args 可以接受元组 **args 可以接受字典， 关键字参数


def p(aa, bb=None, *args, **kwargs):
    print('=' * 30)
    print(aa)
    print(bb)
    print(args)
    print(kwargs)


p((1, 2, 3), {1: 1, 2: 2})
