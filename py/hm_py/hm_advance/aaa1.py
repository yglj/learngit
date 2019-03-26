from functools import reduce

print(reduce(lambda a, b: a+b, list(range(101))))

print(reduce(lambda a, b: a*b, list(range(1, 11))))

jie = 0
for i in range(1, 11):
    jie += reduce(lambda a, b: a*b, list(range(1, i+1)))
print(jie)


for i in range(100, 1000):
    x = i // 100
    y = i % 100 // 10
    z = i % 100 % 10
    print(x, y, z, i) if pow(x, 3) + pow(y, 3) + pow(z, 3) == i else ''

ticket = True
knife = True

print('上火车')
if ticket:
    print('打印车票，可以进站')
    if knife:
        print('没收刀具，上车')
    else:
        print('直接上车')
else:
    print('没票，不能进站')