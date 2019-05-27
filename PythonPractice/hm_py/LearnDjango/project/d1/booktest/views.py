from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext
from booktest.models import Book, Role
# Create your views here.

def my_render(request, temp_path, temp_dict):
     print(temp_path)
     templates = loader.get_template(temp_path)
     context = RequestContext(request, temp_dict)
     res_html = templates.render(context)
     return HttpResponse(res_html)
     

def index1(request):
     return HttpResponse('首页1')


def index2(request):
     return HttpResponse('Ni Hao')


def index(request):
     return HttpResponse('<h1>begain</h1>')


def temp_index(request):
     return my_render(request, r'booktest\temp_index.html', {
          'p_one': '列表：1-9',
          'list': range(1,10)
          })


def show_book(request):
     book_list = Book.objects.all()
     return render(request, r'booktest\show_book.html', {
          'booklist': book_list,
          })


def detail(request, bid):
     book = Book.objects.get(id=int(bid))
     roles = book.role_set.all()
     return render(request, r'booktest\detail.html', {
          'book': book,
          'roles': roles,
          })

