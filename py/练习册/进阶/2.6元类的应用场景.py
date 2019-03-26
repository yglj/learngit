'''
动态修改有什么意义？直接在MyList定义中写上add()方法不是更简单吗？
正常情况下，确实应该直接写，通过metaclass修改纯属变态。

但是，总会遇到需要通过metaclass修改类定义的。ORM就是一个典型的例子。

ORM全称“Object Relational Mapping”，
即对象-关系映射，就是把关系数据库的一行映射为一个对象，
也就是一个类对应一个表，这样，写代码更简单，不用直接操作SQL语句。

要编写一个ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来。

让我们来尝试编写一个ORM框架


'''


class ModelMetaclass(type):
     def __new__(cls,name,bases,attrs):
          if name == 'Model':
               return type.__new__(cls,name,bases,attrs)
          print('找到Model:%s'%name)
          mappings = dict()
          for k,v in attrs.items():
               if isinstance(v,Field):
                    print('mapping reflection:%s => %s'%(k,v))
                    mappings[k] = v
          for k in mappings.keys():
               attrs.pop(k)
          attrs['__mappings__'] = mappings #保存属性和字段的映射关系
          attrs['__table__'] = name #假设表名和类名一致
          return type.__new__(cls,name,bases,attrs)

class Model(dict,metaclass=ModelMetaclass):

     def __init__(self,**kw):
          super(Model,self).__init__(**kw)

     def __getattr__(self,key):
          try:
               return self[key]
          except KeyError:
               raise AttributeError(r" 'model' object has no attribute '%s' "%key)

     def __setattr__(self,key,value):
          self[key] = value

     def save(self):  
          fields = []
          params = []
          args = []
          for k,v in self.__mappings__.items():
               fields.append(v.name)
               params.append('?')
               args.append(getattr(self,k,None))
          sql = " insert into %s(%s) values(%s)" %(self.__table__,','.join(fields),','.join(params))
          print('SQL:%s'%sql)
          print("ARGS:%s"%str(args))

class Field:
     def __init__(self,name,column_type):
          self.name = name
          self.column_type = column_type

     def __str__(self):
          return "%s->%s"%(self.__class__.__name__,self.name)

class IntegerField(Field):
     def __init__(self,name):
          super(IntegerField,self).__init__(name,'bigint')

class StringField(Field):
     def __init__(self,name):
          super(StringField,self).__init__(name,'varchar(100)')

#对应数据库表User
class User(Model):
     #定义类的属性映射到字段的映射
     id = IntegerField('id')
     name = StringField('name')
     password = StringField('password')
     context = StringField('context')

u = User(id=124,name="Mied",passwored="mu384",context="789")
u.save()

'''
用户定义一个class User(Model)时，Python解释器首先在当前类User的定义中查找metaclass，如果没有找到，就继续在父类Model中查找metaclass，找到了，就使用Model中定义的metaclass的ModelMetaclass来创建User类，也就是说，metaclass可以隐式地继承到子类，但子类自己却感觉不到。

在ModelMetaclass中，一共做了几件事情：

排除掉对Model类的修改；

在当前类（比如User）中查找定义的类的所有属性，如果找到一个Field属性，就把它保存到一个__mappings__的dict中，同时从类属性中删除该Field属性，否则，容易造成运行时错误（实例的属性会遮盖类的同名属性）；

把表名保存到__table__中，这里简化为表名默认为类名。

在Model类中，就可以定义各种操作数据库的方法，比如save()，delete()，find()，update等等。

我们实现了save()方法，把一个实例保存到数据库中。因为有表名，属性到字段的映射和属性值的集合，就可以构造出INSERT语句。
'''
