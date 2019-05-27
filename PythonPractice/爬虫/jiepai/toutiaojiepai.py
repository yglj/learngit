"""
爬取今日头条街拍
因为同一图片对应多个url，所以存在图片重复问题
"""
import json
from multiprocessing.pool import Pool
from urllib.parse import urlencode
import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
import re
import os


header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}


def get_page_index(offset):  # 获取头条街拍图集目录页面
    data ={                     # ajax请求参数
        'offset': int(offset),
        'format': 'json',
        'keyword': '街拍',
        # 'autoload': 'true',
        # 'count': 20,
        # 'cur_tab': 3,
        # 'from':'gallery',
    }
    url = 'https://www.toutiao.com/search/?'
    url = url + urlencode(data)
    try:
        page = requests.get(url, headers=header)
        print(page.text)
        if page.status_code == 200:
            return page.text
        return None
    except RequestException:
        print('请求失败')
        return None
    except Exception as ex:
        print(ex, ex.__traceback__)
        return None


def parser_page_index(html):   #解析图集目录页面，生成器，返回组图跳转地址
    data = json.loads(html);
    if data and 'data' in data.keys():
        for item in data['data']:
            yield item['article_url']


def get_detail_page(url):    #获取组图页面
    try:
        html = requests.get(url,headers = header)
        if html.status_code == 200:
            return html.text
        return None
    except RequestException:
        print('请求失败')
        return None


def handle_page_detail(html):  #处理组图页面，选取标题文本，和图片url集合
    soup = BeautifulSoup(html,'lxml')
    title = soup.select('title')[0].get_text()
    #print(title)
    pattern = re.compile('gallery:\sJSON.parse\((.*?)\)',re.S)
    pic = re.search(pattern,html)
    if pic:
        pic = json.loads(pic.group(1))
        #print(pic)
        images = set(re.findall('"url":"(.*?)"',pic,re.S))
        return {'title': title,
                'images': images}


def save_image(url,path):   #下载保存图片
    url = url.replace('\\','')
    try:
        print(url)
        img = requests.get(url,headers= header)
        if img.status_code == 200:
            with open(path,'wb') as f:
                f.write(img.content)
                f.close()
    except RequestException:
        print('请求失败')


def main(offset):
    html = get_page_index(offset)
    if html is None:
        print('无内容')
    for url in parser_page_index(html):
        html = get_detail_page(url)
        if html:
            html = handle_page_detail(html)  #用标题创建组图目录，并爬取创建图片
            fold = html['title']
            print('--正在下载>>"%s"'%fold)
            if not os.path.exists(fold):
                os.mkdir(fold)
            count = 0
            for url in html['images']:
                path = '2.' + fold + '/pic_' + str(count) + '.jpg'
                count += 1
                if not os.path.exists(path):
                    save_image(url, path)


if __name__ == '__main__':
    print('start')
    main(0)
    print('end')
    # pool = Pool()
    # pool.map(main, [i*20 for i in range(3)])