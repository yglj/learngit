#动态语言，根据类创建的实例可以任意绑定属性
#实例属性通过实例变量和self变量绑定
#不要对类属性和实例属性使用相同的名字

class Student(object):
     count = 0
     def __init__(self,name):
          Student.count+=1
          self.name = name

if Student.count != 0:
     print("测试失败")
else:
     A = Student('a')
     if Student.count != 1:
          print("测试失败")
     else:
          B = Student('b')
          if Student.count != 2:
               print("测试失败")
          else:
               print("Student count:",Student.count)
               print('测试通过')
