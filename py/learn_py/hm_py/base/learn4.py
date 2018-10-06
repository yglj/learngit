# 1.苹果的单价
price = input('请输入苹果的单价:')

# 2.苹果的重量
weight = input('请输入苹果的重量:')

price = float(price)  # 类型转换

weight = float(weight)

# 3.苹果的总价
money = weight / price

print('已购买苹果，花费%0.2f元' % round(money, 2))

print('%02d' % 1234567)
