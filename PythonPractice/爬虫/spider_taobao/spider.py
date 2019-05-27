import re
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq
import csv

browser = webdriver.Chrome(r'C:\Users\Administrator\Desktop\spider\chromedriver.exe')
wait = WebDriverWait(browser, 10)


def search():
    print('正在搜索')
    try:
        browser.get('https://www.taobao.com')
        inp = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#q'))
        )
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button'))
        )
        inp.send_keys('美食')
        submit.click()
        total = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.total'))
        )
        # print(total.text)
        total = re.match('.*?(\d+)', total.text).group(1)
        return int(total)
    except TimeoutException:
        return search()


def next_page(pagenum):
    print('正在翻页', pagenum)
    try:
        inp = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > input'))
        )
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit'))
        )
        inp.clear()
        inp.send_keys(pagenum)
        print(pagenum)
        submit.click()
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.active > span'), pagenum)
        )
        get_products()
    except TimeoutException:
        return next_page(pagenum)


def get_products():
    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-itemlist > div > div'))
    )
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()  # 把element对象变为可遍历
    products = []
    for item in items:
        # print(item.html())
        product = {
            'img': item.find('.pic .img').attr('src'),
            'price': item.find('.price').text().strip(r'\n'),
            'sell': item.find('.deal-cnt').text()[:-3],
            'title': item.find('.title').text().replace(r'\n', '\\'),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        # print(product)
        products.append(product)
    save_to_csv(products)


def save_to_csv(products):
    headers = ['img', 'price', 'sell', 'title', 'shop', 'location']
    with open('food.csv', 'a+', errors='ignore', newline='') as f:
        f = csv.DictWriter(f, fieldnames=headers)
        f.writeheader()
        f.writerows(products)


def main():
    try:
        total = search()
        get_products()
        for pageNum in range(2, 7):
            next_page(str(pageNum))
    finally:
        browser.close()


if __name__ == '__main__':
    main()