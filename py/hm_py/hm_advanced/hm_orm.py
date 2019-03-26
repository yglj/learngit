"""
实现一个ORM(对象关系映射)
"""
import pymysql


class ORM(type):
    def __new__(cls, name, bases, attrs):
        mapping = {}
        for k, v in attrs.items():
            if isinstance(v, tuple):
                mapping[k] = v
                print(f'对应sql映射：{k} ==> {v}')

        for k, v in mapping.items():
            attrs.pop(k)

        attrs['__mapping__'] = mapping
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)


class Model(object, metaclass=ORM):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def save(self, cur):
        fields = list()
        args = list()
        # print(dir(Model))
        for k, v in self.__mapping__.items():
            fields.append(k)
            arg = getattr(self, v[0])
            if isinstance(arg, str):
                arg = "'"+arg+"'"
            else:
                arg = str(arg)
            args.append(arg)
        sql = 'insert into %s(%s) values(%s)' % (self.__table__, ','.join(fields), ','.join(args))
        cur.execute(sql)
        print(sql)


class User(Model):
    uid = ('uid', 'int unsigned')
    name = ('name', 'varchar(20)')
    password = ('password', 'varchar(20)')
    render = ('render', 'bit')


if __name__ == '__main__':
    user = User(uid=123, name='老王', password='123456', render=0)
    db = pymysql.connect(host='localhost', port=3306, user='root', password='', database='test', charset='utf8')
    cur = db.cursor()
    user.save(cur)
    db.commit()
    cur.close()
    db.close()

