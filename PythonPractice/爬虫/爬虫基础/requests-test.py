import requests

#get请求

data = {'a':'aaa'}
##response = requests.get('http://www.httpbin.org/get?name="网吧"',params =data)
##print(type(response))
##print(f'状态码:{response.status_code}')
##print(f'响应头:{response.headers}')
##print(f'响应体:{response.text}')
##print(response.cookies)

#解析json

##print(response.json())
##import json
##print(json.loads(response.text))

#获取二进制数据
##print(f'二进制context:{response.content}')
##favicon = requests.get('http://github.com/favicon.ico')
##with open('favicon.ico','wb') as f:
##     f.write(favicon.content)
     
#添加headers
headers = {'User-Agent':'Chrome'}
##response = requests.get('http://www.httpbin.org/get',headers=headers)
##print(response.json()['headers'])

#post请求，状态码判断
##response = requests.post('http://www.httpbin.org/wow/post',data=data,headers=headers,timeout=1)
####print(response.text)
####print(response.json())
##print('error') if not response.status_code == 200 else print('Successfully') 
##exit() if not response.status_code == requests.codes.ok else print('ok')  #exit()退出shell

#上传文件
##files = {'icon':open('favicon.ico','rb')}
##response = requests.post('http://www.httpbin.org/post',files=files)
##print(response.text)

#获取cookie
##response = requests.get('http://www.baidu.com')
##for k,v in response.cookies.items():
##     print(f'{k}:{v}')

#会话维持
##seesion = requests.Session()
##seesion.get('http://www.httpbin.org/cookies/set/number/123456')
##response = seesion.get('http://www.httpbin.org/cookies')
##print(response.text)


#证书验证
##from requests.packages import urllib3
##urllib3.disable_warnings() #关闭安全警告
##r = requests.get('https://www.12306.cn',verify=False)  #ssl.CertificateError
##print(r.status_code)

#代理设置

#超时设置

##from requests.exceptions import ReadTimeout
##try:
##     response = requests.get('http://www.httpbin.org',timeout=0.2)
##     print(response.status_code)
##except ReadTimeout as r:
##     print(r.reason)

#认证设置

#异常处理
from requests.exceptions import ConnectTimeout, ConnectionError,RequestException
try:
     response = requests.get('http://www.httpbin.org/get',timeout=0.3)
     print(response.status_code)
except ConnectTimeout :
     print('time out')
except ConnectionError:
     print('connection error')
except RequestException:
     print('error')
