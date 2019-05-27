from bs4 import BeautifulSoup

html = '''

<html>
<head>
<title>dromouse's story</title>
</head>
<body>
     <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
     <p class="story">
          Once upon a time there were three little sisters; and their names were
          <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
          <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
          <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
          and they lived at the bottom of a well.
     </p>
<p class="story">...</p>
'''
##soup = BeautifulSoup(html,'lxml')
##print(soup.prettify())  #补全不完整的html标签
##print(soup.title.string)  


#标签选择器
a_html = """
<html><head><title>The Dormouse's story begin</title></head>
<body>
<label class="title" name="dromouse"><b>The Dormouse's story</b> </label>
<p class="story" name="name">
     Once upon a time there were three little sisters; and their names were
     <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
     <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
     <a href="http://example.com/tillie" class="sister" id="link3">Tillie<em id='em'>em...</em></a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
#选择元素  <class 'bs4.element.Tag'> （以下方法只返回第一个选中的）

soup = BeautifulSoup(a_html,'lxml')
'''
print(soup.head)
print(soup.body)
print(soup.title)
print(type(soup.title))
print(soup.p)
'''
#选择名称(标签名)
##print(soup.title.name)
##print(soup.head.name)

#选择属性
##print(soup.p.attrs['class'])
##print(soup.p.attrs['name'])

#选择内容
##print(soup.p.text)    
##print(soup.p.string)

#嵌套选择
#print(soup.head.title.string)
'''
#子节点和子孙节点
print(soup.p.contents) #返回 list
for child in soup.p.children:  #直接孩子，返回iterator
     print(child)  

print(list(enumerate(soup.p.descendants)))  #所有子孙
'''

#父节点和祖先节点
##print(soup.a.parent)
##print(list(enumerate(soup.a.parents)))
#兄弟节点
##print(list(enumerate(soup.a.next_siblings)))
##print(list(enumerate(soup.a.previous_siblings)))

#标准选择器 find_all(name,attrs,recursive,text,**kwargs) find()返回第一个n ....
#可根据标签名,属性,内容查找文档
##print(soup.find_all('p'))
##print(soup.find_all('p')[1])  #tag name
'''
for a in soup.find_all('p')[0]:
     print('tag>>>>',a)

print(soup.find_all(attrs={'class','sister'}))   #attrs
print(soup.find_all(id='em'))
print(soup.find_all(class_='sister'))
'''
#print(soup.find_all(text='em...'))   #text

#css选择器 select()直接传入css选择器
print(soup.select('#em'))
print(soup.select('.sister'))
print(soup.select('.sister #em '))  #bs4.element.Tag
print(soup.select('a'))
for a in soup.select('a'):   
     print(a['href'])       #属性
     print(a.get_text())     #文本

'''
推荐使用lxml解析库，必要时用html.parser
标签选择器功能弱但速度快
建议使用find(),find_all()查询单，多个结果
对css选择器熟悉可用select
文本、属性获取方法
'''
print(soup.find('p').find('em'))
