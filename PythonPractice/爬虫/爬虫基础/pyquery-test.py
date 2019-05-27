from pyquery import PyQuery as pq

#初始化对象（字符串，url，文件）

html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
     <p>;;;</p>
 </div>
'''
doc = pq(html)
#doc = pq(url = 'https://www.baidu.com')
#doc = pq(filename = 'demo.html')
#print(doc)
#print(type(doc))   <class 'pyquery.pyquery.PyQuery'>对象

#基本css选择器
##print(doc('li'))
##print(doc('#container .list .active'))

#查找元素
#print(doc.find('li'))

#祖先，子孙，同胞
'''
item = doc('li.item-0.active')
print(item.children())
print(item.parent())
print(list(enumerate(item.parents())))
print(item.siblings())
'''
#遍历
##lis = doc('li').items()
##print(type(lis))
##for li in lis:
##     print(li)

#获取信息（属性，文本，HTML）
a = doc('.item-0.active a')
print(a.html())
print(a.text())
print(a.attr('href'))

#DOM操作
#addClass，removeClass,attr,css,remove
'''
a.addClass('active')
print(a)
a.removeClass('active')
print(a)

a.attr('name','tag-a')
a.css('font-size','20px')
print(a)

print(doc)
doc('div').remove('p')
print(doc.html())
'''

#伪类选择器
html2 = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
html2 = pq(html2)
print(html2('li:last-child'))
print('\n')
print(html2('li:nth-child(2n)')) #li选取偶数孩子
print('\n')
print(html2('li:gt(2)'))  #从大于下标2的li
print('\n')
print(html2('li:contains(second)'))
