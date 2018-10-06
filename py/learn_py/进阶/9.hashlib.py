import hashlib

#1.哈希算法（MD5,SHA1），把任意长度数据转为一个固定长度字符串（16进制字符串）
#摘要（digest），防止原始数据被篡改

#MD5 固定128bit 32位16进制
md5 = hashlib.md5()   #MD5对象
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))  #摘要计算
print(md5.hexdigest())  #返回十六进制摘要


#SHA1 160bit 40位16进制 SHA256  SHA512
#用于加密用户登录密码


def calc_md5():
     return get_md5(passwd + 'the-Salt')

#如果假定用户无法修改登录名，就可以通过把登录名作为Salt的一部分来计算MD5，从而实现相同口令的用户也存储不同的MD5



#2.根据用户输入的口令，计算出存储在数据库中的MD5口令：

def calc_md5(password):
    pass
#存储MD5的好处是即使运维人员能访问数据库，也无法获知用户的明文口令。
#设计一个验证用户登录的函数，根据用户输入的口令是否正确，返回True或False：

# -*- coding: utf-8 -*-
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(user, password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    if db[user] == md5.hexdigest():
         return True
    else:
         return False

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')

#3.加强简单的用户密码，通过对原始的口令加一个复杂的字符串实现，俗称“加盐”


#练习
##根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5：

db = {}

def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')
#然后，根据修改后的MD5算法实现用户登录的验证：

# -*- coding: utf-8 -*-
import hashlib, random

def get_md5(s):  #验证
    return hashlib.md5(s.encode('utf-8')).hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)]) #产生随机用户‘加盐’字符串
        self.password = get_md5(password + self.salt)
db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username, password):
    user = db[username]
    password += user.salt
    return user.password == get_md5(password)

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')


#单向性，不能加密，只能防止篡改
