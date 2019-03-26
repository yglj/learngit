#读写内存中的str
#创建StringIO，调用读写方法，getvalue()方法用于获取写入后的Str
from io import StringIO
f = StringIO()
print(f.write('hello'))
print(f.write(' '))
print(f.write('world'))
print(f.getvalue())

#BytesIO 操作二进制数据，在内存中读写bytes

from io import BytesIO
fb = BytesIO()
fb.write("字符串编码后".encode("utf-8"))
print(fb.getvalue())
#读取时用str或bytes初始化一个StringIO或BytesIO流，再像文件一样读取
def ex3():
     fn = StringIO('one\ttwo\nthree\t\n')
     while True:
          t = fn.readline()
          if t == '':
               break
          print(t.strip())

ex3()

def ex4():
     bn = BytesIO(b'\xac\xa6\xe4\xb8\xb2\xe7\xbc\x96\xe7\xa0')
     print(bn.read())

ex4()

#StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口
#StringIO要么用来读，要么用来写，不能同时用
'''
是因为the stream position的原因，当你用：

d = StringIO('Hello World')
其stream position为0（可以通过d.tell()获得），而后执行

d.readline()
stream position移动到11.因此在执行此方法时，返回的是空字符串。

类似的，使用

f = StringIO()
stream position也为0，而执行

f.write('Hello World')
stream position就移动到11了，因此你再执行readline时返回的依旧是空字符串，若你需要返回'Hello World'可以通过

f.seek(0)
调整stream position即可。
'''
