'''
问题：程序运行中，所有变量都存在内存中，一旦程序结束，内存资源回收
运行时改动的变量失效

解决：需要把变量存到内存
》序列化（serialization,marshalling,flattening）python 中叫pickling
把变量从内存中变成可存储或传输的过程
序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。

unpickling：把变量内容从序列化的对象重新读到内存里称之为反序列化

pickle模块
pickle.dumps（） 把任意对象序列化成一个bytes
pickle.dump() 直接把序列化对象写入 file-like-Object

对象从磁盘读到内存时，可以先把内容读到一个bytes
pickle.loads() 反序列化
pickle.load 直接从一个file-like-Object 中反序列化出对象

Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python
只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。
'''
d = {"teacher":'cjink',"nai":38,"kou":'ojj'}
import pickle

def one():
     text = pickle.dumps(d)
     print('text:',text)
     with open('dumps.txt','wb') as f:
          f.write(text)

     print('continue...')

     with open('dumps.txt','rb') as f:
          text = f.read()
          print('text:',text)
          print(pickle.loads(text))

#one()

nd = ''
def two(sq):
     with open('dumps.txt','rb') as f:
          #print(f.read(),f.tell()) #调用read() 方法后， steam position with 66 ，继续调用为''
          nd = pickle.load(f)
          print(sq,str(nd))
     with open('dumps.txt','ab') as f:
          pickle.dump(nd,f)
          
          

two(1)
two(2)
