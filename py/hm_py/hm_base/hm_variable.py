
def demo1():
    # 1. 苹果重量
    weight = 10

    # 2. 苹果单价
    price = 2.5

    # 3. 需要支付价钱
    money = weight * price

    print(money)

    print(type(0))

    print(type(True))


def demo2():
    a = 'x'
    b = 'b'
    print((a + b) * 10)

    password = float(input("请输入密码："))

    print(type(password))

    print(password)


def demo3():
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


