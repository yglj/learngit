# 把‘salt’ 看做一个口令，要验证哈希码，就必须提供正确的口令
#1. Hmac 算法 在计算哈希码的过程中把key混入

import hmac
message = b'Hello, world!'
key = b'secret'
#参数： key,message 都是bytes类型
bHash = hmac.new(key,message,digestmod='md5')
print(bHash.hexdigest())

#hmac 输出长度与原始哈希算法一致

##练习
##将上一节的salt改为标准的hmac算法，验证用户口令：
# -*- coding:utf-8 -*-
import hmac,random

#验证函数
def md5_digest(key,password):
     return hmac.new(key.encode('utf-8'),password.encode(),digestmod='md5')\
                .hexdigest()
'''
Help on built-in function chr in module builtins:

chr(i, /)
    Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.


'''
class User:
     def __init__(self,username,password):
          self.name = username
          salt = ''.join([chr(random.randint(48,122)) for i in range(20)])
          print(salt)
          self.password = md5_digest(self.name,\
                                     password)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username,password):
     user = db[username]
     return md5_digest(username,password) == user.password
          
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')
