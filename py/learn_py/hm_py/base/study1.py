# 字符串


def p(*exp):
    for i in exp:
        print(i)
        print('-'*30)


# len()  长度
# .count() 统计
# .index() 索引
# 判断方法 .is*()


space_str = '  \r \n \t'
p(space_str.isspace())
# 查找替换 .find() .replace()


r_str = '  sheng si mo mei '
p(r_str.startswith('s'), r_str.endswith('i'))
p(r_str.replace('mei', 'xxx'))  # 不会修改原有字符串的内容

# 大小写转换
# 文本对齐 .ljust() .rjust() .center()
p(r_str.ljust(10))
poem = ['\t\n春晓',
        '杜甫 ',
        '春眠不觉晓\t\n',
        '处处闻啼鸟',
        '夜来风雨声']

for item in poem:
    item = item.strip()
    p('|%s|' % (item.center(10, '-')))


# 去除空白符
# 拆分、连接

poem2 = '白日依山尽\t黄河入海流\t\n欲穷千里目   更上一层楼'

poem2 = poem2.split()
p('\n'.join(poem2))

# 切片      使用索引值限定字符串范围

num_str = '0123456789'

p(num_str[::-1])
p(num_str[2:6], num_str[2:], num_str[:6], num_str[1::-1], num_str[-2:])
