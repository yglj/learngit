##MySQL是为服务器端设计的数据库，能承受高并发访问，
##同时占用的内存也远远大于SQLite。
##此外，MySQL内部有多种数据库引擎，最常用的引擎是支持数据库事务的InnoDB。


import mysql.connector

try:
     conn = mysql.connector.connect(user='root',password='123456',database='stock')
     cursor = conn.cursor()
     
     cursor.execute('create table lang(id int,language varchar(20) primary key)')
     cursor.execute('insert into lang(id,language) values(%s,%s),(%s,%s)',(1,'python',2,'java'))
     
     print(cursor.rowcount)
     conn.commit()
     
     #cursor.execute('select * from sys_dic where dic_id = %s',('nation',))
     #results = cursor.fetchall()
     #for i in results: print(i)
finally:
     cursor.close()
     conn.close()

'''

由于Python的DB-API定义都是通用的，所以，操作MySQL的数据库代码和SQLite类似。

执行INSERT等操作后要调用commit()提交事务；

MySQL的SQL占位符是%s。

'''
