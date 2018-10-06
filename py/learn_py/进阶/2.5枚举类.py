#枚举类 定义一个class类型，然后，每个常量都是class的一个唯一实例

from enum import Enum,unique
month = Enum('Months',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name,member in month.__members__.items():
     print(name,'->',member,':',member.value)
#value属性则是自动赋给成员的int常量，默认从1开始计数


@unique
class Weekday(Enum):  #@unique装饰器可以帮助我们检查保证没有重复值
     Sun = 0
     Mon = 1
     Tue = 2
     Wed = 3
     Thu = 4
     Fri = 5
     Sat = 6

day = Weekday(0) #<=> day = Weekday.Sun
print(day.Sun)
print(day.Sun.name,':',day.Sun.value)
print(Weekday['Sun'])  #key:value = Weekday:Weekday.Sun
print(day == Weekday(0))

#Enum(枚举类名，枚举常量对象tuple) 键：枚举常量对象名 值：枚举常量对象
#既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量
#Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较




#练习 把Student的gender属性改造为枚举类型，可以避免使用字符串：

class Gender(Enum):
    Male = 0
    Female = 1
    
#sex = Enum('Gender',('Male','Female'))
@unique
class Gender(Enum):
    Male = 0
    Female = 1
    
class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!',bart.gender.value)
