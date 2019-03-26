import requests
#它是一个Python第三方库，处理URL资源特别方便

r = requests.get(r'https://www.douban.com')  #使用GET访问页面
print(r.status_code)
#print(r.text)   
print(r.encoding)  #requests自动检测编码，可以使用encoding属性查看

#传入dict参数
page = requests.get('https://www.douban.com/search',params={'p':'python','cat':'1011'})

print(page.url) #实际请求url
#print(r.text)
#print(page.content) #获得二进制（网页）内容无论响应是文本还是二进制内容，我们都可以用content属性获得bytes对象

#对于特定类型的响应，如JSON,可直接获取

page = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
#print(page.json())



#HTTP Header ,传入一个dict作为headers参数(把请求头的用户代理设置为手机浏览器，访问手机版页面)
r = requests.get('https://www.douban.com',headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
#print(r.text)

#发送POST请求，data参数作为POST请求数据
r = requests.post('https://www.douban.com',data={'from_email':'abc@example.com','form_password':'123456'})
#print(r.headers)
#上传数据编码格式
'''
requests默认使用application/x-www-form-urlencoded对POST数据编码。如果要传递JSON数据，可以直接传入json参数：
params = {'key': 'value'}
r = requests.post(url, json=params) # 内部自动序列化为JSON
类似的，上传文件需要更复杂的编码格式，但是requests把它简化成files参数：

>>> upload_files = {'file': open('report.xls', 'rb')}
>>> r = requests.post(url, files=upload_files)
在读取文件时，注意务必使用'rb'即二进制模式读取，这样获取的bytes长度才是文件的长度。

把post()方法替换为put()，delete()等，就可以以PUT或DELETE方式请求资源。

除了能轻松获取响应内容外，requests对获取HTTP响应的其他信息也非常简单。例如，获取响应头：
'''
# r.headers
#{Content-Type': 'text/html; charset=utf-8', 'Transfer-Encoding': 'chunked', 'Content-Encoding': 'gzip', ...}
# r.headers['Content-Type']
#'text/html; charset=utf-8'

#cookies
'''
requests对Cookie做了特殊处理，使得我们不必解析Cookie就可以轻松获取指定的Cookie：
>>> r.cookies['ts']
'example_cookie_12345'
要在请求中传入Cookie，只需准备一个dict传入cookies参数：

>>> cs = {'token': '12345', 'status': 'working'}
>>> r = requests.get(url, cookies=cs)
'''
#指定超时，传入以秒为单位的timeout参数：
# r = requests.get(url, timeout=2.5) # 2.5秒后超时
