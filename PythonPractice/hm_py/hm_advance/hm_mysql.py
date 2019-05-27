# 1.
def reMax(*args):
     return max(args)

print(reMax(1, 55, 2, 4))

# 2.
alist = [1, 2, 3, 4, 5, 6, 4, 2]
def unRepeat(alist):
     return list(set(alist))

print(unRepeat(alist))

#3.
url_str = 'http://www.baidu.com:8080?a=1&b=2&c=3'
def parserUrl(string):
     url_dict = {}
     if '?' in string:
          index = string.index('?')
          url = string[index + 1:].split('&')
          for pro in url:
               k, v = pro.split('=')
               url_dict[k] = v
          print(url_dict)

parserUrl(url_str)

#4.
def odd(args):
     return [x for x in args if x % 2 != 0]

print(odd([1, 2, 4, 6, 9, 7, 8, 10]))

#5.
def test5(string):
     return string.title()

print(test5('we are family'))

#6.
def test6(string):
     print(string.split('.')[1])

test6('aaa.txt')

#7.
class  Students:
     def __init__(self, name, age, scroe):
          self.name = name
          self.age = age
          self.scroe = scroe

     def get_course(self):
          s = sum(self.scroe) // len(self.scroe)
          print(f'xx同学的平均分为{s}分')

stu = Students('aaa', 20, [100, 100, 100])
stu.get_course()
