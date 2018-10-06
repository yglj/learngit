import socket

'''
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #创建socket对象，ipv4，tcp
s.connect(('www.sina.com.cn',80))  #建立连接 地址+端口号
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
#s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
buffer = []  
while True:
     b = s.recv(1024)   #每次接受指定字节数
     if b:
          buffer.append(b)
     else:
          break
s.close()
response = b''.join(buffer)

headers,html = response.split(b'\r\n\r\n',1)  #分离http报文，网页
print(headers.decode('utf-8'))

with open('sina.cn.html','wb') as f:
     f.write(html)
'''

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',9998))

print(s.recv(1024).decode('utf-8'))
for i in [b'a',b'b',b'c']:
     #print(i)
     s.send(i)
     print(s.recv(1024).decode('utf-8'))

while True:
     inp = input('输入：')
     s.send(bytes(inp,encoding='utf-8'))
     if inp == 'exit':
          s.close()
          break
     else:
          print(s.recv(1024).decode('utf-8'))
