from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#创建对象的基类
Base = declarative_base()

class Lang(Base):

     __tablename__ = 'lang'

     #表结构
     id = Column(Integer)
     language = Column(String(20),primary_key=True)


#初始化数据库连接
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/test')

#创建DBSession类型
DBSession = sessionmaker(bind=engine)

#创建session对象
session = DBSession()

#new_lang = Lang(id=3,language='c')

#session.add(new_lang)  #添加对象到session

session.commit()  #提交

result = session.query(Lang).all() #创建查询，filter是where条件，all()返回所有行
print('type:',type(result))
for item in result:
     print(item,item.id,item.language)

session.close()
