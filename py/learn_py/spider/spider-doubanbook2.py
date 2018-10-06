# -*- coding:utf-8 -*-
'''
使用beautifulsoup 爬取douban受欢迎的图书
'''
import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException,ConnectionError

books = ''
try:
     headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
     html = requests.get('https://book.douban.com',timeout=1,headers=headers).text
except RequestException:
     print('request fail')
except ConnectionError:
     print('time out')
else:
     soup = BeautifulSoup(html,'lxml')
     div = soup.find(class_='popular-books')
     h2 = div.find('span').string
     ul = div.select('ul li')
     books += h2
     for li in ul:
          link = li.a.attrs['href']
          title = li.select('h4 a')[0].get_text().strip()
          rating = li.select('.average-rating')[0].text.strip()
          author = li.select('.author')[0].text.strip()
          classify = li.select('.book-list-classification')[0].text.strip()
          reviews =  li.select('.reviews')[0].text.strip()
          info = [title,rating,author,classify,reviews,link]
          books += '\n\n'+'\n'.join(info).strip()
     #print(books)
finally:
     print('finish')
     if books != '':
          with open(r'c:/users/administrator/desktop/spider/popular-book.txt','w',encoding='utf-8') as f:
               f.writelines(books)
