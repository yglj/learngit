#re.match(pattern,string,flags=0)
import re
content = 'Hello 123 4567 World_This is a Regex Demo'
len(content)
r1 = '^Hello\s(\d+)\s\d{4}\s\w{10}.*Demo$' #常规匹配,（）匹配目标
r2 = '^Hello.*Demo$'  #泛匹配
r3 = '.*(\d+).*' #贪婪匹配
r4 = '.*?(\d+).*' #非贪婪匹配
result = re.match(r4,content)
##print(result.span())
##print(result.group())
##print(result.group(1))


content2 = '''a
$tn
c
'''
result = re.match('.*',content2,re.S) #匹配模式re.S
print(result)

content3='a$c%d'#包含特殊字符使用转义
result = re.match('a\$c.*?d$',content3)
print(result)

html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
        </li>
    </ul>
</div>'''
#re.search
##result = re.search('(\d)+',content)
##print(result)
##result = re.search('<li.*?singer="(.*?)">(.*?)</a>',html,re.S)
##print(result.group(1),result.group(2))

#re.findall
'''
result = re.findall('<li.*?<a.*?singer="(.*?)">(.*?)</a>',html,re.S)

for i in result:
     singer,music = i
     print(singer,music)

results = re.findall('<li .*?>\s*?(<a .*?>)?(\w+)(</a>)?\s*?</li>',html,re.S)
for result in results:
     print(result[1])
     '''
#re.sub 替换
html2 = re.sub('<a .*?>|</a>','',html)
results = re.findall('<li.*?(\w+)\s*?</li>',html2,re.S)
print(results)
for result in results:
     print(result.strip())
#re.compile

r = re.compile(r4)
result = re.search(r4,content)
print(result)
