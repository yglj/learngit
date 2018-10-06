# -*- coding=utf-8 -*-
from urllib import request,error,parse
import socket


data = bytes(parse.urlencode({'cjupyter':'xxx'}),encoding='utf-8')
headers = {'head':'head',
           'User-Agent':'python-ship'}




##try:
##     #response = request.urlopen('http://www.baidu.com',timeout = 1)
##     response = request.urlopen('http://www.httpbin.org/post',timeout=1,data=data)  
##     r = response
##     print(f'状态码：{r.status},状态：{r.reason}')
##     print(type(r))
##     #print(r.read().decode('utf-8'))
##     print(r.headers)
##     print(r.getheaders())  
##     print('data:',r.getheader('data'))
##except error.URLError as u:
##     if isinstance(u.reason,socket.timeout):
##          print('超时')


#Request对象,添加请求头
req = request.Request(url='http://www.httpbin.org/post',data=data,headers=headers,method='POST')
response = request.urlopen(req)
##print(response.read().decode('utf8'))


#Handler 代理
##proxy = request.ProxyHandler({'http':'http://127.1.1.5:9632','https':'https:127.1.1.5:9632'})
##opener = request.build_opener(proxy)
##response = opener.open('http://httpbin.org/get')
##print(response.read())


#Cookie
import http.cookiejar
#cookie = http.cookiejar.CookieJar()
filename = r'C:\Users\Administrator\Desktop\cookie.txt'  
#cookie = http.cookiejar.MozillaCookieJar(filename)  #存MozillaCookie格式cookie
cookie = http.cookiejar.MozillaCookieJar()
cookie.load(filename,ignore_discard=True,ignore_expires=True)
handler = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)
response = opener.open('http://www.baidu.com')
#cookie.save(ignore_discard=True,ignore_expires=True)

##for item in cookie:
##     print(item.name+'='+item.value)


#异常处理
     
##try:
##     response = request.urlopen('http://www.cuiqingcai.com/index.html',timeout=0.1)
##except request.HTTPError as h:
##     print(h.reason,h.code,h.headers)
##except request.URLError as u:
##     print('reason:',u.reason)
##else:
##     print('Request Successful')

#url解析
#urlparse
print(parse.urlparse('https://live.bilibili.com/1196?spm_id_from=333.334.bili_live.5'))
#urlunparse [协议，域名，路径，参数，查询字符串，片段]
print(parse.urlunparse(['https','www.baidu.com','','kw','a=0','commit']))

#urljoin
url1 = 'https://www.baidu.com/?tn=93380420_hao_pg'
url2 = 'https://www.bilibili.com/video/av25394736/?spm_id_from=333.334.bili_music.4'
print(parse.urljoin(url1,url2))
#urlencode url参数格式编码
print(parse.urlencode({'a':'Andy'}))     
