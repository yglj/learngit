# coding:utf-8
import time
import re
from pymysql import connect
import urllib.parse
import logging

URL_ROUTE = {}


def route(page_name):
    def set_route(func):
        URL_ROUTE[page_name] = func

        def call_func(*args, **kwargs):
            return func(*args, **kwargs)

        return call_func

    return set_route


@route('/login.py')
def login(parm):
    return '这是登陆页面 %s' % time.ctime()


@route('/registered.py')
def registered(parm):
    return '这是注册页面 %s' % time.ctime()


@route('/index.html')
def index(parm):  # 实现模板文件
    db = connect(host='localhost', port=3306, user='root', password='', database='stock', charset='utf8')
    cur = db.cursor()
    cur.execute('select * from info')
    info = cur.fetchall()
    db.close()
    cur.close()
    html = ''
    content = '''
                <tr>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s(元)</td>
                    <td>%s</td>
                    <td>%s</td>
        <td>
            <input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="%s">
        </td>
                </tr>  '''

    for item in info:
        stock_info = [i for i in item]
        html += content % (*stock_info, stock_info[1])
        # print(html)
    with open('./templates/index.html', encoding='utf-8') as f:
        page_content = f.read()
    return re.sub(r'\{%content%\}', html, page_content)


@route('/update/(\d+)\.html')
def index(parm):  # 实现模板文件
    stock_code = parm.group(1)
    db = connect(host='localhost', port=3306, user='root', password='', database='stock', charset='utf8')
    cur = db.cursor()
    cur.execute('select * from info')
    cur.execute('select note_info from focus where info_id = (select id from info where code = %s)', (stock_code,))
    remark = cur.fetchone()
    info = cur.fetchall()
    db.close()
    cur.close()
    print(remark)
    with open('./templates/update.html', encoding='utf-8') as f:
        page_content = f.read()
    page_content = re.sub(r'\{%code%\}', stock_code, page_content)
    page_content = re.sub(r'\{%note_info%\}', remark[0], page_content)
    return page_content


@route('/center.html')
def center(parm):  # 实现模板文件
    # with open('./templates/center.html', encoding='utf-8') as f:
    #     content = f.read()
    #     info = '从数据库查询信息...'
    #     content = re.sub(r'\{%content%\}', info, content)  # 替换模板中数据
    #     return content
    db = connect(host='localhost', port=3306, user='root', password='', database='stock', charset='utf8')
    cur = db.cursor()
    cur.execute('select a.code,a.short,a.chg,a.turnover,a.price,a.highs,b.note_info '
                'from info as a inner join focus as  b on a.id = b.info_id')
    info = cur.fetchall()
    db.close()
    cur.close()
    html = ''
    content = '''
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s(元)</td>
            <td>%s</td>
            <td style="color:red">%s</td>
            <td>
                <a type="button" class="btn btn-default btn-xs" href="/update/%s.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a>
            </td>
            <td>
                <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="%s">
            </td>
        </tr> '''
    for item in info:
        focus_info = [i for i in item]
        html += content % (*focus_info, focus_info[0], focus_info[0])
    with open('./templates/center.html', encoding='utf-8') as f:
        page_content = f.read()
    return re.sub(r'\{%content%\}', html, page_content)


# def application(page_name):
#     if page_name == '/login.py':
#         return login()
#     elif page_name == '/registered.py':
#         return registered()
#     else:
#         return 'not found page'
@route(r'/add/(\d+)\.html')
def add_focus(parm):
    stock_code = parm.group(1)
    print('code:', stock_code)
    db = connect(host='localhost', port=3306, user='root', password='', database='stock', charset='utf8')
    cur = db.cursor()
    # 1.判断stock是否存在
    sql = 'select * from info where code = %s;'
    cur.execute(sql, (stock_code,))
    db.commit()
    if not cur.fetchone():
        db.close()
        cur.close()
        return '没有这只stock（%s）' % stock_code
    # 2.判断是否已关注
    sql = 'select * from focus inner join info on focus.info_id = info.id where info.code = %s'
    cur.execute(sql, (stock_code,))
    db.commit()
    if  cur.fetchone():
        db.close()
        cur.close()
        return '已关注过stock（%s),请勿重复关注' % stock_code
    # 3.添加关注
    sql = 'insert into focus(info_id) select id from info where code = %s'
    cur.execute(sql, (stock_code,))
    db.commit()
    db.close()
    cur.close()
    return '关注成功！'


@route(r'/cancel/(\d+)\.html')
def cancel_focus(parm):
    stock_code = parm.group(1)
    print('code:', stock_code)
    db = connect(host='localhost', port=3306, user='root', password='', database='stock', charset='utf8')
    cur = db.cursor()
    # 1.判断stock是否存在
    sql = 'select * from info where code = %s;'
    cur.execute(sql, (stock_code,))
    db.commit()
    if not cur.fetchone():
        db.close()
        cur.close()
        return '没有这只stock（%s）' % stock_code
    # 2.判断是否已关注
    sql = 'select * from focus inner join info on focus.info_id = info.id where info.code = %s'
    cur.execute(sql, (stock_code,))
    db.commit()
    if not cur.fetchone():
        db.close()
        cur.close()
        return '还未关注过stock（%s)' % stock_code
    # 3.取消关注
    sql = 'delete from focus  where info_id = (select id from info where code = %s)'
    cur.execute(sql, (stock_code,))
    db.commit()
    db.close()
    cur.close()
    return '取消关注成功！'


@route(r'/update/(\d+)/(.*)\.html')
def update_focus(parm):
    stock_code = parm.group(1)
    remark = parm.group(2)  # url的编码
    remark = urllib.parse.unquote(remark)
    print('code:', stock_code)
    db = connect(host='localhost', port=3306, user='root', password='', database='stock', charset='utf8')
    cur = db.cursor()
    # 1.判断stock是否存在
    sql = 'select * from info where code = %s;'
    cur.execute(sql, (stock_code,))
    db.commit()
    if not cur.fetchone():
        db.close()
        cur.close()
        return '没有这只stock（%s）' % stock_code
    # 2.判断是否已关注
    sql = 'select * from focus inner join info on focus.info_id = info.id where info.code = %s'
    cur.execute(sql, (stock_code,))
    db.commit()
    if not cur.fetchone():
        db.close()
        cur.close()
        return '还未关注过stock（%s)' % stock_code
    # 3.取消关注
    sql = 'update focus set note_info = %s where info_id = (select id from info where code = %s)'
    cur.execute(sql, (remark, stock_code))
    db.commit()
    db.close()
    cur.close()
    return '修改备注成功！'


def application(env, response_func):  # 让web服务器支持WSGI协议
    response_func('200 ok', [('content-type', 'text/html;charset=utf-8;')])
    page_name = env['PATH']
    # if page_name == '/login.py':
    #     return login()
    # elif page_name == '/registered.py':
    #     return registered()
    # elif page_name == '/index.py':
    #     return index()
    # elif page_name == '/center.py':
    #     return center()
    # else:
    #     return 'not found page 我不是水水'

    # 配置日志信息
    logging.basicConfig(level='INFO',
                        filename='./log.txt',
                        filemode='a',
                        format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    logging.info('访问的路径：%s' % page_name)

    try:
        for url, func in URL_ROUTE.items():
            match_ret = re.match(url, page_name)
            if match_ret:
                return func(match_ret)
        else:
            logging.warning('url（%s）没有对应的函数...' % page_name)
            return '请求的url（%s）没有对应的函数' % page_name
    except Exception as ex:
        return 'Not Found The Page By Cause:\n %s' % ex

