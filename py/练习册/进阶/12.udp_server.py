import socket

#不需要建立连接，只要地址就能发送数据

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #创建socket对象，ipv4,udp
s.bind(('127.0.0.1',9990))   #绑定端口
print('bind port on 9990')

while True:
     data,addr = s.recvfrom(1024)
     print('socket addrres from %s:%s'%addr,data) 
##     rec = sock.recv(1024).decode('utf-8')
##     if rec == 'exit':
##          break
     s.sendto(('return %s'%data.decode('utf-8')).encode('utf-8'),addr) #发送数据（数据，地址）
     if data == b'over':
          s.close()
          print('over')
          break
          
     
