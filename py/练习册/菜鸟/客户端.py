import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #ipv4，tcp流 
s.connect(("www.sina.com",80))                     #建立连接

s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')  #发送数据

buffer = []                 #存入list中
while True:
    a = s.recv(1024)       #循环，每次接受1k的数据
    if a:
        buffer.append(a)
    else:        
        break

data = b" ".join(buffer)

s.close()

header ,html = data.split(b'\r\n\r\n',1)    #分离网页
  
print(header.decode("utf-8"))    #输出头文件

with open("sina",'wb') as f:    #保存到文件中
    f.write(data)
