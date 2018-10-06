#WSGI接口：web server gateway interface

from wsgiref.simple_server import make_server

def handle(env,response):
     #environ这个dict对象拿到HTTP请求信息，
     #start_response()函数接收两个参数，一个是HTTP响应码，
     #一个是一组list表示的HTTP Header，每个Header用一个包含两个str的tuple表示
     response('200 ok',[('Content-Type','text/html')])
     body = '<h1>hello %s</h1>'%(env['PATH_INFO'][1:] or 'xxx')
     return [body.encode('utf-8')]

server = make_server('127.0.0.1',9000,handle) #创建服务器 ip,端口，处理函数

print('Serving HTTP on 9000')
server.serve_forever() #开始一直监听http请求

