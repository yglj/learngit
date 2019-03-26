
# 抛出异常： 程序停止执行，并提示错误信息

# 捕获异常： 针对可能出错的代码

# try:            # 尝试代码
#     n = int(input('请输入一个整数：'))
#     10 / n
#     # n + 'a'
# except ZeroDivisionError as z:    # 异常处理对象
#     print(z)
# except ValueError as e:
#     print(e)
# except Exception as e:
#     print('未知错误:%s' % e)
# else:
#     print('没有出现异常时执行')
# finally:
#     print('无论是否出现异常，都会执行')

print('-' * 30)

# 异常的传递： 函数、方法出现异常时会传递给调用方，最后传到主函数 （异常栈）

# 根据需求主动抛出异常raise


def input_password():
    pwd = input('请输入密码:')
    if len(pwd) >= 8:
        return pwd
    print('抛出异常')
    raise Exception('密码长度不够')  # 利用异常限制用户输入,不再向下执行


try:
    input_password()
except Exception as e:
    print(e)

