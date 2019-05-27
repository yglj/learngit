# 渐进时间复杂度：T(n) = O(f(n))
#随着输入规模的增大，公式重常量，系数，低阶项并不影响增长趋势


def cal_1(n):
    i = 0
    sum = 0
    for i in range(n + 1):  
        sum += i  # 需要n个unit_time执行时间
    return sum
# 总执行时间： (2n +2 )*unit_time
# O(n)


def cal_2(n):
    i = 1
    j = 1
    sum = 0
    for i in range(n + 1):
        j = 1
        for j in range(n + 1):
            sum += (i * j)
# 总执行时间： (2n^2 + 2n + 3)*unit_time
# O(n^2)


if __name__ == '__main__':
    n = 0
    cal_1(n)
    cal_2(n)



        
    
