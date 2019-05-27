#输出第n项
def fib_index(n):
    a,b,c = 0,1,0
    if (n == 0):
        return a
    elif (n == 1):
        return b
    else :
        for i in range(n-1):
            c = a+b
            a,b = b,c
        return c
result = fib_index(5)
#print(result)
#输出n项
def fib1(n):
    a,b,c = 0,1,0
    if  n == 0:
        print(a)
    elif  n==1:
        print(b)
    else:
        l = [a,b]
        while n>=2:
            c = a+b
            a,b = b,c
            n-=1
            l.append(c)
        return l
result = fib1(5)
print(result)
#递归实现
def fib2(n):
    if  n==0:
        return 0
    elif  n==1:
        return 1
    else:
        while(n>=2):
            return fib2(n-1)+fib2(n-2)
result = fib2(5)
print(result)