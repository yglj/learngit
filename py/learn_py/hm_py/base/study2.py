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