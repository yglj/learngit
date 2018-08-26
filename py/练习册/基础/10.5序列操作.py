#切片（Slicing）运算 【列表、元组与字符串】  下标操作 （Subscription Operation


#字符串操作
word='hello world'
for a in word:
     print(a)
print(word[5])
print(word[0:-5])
print(','.join(word)) #连接


a='abc'
print(a.replace('a','d')) #替代
print(a)


sentence='i am a english leanrning'
print(sentence[::4])  #step 步长为4
print(sentence.split())
s='t,t,t,e,e'
print(s.split(','))        #分离,返回一个列表
print('aaa'.split('a'))

