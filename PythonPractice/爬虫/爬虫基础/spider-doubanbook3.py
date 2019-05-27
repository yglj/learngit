import requests
from requests.exceptions import ConnectionError,RequestException
from pyquery import PyQuery as pq


try:
     headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
     html = requests.get('https://read.douban.com/kind/1?sort=hot&dcs=book-hot&dcm=douban&dct=read-more',headers=headers).text
except RequestException as e:
     print(e.reason)
except ConnectionError as e:
     print(e.reason)
else:
     #print(html)
     books = ''
     section = pq(html)
     h3 = section('.hd h1').text().strip()
     ul = section('.list-lined.ebook-list.column-list').find('li')
     books += h3
     for li in ul.items():
          href = li.find('a:first-child').attr('href').strip()
          title = li('.title a').text().strip()
          author = li('.author-item').text().strip()
          #year = li('.year').text().strip()
          #publisher = li('.publisher').text().strip()
          rating = li('.rating-average').text().strip()
          abstract = li('.article-desc-brief').text().strip()
          book = f'\n\n\n\n{title}\n\n{author}/{rating}\n\n{abstract}'
          books += book
     with open('c://users/administrator/desktop/spider/doubanbook3.txt','w',encoding='utf-8') as f:
          f.writelines(books)
finally:
     print('over')
          
