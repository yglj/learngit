#方法1：递归
def M(n):
    if(n == 0):
        return  0
    elif(n == 1):
        return 1
    else:
        return n*M(n-1)
#n = int(input("阶乘数："))
#print(M(n))

#方法2：遍历
def M2():
    n = int(input("阶乘数："))
    if n<0:
        print("负数没有阶乘")
    elif n==0:
        print("0的阶乘为0")
    else:
        f = 1
        for i in range(1,n+1):
            f *=i
        print("{}的阶乘为：{}".format(n,f))
M2()