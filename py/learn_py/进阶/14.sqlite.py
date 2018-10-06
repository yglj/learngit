# SQLite 一种嵌入式数据库
# 一个数据库连接称为Connection
# 通过 游标Cursor 执行sql语句
# Python定义了一套操作数据库的API接口，任何数据库要连接到Python，只需要提供符合Python标准的数据库驱动即可。


import sqlite3  #导入驱动
'''
try: 
     conn = sqlite3.connect('s.db')  #创建连接对象
     cursor = conn.cursor()   #创建游标对象
     #cursor.execute('create table stu (name varchar(10),id int primary key)')
     #cursor.execute('insert into stu (name,id) values ("pp","9")')
     #print(cursor.rowcount)   #获取插入的行数
     conn.commit()    #提交事务
     
     cursor.execute('select * from stu where id like ?',('_',))
     print(cursor.rowcount)
     
     cursor.execute('delete  from stu where id = ?',('4',))
     print(cursor.rowcount)
     
     cursor.execute('update stu set name=? where id=?',('dd','5'))
     print(cursor.rowcount)

     conn.commit()

     cursor.execute('select * from stu')
     value = cursor.fetchall()  #拿取结果集 list（tuple）
     print(value)
     cursor.close()
     
finally:
     conn.close()
'''
##
##练习
##请编写函数，在Sqlite中根据分数段查找指定的名字：

# -*- coding: utf-8 -*-

import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()

def get_score_in(low, high):
    #' 返回指定分数区间的名字，按分数从低到高排序 '
     conn = sqlite3.connect('test.db')
     cursor = conn.cursor()
     cursor.execute('select name from user where score between ? and ? order by score asc',(low,high))
     names = cursor.fetchall()
     cursor.close()
     conn.close()
     names = [''.join(name) for name in names]
     return names 
     

# 测试:
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('Pass')
