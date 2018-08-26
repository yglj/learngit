from urllib import request
#urllib提供的功能利用程序去执行各种HTTP请求，如果需要可以把请求伪装成浏览器，
#方法是监听浏览器发出的请求，根据请求头来伪装。（User-Agent）就是来标示浏览器
'''
from urllib import request
with request.urlopen('http://www.baidu.com') as f:  
     data = f.read()
     print(f'状态:',f.status,f.reason)
     for k,v in f.getheaders():
          print('请求头:')
          print(f'{k}:{v}')
     print('数据:',data.decode('utf-8'))  #https加密不会得到html的内容
'''
#模拟浏览器GET请求，需要使用Request对象，添加HTTP头，可以伪装成浏览器
'''
r = request.Request('http://www.douban.com/')
r.add_header('User-Agent','Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(r) as f:
     data = f.read()                   #返回二进制bytes对象
     for k,v in f.getheaders():
          print(f'请求头：{k}-->{v}')
     print(data.decode('utf-8'))
'''     
#发送POST请求，需要传入data参数（以bytes形式）



from urllib import parse
email = '2365952530@qq.com'
passwd = '123456789b'
login_data = parse.urlencode([
    ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
     ])
r = request.Request('https://passport.weibo.cn/sso/login')
r.add_header('Origin', 'https://passport.weibo.cn')
r.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
r.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(r) as f:
     if f.status == 200:
          data  = f.read()
          print('Date',data.decode('utf-8'))
          for k,v in f.getheaders():
               print(f'响应头：{k}===={v}')
     else:
          print(f.reason)


'''
Handler
如果还需要更复杂的控制，比如通过一个Proxy去访问网站，我们需要利用ProxyHandler来处理，示例代码如下：

proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
with opener.open('http://www.example.com/login.html') as f:
    pass
'''

