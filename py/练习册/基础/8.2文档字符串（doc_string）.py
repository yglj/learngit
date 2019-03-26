def product(*y):
    '''
    一个函数将传入的参数相乘

    *y 可变参数 实参传入一个元组
    用i遍历元组的每个值与x相乘结果回传给x
    返回x
    '''
    x=1
    for i in y:
        x=x*i
    return x
print(product())


print("1:",product(5))
print("1:",product(5))
print('3:',product(5,6,7))
print('4:',product(5,6,7,9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
  try:                        
    product()               
  except TypeError:           
    print('测试失败!')          
  else:                       
    print('测试成功')

print(product.__doc__)
help(product)
