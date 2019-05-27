import asyncio  #异步io
import time

'''
@asyncio.coroutine # 把一个generator标记为coroutine类型
def hello():
     t = time.time()
     print('cao ni ma!')
     r = yield from asyncio.sleep(1)
     print(r)
     print('hello again!')
     print(time.time()-t)

loop = asyncio.get_event_loop()  #获取EventLoop
loop.run_until_complete(hello())   #执行协程直到完成
loop.close()
'''

import threading
'''
@asyncio.coroutine 
def now(i):
     print(threading.currentThread(),i)
     r = yield from wio(i)      #中断，模拟io操作，拿到返回（None）
     print(threading.currentThread(),i)

def wio(i):
     print('io wait one seconds')
     return asyncio.sleep(i)  #协程休眠i秒

task = [now(1),now(2)]              #任务列表
loop = asyncio.get_event_loop()   
loop.run_until_complete(asyncio.wait(task)) 
loop.close()
'''



@asyncio.coroutine
def get(host):
     print('start requests %s '%host)
     reader,writer = yield from asyncio.open_connection(host,80) #切换请求任务
     print('conntion %s'%host)  # StreamReader,StreamWriter 
     header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n'%host
     writer.write(header.encode('utf-8'))
     yield from writer.drain() # 刷新底层传输的写缓冲区
     print('ok')
     while True:
          h = yield from reader.readline()
          #print(h)
          if h == b'\r\n' or h==b'':
               break
          print('%s header > %s'%(host,h.decode('utf-8').rstrip()))
     writer.close()
     print('finish')

tasks = [get(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

          
     
     
     
     
     
