i=0
while i<5:
    print("第%d次"%(i+1))
    i+=1
    for j in range(3):
      print('j=',j)
      if j==2:
        break             #中止循环语句的执行
    for k in range(4):
      if k==2:
        continue         #跳过当前循环块中的剩余语句，并继续该循环的下一次迭代。
      print('k=',k)
    if i>3:
     break
    print("i=",i)
