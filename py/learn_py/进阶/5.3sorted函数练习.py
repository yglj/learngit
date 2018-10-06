# 把要排序列先按key 中方法处理，再按处理后的序列排序号
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
     return t  #t[0]

L2 = sorted(L, key=by_name)
print(L2)
def by_score(t):
     t = -t[1]
     #print(t)
     return t
L2 = sorted(L, key=by_score)
print(L2)
