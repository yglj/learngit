def A(num):
    count =0
    s=0
    a = num
    while a > 0:
        a//=10
        count+=1
        #print(a,count)
    a = num
    while a/10 > 0:
        b = a%10;
        a //= 10;
        s += pow(b,count)
        #print(s)
    if s==num:
        return s

result = A(153)
#print(result)
def search_A(n):
    for i in range(n+1):
        if i == A(i):
            print(i,end=" ")

search_A(1000)

#方法2
num = int(input("输入"))
n = len(str(num))
temp =num
s=0
while temp >0:
    digit = temp % 10;
    temp //= 10;
    s += digit**n
if s == num:
    print(True)
else:
    print(False)