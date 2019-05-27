'''
print('who do you think i am')
you=input()
print('oh,yes! i am a')
print(you)
'''
'''
l=[5,'everyone',0.53,True]
print(l[1])
print(l[1:-1])
'''
from random import choice
score=[0,0]
direction=['left','center','right']
def kick():
 for i in range(1,6):
    print('======Round%d-You Kick!====='%i)
    print('left,center,right')
    you=input()
    print('You KicKed '+you)
    com=choice(direction)
    print('Computer saved '+com)
    if  you!=com:
        score[0]+=1
        print("Goal!")
    else:
        print('Oops...')
    print('Socre:%d(you)-%d(com)\n'%(score[0],score[1]))


    print('======Round%d-You Saved!====='%i)
    print('left,center,right')
    you=input()
    print('you saved '+you)
    com=choice(direction)
    print('computer kicked '+com)
    if you==com:
     print("saved!")
    else:
        print('Oops...')
        score[1]+=1
    print('Socre:%d(you)-%d(com)\n'%(score[0],score[1]))


i=1
print('===Round %d ===='%i)
kick()
while score[0]==score[1]:
    i+=1
    print('====Round %d ===='%i)
    kick()

if score[0]>score[1]:
    print('you win!')
else :
    
   print('you lose!')
    
  
