# for i in range(1, 10):
#     for j in range(1, i + 1):
#         # if j<=i:
#         print("{}*{}={}".format(i, j, i * j), end=" ")
#     print()
l = ["%d*%d=%d"%(i,j,i*j) for i in range(1,10) for j in range(1,i+1)]
print(l)