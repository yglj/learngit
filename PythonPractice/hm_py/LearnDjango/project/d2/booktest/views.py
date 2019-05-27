from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from booktest.models import *
from datetime import date
from django.template import loader, RequestContext
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.conf import settings
# Create your views here.


def show_book(request):  # 模型类的查询，删除
    book_list = BookInfo.objects.all()
    return render(request, r'booktest\book_index.html', {
        'book_list': book_list,
    })


def create_book(request):
    book = BookInfo()
    book.b_title = '新增项'
    book.pub_date = date(1990, 1, 1)
    book.save()
    return redirect('/book')
    # return HttpResponse('ok')


def delete_book(request, bid):
    book = BookInfo.objects.get(id=int(bid))
    # book.isDelete = True
    book.delete()
    return redirect('/book')
    # return HttpResponse('ok')


def img(request):
    aimg = FieldExercise.objects.all()
    aimg = aimg[0].seven.read()
    return HttpResponse(aimg)


def current_area(request):  # 自关联查询
    currentArea = AreaInfo.objects.get(id=440100)
    # parentArea = currentArea.parentNode
    # childAreas = currentArea.areainfo_set.all()
    return render(request, 'booktest/current_area.html', {
        'currentArea': currentArea,
        # 'parentArea': parentArea,
        # 'childAreas': childAreas,
    })


def show_args1(request, a):  # urlconf 参数传递
    if  a == '2':
        url = reverse('booktest:a2', kwargs={'arg':'123'})
        return redirect(url)
    return HttpResponse('<h1>展示参数：%s</h1>' % a)


def show_args2(request, arg):
    return HttpResponse('<h1>展示参数：%s</h1>' % arg)


def show_request(request):  # http请求方式及请求参数
    return render(request, 'booktest/request.html')


def show_method(request):
    return HttpResponse('<h1>请求方式：{} </h1>'.format(request.method))


def show_post(request):
    print(request.POST.getlist('hobby'))
    return render(request, 'booktest/post_args.html', {
        'name': request.POST.get('name', 'does not exist'),
        'gender': request.POST.get('gender', 'does not exist'),
        'hobby': request.POST.getlist('hobby'),
    })


def show_get(request):
    return render(request, 'booktest/get_args.html', {
        'a': request.GET.get('a'),
        'b': request.GET['b'],
        'c': request.GET.get('c'),
    })



def my_render(request, path, context):  # HttpResponse对象， render方法渲染模板
    template = loader.get_template(path)
    context = RequestContext(request, context)
    return HttpResponse(template.render(context))



def index_one(request):
    return my_render(request, 'booktest/index_one.html', {
        'one': 'hello',
    })


def json1(request):  # json数据
    return render(request, 'booktest/json1.html')


def json2(request):
    return JsonResponse({'a': 1,
                         'b': 2,
                         'c': 'json',
                         })

def set_cookie(request):  # 状态保持cookie和session
    response = HttpResponse('<h1>已设置cookie，请到后台Network查看</h1>')
    response.set_cookie('project','你好'.encode('utf-8').decode('latin1'))
    print(response.cookies)
    return response


def get_cookie(request):
    response = HttpResponse('<h1>读取cookie数据如下：</h1>')
    if 'project' in request.COOKIES:
        response.write(request.COOKIES['project'])
    return response


def session_test(request):
    request.session['set'] = 'test'
    res = HttpResponse('<h1>设置session</h1>')
    if 'set' in request.session:
        res.write('<h1> session: %s</h1>' % request.session['set'])
    del request.session['set']  # 删除session中的指定键及值，在存储中只删除某个键及对应的值。
    request.session.flush()  # 清除session数据，在存储中删除session的整条数据
    return res


def login(request):
    if 'username' in request.COOKIES:
        username = request.COOKIES['username']
    else:
        username = ''
    return render(request, 'booktest/login.html', {
        'username': username,
    })


def login_require(func): # 登录装饰器
    def wrapper(request, *args, **kwargs):
        if not request.session.has_key('isLogin'):
        # if not request.session.get('isLogin'):
            return redirect('/login')
        else:
            return func(request, *args, **kwargs)
    return wrapper



