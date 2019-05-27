import io
f = open("a.txt",'w',encoding="utf-8")
text = """
        hi
        hii
        hiiii
        hiiiiiii
       """
f.write(text)
f.write(u'#########')
f.close()

f = open("a.txt",'r')
while True:
    line = f.readline()
    if(len(line) == 0):
        break
    print(line,end='')
f.close()

with open('a.txt','r') as f:
    while True:
        l = f.read(100)
        if (len(l) == 0):
            break
        print(l)

context = io.open('a.txt','r',encoding='utf-8').read(1024)
print(context)