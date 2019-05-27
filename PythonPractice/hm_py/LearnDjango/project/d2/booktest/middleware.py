# 中间件
from django.http import HttpResponse

class BanIpsMiddleWare:
    ban_IPs = ['192.168.25.133']

    def __init__(self):
        # 初始化：无需任何参数，服务器响应第一个请求的时候调用一次，用于确定是否启用当前中间件
        print('=======init=========')

    def process_request(self, request):
        # 处理请求前：在每个请求上，request对象产生之后，url匹配之前调用，返回None或HttpResponse对象。
        print(request.META['REMOTE_ADDR'])
        if request.META['REMOTE_ADDR'] in BanIpsMiddleWare.ban_IPs:
            return HttpResponse('<h1>Forbidden request</h1>')

        print('------------request process--------------')

    def process_view(self, request, *args, **kwargs):
        # 处理视图前：在每个请求上，url匹配之后，视图函数调用之前调用，返回None或HttpResponse对象。
        print('------------request view--------------')

    def process_response(self, request, response):
        # 处理响应后：视图函数调用之后，所有响应返回浏览器之前被调用，在每个请求上调用，返回HttpResponse对象
        print('------------request response--------------')
        return response

    def process_exception(self, request, exception):
        print('this message in process_exception :\n%s' % exception)


