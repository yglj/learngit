#在条件为真的情况下， 重复执行语句块
i=0
while i<10:
    print (i)
    i=i+1
    
sum=0
i=0
while i<100:
#for i in range(0,100):
    i=i+1
    sum=sum+i
print(sum)
#你可以在 while	循环中使用  else 从句。
#True和False被称作布尔（Boolean）型，你可以将它们分别等价地视为1与0
num = 55
b = True
while b:
    guess = eval(input())
    if(guess == num):
        print("you are right")
        b = False
    elif(guess < num):
        print("less")
    elif(guess > num):
        print("bigger")
else:
    print('over')
    
print('done')
