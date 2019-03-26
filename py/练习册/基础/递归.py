def f(n):#递归调用
    if n==1:
        return n
    else:
        return f(n-1)*n
print(f(989))
print(f(2))
print(f(3))        

def fc(n):  #尾调用
    return fc(n,1)

def fa_iter(n,p):
    if n==1:
        return p
    return fc_iter(n-1,n*p)
print(fc(100))
