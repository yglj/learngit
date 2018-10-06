'''
multiprocessing
Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。

子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。

Python的os模块封装了常见的系统调用，其中就包括fork，可以在Python程序中轻松创建子进程：

import os

print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
运行结果如下：

Process (876) start...
I (876) just created a child process (877).
I am child process (877) and my parent is 876.
有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务，常见的Apache服务器就是由父进程监听端口，每当有新的http请求时，就fork出子进程来处理新的http请求

如果你打算编写多进程的服务程序，Unix/Linux无疑是正确的选择。由于Windows没有fork调用
multiprocessing模块提供了一个Process类来代表一个进程对象
'''
import os
from multiprocessing import Process

def runC(test):
     print('child process(%s) start %s'%(os.getpid(),test))


if __name__ == '__main__':
     print("parent process pid(%s)"%os.getpid())
     p = Process(target=runC, args=('exce',)) #传入一个执行函数和函数的参数
     print('child process start')
     p.start() #用start()方法启动，这样创建进程比fork()还要简单。
     #p.join() #join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
     print('end')


'''
import random,time,os

from multiprocessing import Process,Pool
# 子进程要执行的代码
def multiTask(name):
    btime =  time.time()
    time.sleep(random.random()*3)
    rtime = time.time() - btime
    print('Run child process (%s)...%s seconds' % (os.getpid(),rtime))

if __name__=='__main__':
    print('Parent pid (%s) ' % os.getpid())
    p = Pool(4)
    for i in range(5):
         p.apply_async(multiTask, args=(i,))
    print('begin')
    p.close()
    p.join()
    print('end.')
##Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
##
##请注意输出的结果，task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行
'''

#子进程 pass


#进程间通信

#操作系统提供了很多机制来实现进程间的通信。Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。
import multiprocessing,os,time,random
from multiprocessing import Process,Queue  

def write(q):
     print('read pid:',os.getpid())
     mess = 'abcdefg'
     for m in mess:
          print('put %s in queue'%m)
          q.put(m)
          time.sleep(random.random()*2)

def read(p):
     print('read pid:',os.getpid())
     while True:
          val = p.get(True)
          print('val:',val)

if __name__ == '__main__':
     q = Queue()
     pw = Process(target=write, args=(q,))
     pr = Process(target=read, args=(q,))
     pw.start()
     pr.start()
     print('begin:')
     pw.join()
     pr.terminate()
     print('end')
##在Unix/Linux下，multiprocessing模块封装了fork()调用，使我们不需要关注fork()的细节。由于Windows没有fork调用，因此，multiprocessing需要“模拟”出fork的效果，父进程所有Python对象都必须通过pickle序列化再传到子进程去，所有，
##如果multiprocessing在Windows下调用失败了，要先考虑是不是pickle失败了

##小结
##在Unix/Linux下，可以使用fork()调用实现多进程。
##
##要实现跨平台的多进程，可以使用multiprocessing模块。
##
##进程间通信是通过Queue、Pipes等实现的。
