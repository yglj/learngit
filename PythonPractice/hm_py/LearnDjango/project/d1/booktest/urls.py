
from django.conf.urls import url, include
from booktest import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index1', views.index1),
    url(r'^index2', views.index2),
    url(r'^temp_index', views.temp_index),
    url(r'^book', views.show_book),
    url(r'^show_book/(\d+)/$', views.detail),
]

