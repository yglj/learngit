from collections import namedtuple,deque,defaultdict,OrderedDict
point = namedtuple('Point',['x','y'])
p = point(1,2)
print(p.x,p.y)

q=deque(['a','b','c'])
print(q.append('x'),q.appendleft('y'))
print(q)
print(q.pop(),q.popleft())

d=defaultdict(lambda: 'bucunzai')
d['a']=1
print(d['a'])
print(d['c'])

dd=dict([('b',1),('a',2),('c',3)])
print(dd)
ddd=OrderedDict([('b',1),('a',2),('c',3)])
print(ddd)
print(isinstance(dd,dict))


