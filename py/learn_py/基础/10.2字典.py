#字典
#无序 键值必须是唯一
score={
    '长孙':95,
    '慕容': 97,
    '上虞': 89
    }
print(score['长孙'])

for name in  score:
   print(name,score[name],":")


n={'a':45,'b':56,'c':64} 
print('a' in n)        
print(n.get('v',None))
print(n.pop('c'))
print(n)
del n['a']
print(n)




