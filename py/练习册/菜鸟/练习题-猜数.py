name=eval(input('请输入姓名：'))

f=open('game.txt')
#score=f.read().split()
lines=f.readlines()
f.close()

scores={}
for i in lines:
    s=i.split()
    scores[s[0]]=s[1:]
score=scores.get(name)
if score is None:
   score =[0,0,0]
   
game_times=int(score[0])
min_times=int(score[1])
total_times=int(score[2])
if game_times>0:
   avg_times=float(total_times)/game_times
else:
    avg_times=0
print('%s,你已经玩了%d次，最少%d轮猜出答案，平均%.2f轮猜出答案'%(name,game_times,\
                                        min_times,avg_times))

from random import randint
num=randint(1,100)
print('Guess what i think ')

def e(n,m):
    if answer<num:
        print('to small')
        return False;
    elif answer>num:
        print('to big')
        return False
    else :
       print('equal')
       print('%d is right'%answer)
       return num
answer=0
t=0
while answer!=num:
     answer=int(input())
     if answer<0:
       print('Exit game...')
       break
     e(answer,num)
     t+=1
if game_times==0 or t<min_times :
        min_times=t
total_times+=t
game_times+=1

scores[name]=[str(game_times),str(min_times),str(total_times)]
#result='%d %d %d'%(game_times,min_times,total_times)
result=' '
for n in scores:
    line=n+' '+' '.join(scores[n])+'\n'
    result+=line
print(result)
f=open('game.txt','w')
f.write(result)
f.close()
