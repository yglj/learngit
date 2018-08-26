'''
需求：如果我们要操作文件、目录，可以在命令行下面输入操作系统提供的各种命令来完成。
比如dir、cp等命令

问题：在python程序中怎么操作文件和目录

办法：操作系统提供的接口函数，内置os模块可以直接调用

os 模块
属性：
name 操作系统类型（posix -> linux,unix,mac os x  nt->windows）
uname() 系统详情（windos不提供，os有些函数与操作系统有关）
environ 环境变量
》environ.get('key')

操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中
os.path.abspath('.') 查看当前路径的绝对路径
os.path.join(url,path) 把两个路径合成一个 》win：part-1\part-2 linux:part-1/part-2
os.path.split() 拆分路径 》os.path.splitext() 拆分文件，扩展名
os.mkdir(url) 创建一个目录 
os.rmdir(url) 删除一个目录

os.rename（） 重命名
os.remove() 删除
复制文件的函数居然在os模块中不存在！原因是复制文件并非由操作系统提供的系统调用

shutil模块，可以看做os模块的补充
copyfile() 文件复制

Python的os模块封装了操作系统的目录和文件操作，要注意这些函数有的在os模块中，有的在os.path模块中。

练习
利用os模块编写一个能实现dir -l输出的程序。

编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
'''
import os,os.path,shutil
print('os:%s'%os.name)
#print('\n'.join(os.environ.get('path').split(';')))

#print(os.path.abspath('../../../'))
ab = os.path.abspath('../../../')
path = os.path.join(ab,'abandon')  #只是拼出了一个url字符串
#os.mkdir(path)
#os.rmdir(path)


#win10的cmd里dir就是列出文件详细信息，dir -l的话列出的是磁盘卷序列号
import datetime

#模仿dos命令行的dir命令
##for x in os.listdir('.'):
##     #print(x)
##     size = os.path.getsize(x) if (not os.path.isdir(x)) else ''
##     mtime = datetime.datetime.fromtimestamp(os.path.getmtime(x)).strftime('%Y-%m-%d %w %H:%M')
##     flag = '<DIR>' if os.path.isdir(x) else ''
##     print('%s\t%s\t%s\t%s\t'%(mtime,flag,size,x))


def find_str(path,string):
     if (not os.path.isdir(path)):
          path = path.split('\\').pop()
          #print(path)
          if string in path:
               print('relative:',path)
          return

     for cpath in os.listdir(path):
          find_str(os.path.join(path,cpath),string)
     

find_str(r'C:\Users\Administrator\Desktop\py','dump')


