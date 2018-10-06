from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


browser = webdriver.Chrome()   #声明浏览器对象
'''
try:
     browser.get('https://www.baidu.com')         #访问页面    
     inputs = browser.find_element_by_id('kw')   #查找单个元素
     inputs .send_keys('java')       #输入’java‘
     inputs.send_keys(Keys.ENTER)         #回车
     wait = WebDriverWait(browser,10)    #等待10s，直到id='content_left'元素加载出来
     wait.until(EC.presence_of_element_located((By.ID,'content_left')))
     print(browser.current_url)      #url,cookies,html
     print(browser.get_cookies())
     print(browser.page_source)
finally:
     time.sleep(10)
     browser.close()
'''
'''
#查找单个元素
browser.get('https://www.taobao.com')
input_first = browser.find_element_by_id('q')
input_second = browser.find_element_by_css_selector('#q')
input_third = browser.find_element_by_xpath('//*[@id="q"]')
inp = browser.find_element(By.ID,'q')
print(input_first,'\n\n',input_second,'\n\n',input_third,'\n\n',inp)
#查找多个元素
print('--------------')
inps = browser.find_elements_by_css_selector('.service-bd li')
inps2 = browser.find_elements(By.CSS_SELECTOR,'.service-bd li')
print(inps,'\n')
print(inps2)
'''

'''
#元素交互操作
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
inputs = browser.find_element_by_id('q')
print(type(inputs)) #<class 'selenium.webdriver.remote.webelement.WebElement'>
inputs.send_keys('手机')
time.sleep(3)
inputs.clear()
inputs.send_keys('python')
button = browser.find_element_by_class_name('btn-search')
button.click()
'''

'''
#交互动作
from  selenium.webdriver import ActionChains
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
source = browser.find_element_by_css_selector('#draggable')
target = browser.find_element_by_css_selector('#droppable')
actions = ActionChains(browser) 
actions.drag_and_drop(source,target)    #把source拖拽到target处
actions.perform()
'''

'''
#获取信息（属性，文本，id，位置，标签名，大小）
url= 'https://www.zhihu.com/explore'
browser.get(url)
logo = browser.find_element_by_id('zh-top-link-logo')
print(logo)
print(logo.get_attribute('class'))
print(logo.text)
print(logo.id)
print(logo.location)
print(logo.tag_name)
print(logo.size)
'''
from selenium.common.exceptions import NoSuchElementException
#Frame 页面框架
'''
url =  'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
source = browser.find_element_by_id('draggable')
print(source)
try:
     logo = browser.find_element_by_class_name('logo')
     print(logo)
except NoSuchElementException:
     print('no logo')
browser.switch_to.parent_frame()
logo = browser.find_element_by_class_name('logo')
print(logo)
print(logo.text)
'''

#等待 显式、隐式
'''
browser.get('https://www.zhihu.com/explore')
browser.implicitly_wait(10)
inp = browser.find_element_by_class_name('zu-top-add-question')
print(inp.text)

browser.get('https://www.taobao.com/')
wait = WebDriverWait(browser,10)
input = wait.until(EC.presence_of_element_located((By.ID,'q')))
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.btn-search')))
print(input,button)
'''

#前进后退
'''
browser.get('https://www.baidu.com/')
browser.get('https://www.taobao.com/')
browser.get('https://www.python.org/')
browser.back()
time.sleep(3)
browser.forward()
'''

#Cookies
'''
browser.get('https://www.zhihu.com')
print(browser.get_cookies())
browser.add_cookie({"name":"xxx","domain":"www.zhihu.com","value":"germey"})
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())
'''
#执行js（用js操作页面动作）
'''
browser.get('https://www.zhihu.com/explore')
browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
browser.execute_script('alert("到网页底部")')
'''
#选项卡管理
browser.get('https://www.baidu.com')
browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to.window(browser.window_handles[1])
browser.get('https://www.taobao.com')
time.sleep(3)
browser.switch_to.window(browser.window_handles[0])
browser.get('http://www.zhihu.com')


#异常处理
from selenium.common.exceptions import TimeoutException
try:
     browser.find_element_by_id('hello')
except NoSuchElementException:
     print('no element')
except TimeoutException:
     print('time out')
finally:
     browser.close() #只关闭了zhihu
