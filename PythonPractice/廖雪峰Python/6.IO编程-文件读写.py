
##读写文件是常见的io操作，在磁盘读写文件由操作系统提供功能，
##操作步骤：
##内置open（）函数
##1.请求系统打开一个文件对象（通称文件描述符）
##2.从系统提供的接口中读取文件对象数据或把数据写入文件对象
##3.如果文件不存在抛出IOError错误，提示文件不存在
##4.如果文件打开成功，调用read(),或write()方法读写文件
##5.调用完毕后，close（）关闭文件，（文件对象会占用系统资源，且系统同时打开文件有限）

##文件读写时可能产生IOError，一旦出错后面的f.close()就不会调用
##所以为了确保文件正确关闭，需要try...finally

try:
    f = open(r'C:\Users\Administrator\Desktop\py\练习册\进阶\op.txt', 'r')
    #print(f.read())
finally:
    if f:
        f.close()

     
#这try ... finally是一样的，但是代码更佳简洁，不必调用f.close()方法。
with open('op.txt','r',encoding='gbk',errors='ignore') as lines:
    for f in lines:
        #print(f.strip())
        pass



##调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。
##如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：
'''
file-like Object
像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。除了file外，还可以是内存的字节流，网络流，自定义流等等。file-like Object不要求从特定类继承，只要写个read()方法就行。

StringIO就是在内存中创建的file-like Object，常用作临时缓冲。
'''
##二进制文件
##前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。
##要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可
##>>> f = open('/Users/michael/test.jpg', 'rb')
##>>> f.read()
##b'\xff\xd8\xff\xe1\x00\x18Exif\x00\x00...' # 十六进制表示的字节
##字符编码
##要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件：
##>>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')

##遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。
##遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：
##>>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')

'''
写文件
写文件和读文件是一样的
当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。
只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。
忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。所以，还是用with语句来得保险：


with open('/Users/michael/test.txt', 'w') as f:
    f.write('Hello, world!')
要写入特定编码的文本文件，请给open()函数传入encoding参数，将字符串自动转换成指定编码。

'w'覆盖写入
'a'以追加（append）模式写入。
'''


##请将本地一个文本文件读为一个str并打印出来：
fpath = r'C:\Windows\system.ini'

with open(fpath, 'r') as f:
    lines = f.readlines()
    for s in lines:
        print(s.strip())



