import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
addr = ('127.0.0.1',9990)
inp = True
while inp:
     inp = bytes(input('输入：'),encoding='utf-8')
     s.sendto(inp,addr)
     print(s.recv(1024).decode('utf-8'))

s.sendto(b'over',addr)
s.close()
print('over')
