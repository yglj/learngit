'''
import time,threading,multiprocessing,random
def loop():
     a,b = 1,1
     n = 0
     while n<10:
          n = a
          a,b = b,a+b
          print('thread(%s):%s'%(threading.current_thread(),n))

print(multiprocessing.cpu_count())

def kill():
     print('thread({}) begin\n'.format(threading.current_thread().name))
     n = 10
     x = 0
     while True:
          if n > 10**10:               
               break
          n *= 10
          x = x^1
          print('thread%s -> %s\n'%(threading.current_thread().name,n))
          time.sleep(random.random()*3)  #不加休眠，看起来像并发
          #print('x:%s\t'%(x))
          

money = 1000
lock = threading.Lock()
def save(n):
     global money #把money声明为global variable ,避免被局部覆盖
     money = money + n
     #print('({}) give:{}'.format(threading.current_thread().name,n))
     money = money - n
     #print('({}) get:{}'.format(threading.current_thread().name,n))

def change(n):
     for i in range(100000):
          try:
               lock.acquire() # 先要获取锁
               save(n)
               #print('({}) have money {}'.format(threading.current_thread().name,money))
          finally:
               lock.release() # 改完了一定要释放锁:


          
if __name__ =='__main__':
#创建
##     print('main thread(%s)'%(threading.current_thread()))
##     t = threading.Thread(target=loop ,name='thread_a')
##     t.start()
##     t.join()
##     print('end')
#多线程不能并发     
     for i in range(multiprocessing.cpu_count()): #cup 4 core GIL的存在让线程只能用一个core,交替运行
          t = threading.Thread(target=kill, name=i+1)
          t.start()
     
     print('end')

     
## 锁 （变量都由所有线程共享，防止共享资源访问冲突）

     #不上锁
     
##     t1 = threading.Thread(target=change, name="one",args=(3,))
##     t2 = threading.Thread(target=change, name="two",args=(5,))
##     t1.start()
##     t2.start()
##     t1.join()
##     t2.join()
##     print('money:',money)
'''
          
          


'''多进程
import multiprocessing,os,time,random,pickle
from multiprocessing import Process,Queue  

def write(q):
     print('read pid:',os.getpid())
     mess = 'abcdefg'
     for m in mess:
          m = pickle,dumps(m)
          print('put %s in queue'%m)
          q.put(m)


w = pickle.dumps(write)
print(w)
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
'''

import threading

local = threading.local()
def saying():
     print('thread_{} said Can I help your {}\n'.format(threading.current_thread().name,local.name))

def run(people):
     local.name = people
     saying()               #local把name 变成线程的全局变量，就不用传递参数
     

     
if __name__ == '__main__':
     t1 = threading.Thread(target=run, args=('lihong',), name='one')
     t2 = threading.Thread(target=run, args=('wangwu',), name='two')
     t1.start()
     t2.start()
     t1.join()
     t2.join()
     print('&&&&&&&&&')
