f=open('score.txt')
lines=f.readlines()
results=[]
#print(lines)
f.close()

for line in lines:
  #  print(line)
    data=line.split()
   # print(data)

    sum=0
    for  score in data[1:]:
        point=60
        if point>int(score):
            continue
        sum+=int(score)
    result='%s\t:%d\n'%(data[0],sum)
    #print (result)
 
    results.append(result)

    print(results)

output=open('result.txt','w')
output.writelines(results)
output.close()
    


