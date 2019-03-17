import mysql.connector

try:
    conn = mysql.connector.connect(user='root', password='123456', database='test')
    cursor = conn.cursor()

    cursor.execute('create table lang(id int,language varchar(20) primary key)')
    cursor.execute('insert into lang(id,language) values(%s,%s),(%s,%s)', (1, 'python', 2, 'java'))

    print(cursor.rowcount)
    conn.commit()

    # cursor.execute('select * from sys_dic where dic_id = %s',('nation',))
    # results = cursor.fetchall()
    # for i in results: print(i)
finally:
    cursor.close()
    conn.close()
