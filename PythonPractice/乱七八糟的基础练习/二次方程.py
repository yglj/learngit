import cmath
def f(a,b,c):
    d = b**2 - 4*a*c
    x1 =( -b + cmath.sqrt(d))/(2*a)
    x2 =( -b + cmath.sqrt(d))/(2*a)
    print("解：x1:{0},x2:{1}".format(x1,x2))
f(2,3,4)
