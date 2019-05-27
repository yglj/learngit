Alphabet = ["a","c","c","d","e","f","g","h","i","j"]
#索引
print(Alphabet[-9:3]) #只能从左到右
print(Alphabet[3:-3:2])
#增加
Alphabet.append("k")
print(Alphabet)
Alphabet.insert(1,"b")
print(Alphabet)
Alphabet.extend(("m","n"))
print(Alphabet)
#搜索
print(Alphabet.index("k"))
print("c" in Alphabet)
#删除
print(Alphabet.pop()) #推出右边的一个
Alphabet.remove("c")  #移除第一次出现的
print(Alphabet)
#list运算符 +,-,*
li = Alphabet * 2
print(li)

#连接
T = "_".join(Alphabet)
print(T)

#分割
print(T.split("_"))

#映射解析
one = [1,2,4,5]
one = [one*2 for one in one]
print(one)

#dictionary中解析
dict = {1:"one",2:"two",3:"three"}
print(dict.values())
print(dict.keys())
print(dict.items())
print([k for k,v in dict.items()])
print(["%s=%s"%(k,v) for k,v in dict.items()])

#list 过滤
g = [1,2,2,3,3,3]
print([i for i in g if g.count(i) == 1]) #list中出现的次数为1的元素