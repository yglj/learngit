#集合（Set）是简单对象的无序集合（Collection
s=set([1,2,4,1,3,2])
print(s)
s={1,2,3,1}
s.add(4)       #add
print(s)
s.remove(4)    #移除
print(s)

s1 = set([1, 1, 2, 2, 3, 3])
print(s1)
s2 = set([2, 3, 4])
print(s1 & s2)         #交集
print(s1 | s2)         #并集

bri = set(['brazil','russia', 'india'])
'india'	in bri
'usa'in	bri 
bric = bri.copy() 
bric.add('china')
print(bric.issuperset(bri))
bri.remove('russia')
print(bri.intersection(bric))#交集