def login_check(request):
    username = request.POST['username']
    password = request.POST['password']
    remember = request.POST.get('remember')
    verify_code = request.POST.get('verify_code')
    if username == 'bbb' and password == '123':
        request.session['username'] = username
        request.session['isLogin'] = True
        if not verify_code.upper() == request.session['verify_code']:
            return redirect('/login')
        red = redirect('/change_pwd')
        if remember == 'on':
            red.set_cookie('username', username)
        return red
    else:
        return redirect('/login')


@login_require
def change_pwd(request):
    """修改密码,只有在登录状态才能修改"""
    return render(request, 'booktest/change_pwd.html')


@login_require
def change_pwd_action(request):
    """修改密码提交"""
    username = request.session.get('username')
    pwd = request.POST.get('pwd')
    msg = '%s 修改密码为：%s' % (username, pwd)
    return render(request, 'booktest/change_pwd_action.html', {
        'content': msg,
    })


def verify_code(request):
    from PIL import Image, ImageFilter, ImageDraw, ImageFont
    from django.utils.six import BytesIO
    import random

    def rndChar():
        return chr(random.randint(65, 90))

    def rndColor():  # 填充色 rgb
        return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

    def rndColor2():  # 字体色
        return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

    width = 4 * 60  # 4个字符
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))  # 白色底图
    draw = ImageDraw.Draw(image)
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rndColor())  # 每一点随机填充颜色
    font = ImageFont.truetype(r'D:\python\a\Library\lib\fonts\Vera.ttf', 36)  # 无法定位，提供系统绝对资源
    rand_str = ''
    for i in range(4):
        rand_str += rndChar()
        draw.text((60 * i + 10, 10), rand_str[i], font=font, fill=rndColor2())

    # 模糊
    image = image.filter(ImageFilter.BLUR)
    request.session['verify_code'] = rand_str
    buf = BytesIO()
    image.save(buf,'png')
    return HttpResponse(buf.getvalue(), 'image/png')


def temp_tagsAndfilter(request):
    """模板标签，模板过滤器"""
    book = BookInfo.objects.all()
    return render(request, 'booktest/temp_tags.html', {
        'book': book,
    })


def temp_inherit(request):
    """模板继承"""
    return render(request, 'booktest/child.html')


def temp_escape(request):
    """模板继承"""
    return render(request, 'booktest/temp_escape.html', {
        'content': '<h1>templates escape</h1>',
    })


def upload(request):
    """上传文件"""
    return render(request, 'booktest/upload.html')


def upload_handle(request):
    pic = request.FILES.get('pic')
    print(pic.name)
    save_path = '%s/booktest/%s' % (settings.MEDIA_ROOT, pic.name)
    with open(save_path, 'wb') as f:
        for content in pic.chunks():
            f.write(content)
    # FileTest.objects.create(img=pic.name)
    FileTest(img=pic.name).save()
    return HttpResponse('ok')


from django.core.paginator import Paginator
def pagination(request, pid):
    """分页"""
    if pid is '':
        pid = 1
    areas = AreaInfo.objects.filter(parentNode__isnull=True)
    paginator = Paginator(areas, 9)
    page = paginator.page(pid)
    print(paginator.page_range)
    return render(request, 'booktest/pagination.html', {
        'page': page,
        'pid': pid,
    })


# 省市区选择
def getProv(request):
    areas = AreaInfo.objects.filter(parentNode__isnull=True)
    prov_list = []
    for area in areas:
        prov_list.append((area.id, area.title))
    return JsonResponse({'prov': prov_list})


def getCity(request, cid):
    citys = AreaInfo.objects.filter(parentNode_id__exact=str(cid))
    city_list = []
    for city in citys:
        city_list.append((city.id, city.title))
    return JsonResponse({'city': city_list})


def getCounty(request, cid):
    countys = AreaInfo.objects.filter(parentNode_id__exact=str(cid))
    county_list = []
    for county in countys:
        county_list.append((county.id, county.title))
    return JsonResponse({'county': county_list})


def make_html(request):
    return render(request, 'booktest/maketinymce.html', {

    })


def show_html(request):
    htmls = HtmlTest.objects.all()
    content = []
    for html in htmls:
        content.append({html.id, html.ahtml})
    return HttpResponse(content)