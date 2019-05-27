# -*- coding:utf-8 -*-
# 抓取猫眼top100电影（只抓到了99个），最后一部龙猫无评分，抓取不到

from multiprocessing.pool import Pool
import requests
from requests.exceptions import RequestException
import re
import json


def get_one_page(url):  #get方式请求页面，返回html
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"}
    try:
        page = requests.get(url,headers = headers)
        if page.status_code == 200:
            return page.text;
        return None
    except RequestException:
        print('request error')
        return None

def parser_one_page(page):    #利用正则模板解析
    pattern = re.compile('<dd>.*?board-index.*?">(\d+)</i>.*?data-src="(.*?)".*?'
                          +'title="(.*?)".*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                          +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
    items = re.findall(pattern,page)
    for item in items:       #遍历每一部电影
        yield{               #生成器返回电影信息字典
            'seq':item[0],
            #'src':item[1],
            'title':item[2],
            'star':item[3].strip()[3:],
            'time':item[4].strip()[5:],
            'score':item[5]+item[6]
        }


def write_to_file(content):    #写入序列化json字符串
    with open('maoyantop100.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
        f.close()

def main(offset):           #offset动态请求翻页，共十页，每页十部
    url = 'http://maoyan.com/board/4?offset='+str(offset)
    html = get_one_page(url)
    for line in parser_one_page(html):
        write_to_file(line)
        print(line)
    #print(html)

if __name__ == '__main__':
    #pool = Pool()             #利用进程池秒抓
    #pool.map(main,[i*10 for i in range(10)])
    for i in range(10):
        main(i*10)



