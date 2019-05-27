a = 54
b = 24
if a > b:
    c = b
else:
    c = a
y = 0
for i in range(1,c+1):
    if a%i == 0 and b%i == 0:
        y = i
        #print("公约数：",i)
print("最大公约数",y)


print(6>7 and 7 or 6)
print(7>6 and 7 or 6)