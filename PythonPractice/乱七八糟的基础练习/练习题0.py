l = [1,2,3,4]
for i in l:
    for j in l:
        for k in  l:
            if(i != j and i!=k and j!=k):
                print(i*100+j*10+k)
