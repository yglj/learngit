a = 54
b = 24
c = a > b and a or b
while(c):
    if c%a == 0 and c%b == 0:
        break
    c+=1
print("最小公倍数",c)


