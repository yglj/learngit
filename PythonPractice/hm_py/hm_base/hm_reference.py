# 变量的引用及是否可变
# 变量和数据分开存储，变量记录数据的地址引用
# id()查看变量在内存中的地址


a = 1
b = a
print(id(1) == id(a) == id(b))  # 数据1， a , b , 1 的内存地址相同
print(id(a))
print(id(b))

# 函数参数和返回值的通过引用传递


def test(num):
    print('函数接收的参数%d的保存的内存地址:%d ' % (num,id(num)))
    result = 'address'
    print('函数返回值的内存地址:%d' % id(result))
    return result


n = 10
print('变量n的保存数据的内存地址:%d' % id(n))
result = test(n)
print('变量获得函数返回值的地址:%d' % id(result))

# 可变和不可变数据类型 （内存中的数据不允许修改）
# 字典的ｋｅｙ只能使用不可变数据类型（ｌｉｓｔ，ｄｉｃｔ）　
# 不可变数据类型： 字符串，数字，元组
print({'(1,)': 'xx'})


# 哈希 hash()
# 接受不可变类型，提取特征码，相同的内容会得到相同的的结果,可以判断数据是否相同
print(hash((1,)))