# 非数字型变量： 列表，字典，集合，字符串，元组
# 序列(sequence)/容器
# 遍历 for...in...
# 长度，大小 ，比较，删除
# 链接+ ， 重复*
# 切片[]

# 列表一般存储相同数据类型

alist = ['a', 1, True, 'b', 'a']

b = list(('a', 'b'))
print(b)

# 增加：.insert() .append() .extend()

# 修改： list[index]  list.index()

# 删除： del list[index]  .remove() .pop() .clear()

# 排序： .sort(reverse = False) .reverse()
print(alist.reverse(), alist)

# 统计： .count() len(list)

print(alist.count('a'))
# del 将变量从内存中删除

# 方法与函数类似，方法通过对象调用，针对对象的操作，从属于对象

# 遍历，可迭代对象iterable 迭代器iterator 可重复遍历

it_list = iter(alist)

for item in it_list:
    print(item)

print('+' * 50)

for item in alist:
    print(item)


def p(*args):
    print(args)
    print('-'*20)


out = print

out(1)


# python 内置函数
# len(), del(), max(), min(), p3取消了cmp()

p('1' < 'A')
p('A' > 'a')

# * 重复， + 拼接 ， in ， == ， 等运算符
a = [1,2]
p([1, 2] > [0, 1])
p([1, 2] + [3, 4])  # 合并成新的列表
p([1, 2].extend([3, 4]))  # 在原有列表上扩展
a.append([3, 4])   # 追加
p(a)
p(1 in [1, 2])


# for...in...else...


for i in [1, 2, 3]:
    print(i)
    if i == 2:
        break
else:
    print('break 退出后不执行else中语句')
