# -*- coding='utf-8' -*-
'''
抓取豆瓣读书新书速递内容并保存成txt
'''
import requests,re
from requests.exceptions import ConnectionError,RequestException
count = 0
books = ''
try:
     result = requests.get('https://book.douban.com',timeout=1).text
     #print(book.status_code)
except ConnectionError as e:
     print('connection error')
except RequestException as e:
     print('request error')
else:
     #print(result)
     info = re.findall('<li.*?<div class="info">(.*?)</p>.*?<p.*?>(.*?)</p>',result,re.S)  #取div class= info 和 abstract（介绍）
     #print(info)
 
     for item,abstract in info:   #遍历每一条图书
          #print(item)
          #print(type(item))
          item = item.replace(' ','')    
          href = re.search('.*?href="(.*?)"',item,re.S).group(1)  #提取链接
          title = re.search('<h4.*?>(.*?)</h4>',item,re.S).group(1).replace(' ','')  #书名
          more = re.findall('<span.*?author">(.*?)</span>.*?year">(.*?)</span>.*?publisher">(.*?)</span>',item,re.S)
          #print(more,type(more))    #提取作者，年份，出版社
          if more == []:         #多余不符合提取格式的图书，不添加，只加新书速递的内容
               break
          [(author,year,publisher)] = more
          author = re.sub('\s|/|&nbsp','',author)    #替换多余的空格
          year =re.sub('\s|/','',year)
          publisher = re.sub('\s|/','',publisher)
          abstract = abstract.replace(' ','')
          #book = [title,author,year,publisher,href]
          book = f"{title}\n{author}/{publisher}/{year}\n{href}\n{abstract}\n\n\n"      #分行         
          #print(type(book))
          #print(type(books))   
          books += book  
          count += 1       #统计书数
finally:
     #print('一共++++++',count)
     with open('doubanbook.txt','w',encoding='utf-8') as f:
          f.write(f'一共统计有{count}本')  
          f.write(books)


