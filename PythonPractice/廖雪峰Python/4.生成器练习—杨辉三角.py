def triangles1():
    result = [1]
    yield result		
    while True:
        t = [1]  #浅拷贝，t与result存放同一个地址
        for i in range(1,len(result)):
            t.append(result[i-1] + result[i])
        t.append(1)
        result = t   #print("t",t,result)
        yield result
#  二
def triangles2():
    result = [1]
    yield result		
    while True:
        t = result[:]  #深拷贝
        for i in range(1,len(result)):
            t[i]=result[i-1] + result[i]
        t.append(1)
        result = t[:]   #print("t",t,result)
        yield result
# 三 测试失败？
def triangles():
    t = [1]
    while True:
        yield t
        r = t[:]
        r.append(0)
        t = [r[i]+r[i-1] for i in range(len(r))]
        

def triangles3():  # 插入法
    yield [1]
    tris = [1, 1]
    while True:
        yield tris
        new_tris = [1, 1]
        new_tris = [new_tris.insert(n, tris[n] + tris[n-1]) for n in range(1, len(tris))]
##        for i in range(1, len(tris)):
##            new_tris.insert(i, tris[i] + tris[i-1])
        tris = new_tris

# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles2():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
print(results)
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')

