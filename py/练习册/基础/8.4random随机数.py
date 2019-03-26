from random import randint
def e(n,m):
    if answer<num:
        print('to small')
        return False
    if answer>num:
           print('to big')
           return False
    if answer==num:
             print('equal')
             print('%d is right'%answer)
             return True
num = randint(1,100)                 
binggo=False
print('kill')
while binggo==False:
     answer=int(input())  
     binggo=e(answer,num)
