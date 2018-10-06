# 封装数据和逻辑，方便调用，不需要知道具体的内部细节
'''
__xxx__特殊变量，可以直接访问
访问限制
实例变量.__name  等价 private修饰符
无法从外部访问属性
'''
class Student:
     def __init__(self,name,score):
          self.__score = score  #限制访问，变量名会被修改
          self.__name = name
     def setName(self,str):
          if type(str) == str:  #类型检查
               self.name = str
          else:
               raise TypeError("bad type")
     def getName(self):
          return self.__name
     def print(self):
          print("{1}={0}".format(self.__score,self.__name))
     def garde(self):
          if self.__score > 90:
               return 'A'
          elif self.__score > 60:
               return 'B'
          else:
               return 'C'

lisa = Student("Lisa",89)
Bart = Student("Bart",56)
print(lisa.garde())
print(Bart.garde())
#print(lisa.__name)  #不能访问
#lisa.setName(45)
lisa.__name = 'l' # 和class里的__name不是同一个变量 
print(lisa.__name)
print(lisa.getName())

