import threading,socket,time

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #创建tcp socket 对象
s.bind(('127.0.0.1',9998))  #绑定监听端口
s.listen(3)           #监听连接数
print('wait connection...')       

def tcpLink(sock,addr):
     print('Accept new connection from:\n %s:%s'%addr)
     #buffer = []
     sock.send(b'welcome!')  #发送数据
     while True:
          data = sock.recv(1024) #接收数据
          time.sleep(1)
          if not data or data.decode('utf-8') == 'exit':
               break
          sock.send(('hello %s'%data.decode('utf-8')).encode('utf-8'))
     sock.close()
     print('connection from %s:%s closed '%addr)


while True:
     sock,addr = s.accept()    #(socket对象，地址）接受建立连接
     t = threading.Thread(target = tcpLink, args = (sock,addr))  #开启线程处理连接
     t.start()



          
     
if __name__ == '__main__':
     server()
     
