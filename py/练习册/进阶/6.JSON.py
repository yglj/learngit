'''
JSON
如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，
但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。
JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。

JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应如下：

JSON类型	Python类型
{}	        dict
[]	        list
"string"	str
1234.56	        int或float
true/false	True/False
null	        None
JSON标准规定JSON编码是UTF-8

把Python对象变成一个JSON
内置JSON模块
dumps()方法返回一个str，内容就是标准的JSON。
dump()方法可以直接把JSON写入一个file-like Object。

要把JSON反序列化为Python对象
loads() 把JSON的字符串反序列化
load() 从file-like Object中读取字符串并反序列化


Python的dict对象可以直接序列化为JSON的{}
对于自定义class对象 会报错：TypeError
因为这些对象是不可序列化的为json的对象

dumps()方法提供一个default参数，可以传入一个转换函数
通常class的实例都有一个__dict__属性，它就是一个dict，也可以自定义函数

把JSON反序列化为一个Student对象实例
object_hook接收一个转换函数
'''
d = {'a':2,'b':'boduojieyi','c':True,'d':None,'e':[1,2,3,4],'f':{1:'1'}}
import json
def json1():
     dm = json.dumps(d)
     with open('json.txt','w') as f:
          dm1 = json.dump(d,f)
          
     print(dm,dm1)

     with open('json.txt','r') as f:
          print(json.load(f))

     json.loads(dm)


class stu:
     def __init__(self,age,goal):
          stu.age = age
          stu.goal = goal

s = stu(19,'009')
##print(json.dumps(s)) TypeError: Object of type 'stu' is not JSON serializable
def stuTurn(obj):
     return {'age':obj.age,'goal':obj.goal}  #?
     
print(json.dumps(s,default = stuTurn))
print(json.dumps(s,default = lambda s:s.__dict__))

jstr = '{"age":true,"goal":null}'
def jstrturn(obj):
     return stu(obj['age'],obj['goal'])
     
print(json.loads(jstr,object_hook = jstrturn))


#对中文进行JSON序列化时，json.dumps()提供了一个ensure_ascii参数，观察该参数对结果的影响
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)

'''
Python语言特定的序列化模块是pickle，但如果要把序列化搞得更通用、更符合Web标准，就可以使用json模块。

json模块的dumps()和loads()函数是定义得非常好的接口的典范。当我们使用时，只需要传入一个必须的参数。但是，当默认的序列化或反序列机制不满足我们的要求时，我们又可以传入更多的参数来定制序列化或反序列化的规则，既做到了接口简单易用，又做到了充分的扩展性和灵活性。
'''
