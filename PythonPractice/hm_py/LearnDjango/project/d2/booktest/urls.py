from django.conf.urls import include, url
from booktest import views

urlpatterns = [
    url(r'^book/', views.show_book),
    url(r'^create_book/', views.create_book),
    url(r'^delete_book(\d+)/', views.delete_book),
    url(r'^img/', views.img),

    url(r'^area/', views.current_area),
    url(r'^args1_(\d+)/$', views.show_args1, name='a1'),  # urlconf 位置参数, url反向解析
    url(r'^args2_(?P<arg>\d+)/$', views.show_args2, name='a2'),  # urlconf 指定url与视图函数的对应关系 关键字参数

    url(r'^show_request/', views.show_request),
    url(r'^show_method/', views.show_method),
    url(r'^show_post/', views.show_post),
    url(r'^show_get/', views.show_get),
    url(r'^index_one/', views.index_one, name='index'),

    url(r'^json1/', views.json1),
    url(r'^json2/', views.json2),

    url(r'^get_cookie/', views.get_cookie),
    url(r'^set_cookie/', views.set_cookie),
    url(r'^session_test', views.session_test),
    url(r'^login/', views.login),
    url(r'^login_check', views.login_check),
    url(r'^change_pwd/', views.change_pwd),
    url(r'^change_pwd_action', views.change_pwd_action),
    url(r'^verify_code/$', views.verify_code),

    url(r'^temps/', views.temp_tagsAndfilter),
    url(r'^temp_inherit/', views.temp_inherit),
    url(r'^temp_escape/', views.temp_escape),

    url(r'^upload/', views.upload),  # 不以/结尾会贪婪匹配
    url(r'^upload_handle/', views.upload_handle),
    url(r'^page(?P<pid>\d*)/', views.pagination, name='page'),
    url(r'^get_prov/', views.getProv),
    url(r'^get_city/(?P<cid>\d+)/', views.getCity),
    url(r'^get_county/(?P<cid>\d+)/', views.getCounty),

    url(r'^make_html/', views.make_html),
    url(r'^show_html/', views.show_html),
]
