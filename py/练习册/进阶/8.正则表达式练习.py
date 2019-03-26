
import re

def is_valid_email(addr):
     if re.match(r'[a-z\.]+\@[0-9a-z]+\.com$',addr):
          print(re.match(r'([a-z\.]+\@[0-9a-z]+\.com$)',addr).group(0)) 
          return True



# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')


##match
##([a-z\.]+\@[0-9a-z]+\.com$)



##版本二可以提取出带名字的Email地址：
##
##<Tom Paris> tom@voyager.org => Tom Paris
##bob@example.com => bob

def name_of_email(addr):
     x = re.match(r'(\<?)([a-zA-Z\s]+)\>?([\s\w]{0,9}\@[a-z]+\.org$)',addr)
     if x:
          print(x.group(3))        #group(0) 返回匹配整个字符串本身
          return x.group(2)


# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')


#\<?([a-zA-Z\s])\>?[\s\w]{0,9}\@[a-z]+\.org$


#分割，分组
