#Python内置的@property装饰器就是负责把一个方法变成属性调用的

#注意：不能把方法名与属性同名 ，可用_区别

class S:       #利用getter，setter 来检查参数，获取设置参数
     def setScore(self,x):
          if  not isinstance(x,int):
               raise TypeError('score must be an integer!')
          if x < 0 or x > 100:
               raise ValueError("score must between 0~100")
          self.x = x
     def getScore(self):
          return self.score
s = S()
s.setScore(10)


class T:
     @property   
     def s(self):
          return self.x        
     @s.setter
     def s(self,value):
          self.x = value

     @property
     def sum2(self):
         return self.s*2

t = T()
t.s = 100

print(t.s,t.sum2)


# -*- coding: utf-8 -*-
   
class Screen(object):
     @property
     def width(self):
          return self._width
     
     @width.setter
     def width(self,w):
          self._width = w

     @property
     def height(self):
         return self._height
     
     @height.setter
     def height(self,h):
          self._height = h

     @property
     def resolution(self):
          return self.width * self.height
     

# 测试:请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
