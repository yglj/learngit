# coding:utf-8
"""
.:任意一个字符（除了\n）
[], \s, \S, \d, \D, \w, \W
* 0次或无限次
+ 1次或多次
？ 1次或0次
{m，n} m到n次
^开头， $结尾
a|b a或b
"""
import re


def re_demo(pattern, html):
    result = re.match(pattern, html)
    print(result)
    print(result.group())


if __name__ == '__main__':
    # re_demo('(\w\s)+', 'a\nb\n\rc')
    email = ['1446s@qq.com', '1446s@163.com']
    for p in email:
        x = re.compile('[\w|\s]+@.*?\.com$')
        re_demo(x, p)

    html = r"<body><p>this is a p tag.</p></body>"
    print(re.match(r"<(\w+)><(\w+)>.*?</\2></\1>", html))
    # (?P<name>)和(?P=name)
    print(re.match(r"<(?P<a>\w+)><(?P<b>\w+)>.*?</(?P=b)></(?P=a)>", html))
   #  print(re.match(r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>", html))


# search()
# findall()
# sub() 将匹配到的数据进行替换
# split() 根据匹配进行切割字符串，返回一个列表
# 贪婪匹配，非贪婪匹配
