#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件:urls.py
@说明:在应用中定义URLconf,引入mysql
@时间:2019/12/23 23:55:53
@作者:MrShiSan
@版本:1.1
'''

from django.conf.urls import url
from booktest import views

''' 获取值
    1.请求的url被看做是一个普通的python字符串，进行匹配时不包括域名、get或post参数
        http://127.0.0.1:8000/delete1/?a=10,自动会删除域名等
            (1).delete1/
    2.获取值需要在正则表达式中使用小括号，分为两种方式：
        方式一：位置参数
        方式二：关键字参数
'''
urlpatterns = [
    # 配置首页url
    url(r'^$', views.index),
    # 配置详细页url，\d+表示多个数字，小括号用于取值，建议复习下正则表达式
    # url(r'^(\d+)/$',views.detail),
    url(r'^delete(\d+)/$',views.delete),
    url(r'^create/$',views.create),
    url(r'^area/$',views.area),
    # url(r'^show\d+/$',views.show_arg),
    # url(r'^show(\d+)/$',views.show_arg),                  # 直接使用小括号，通过位置参数传递给视图。
    # ?P部分表示为这个参数定义的名称为id，可以是其它名称,对应的视图参数必须一致
    url(r'^show(?P<id1>\d+)/$',views.show_arg),             # 关键字参数
    # 开始显示服务器创建的request对象属性
    url(r'^method_show/$', views.method_show),              # method属性
    url(r'^show_reqarg/$', views.show_reqarg),              # GET、POST属性
    # 开始测试HttpResponse对象
    url(r'^index2/$',views.index2),                         # 直接返回数据
    url(r'^index3/$',views.index3),                         # 调用模板进行回应
    url(r'^index4/$',views.index4),                         # 调用模板简写函数render
    # 开始进行jquery数据的JsonResponse响应
    url(r'^json1/$', views.json1),
    url(r'^json2/$', views.json2),
    # 定义重定义向视图，转向首页
    url(r'^red1/$', views.red1),
    # 重定向简写函数redirect
    url(r'^red2/$', views.red2),
    # 设置Cookies
    url(r'^cookie_set/$',views.cookie_set),
    # 读取cookie
    url(r'^cookie_get/$',views.cookie_get),
    # 写session
    url(r'^session_test/$',views.session_test),
    # 读session
    url(r'^session_read_test/$',views.session_read_test),
    # 删除session
    url(r'^session_delete_test/$',views.session_delete_test),
    # 测试redis数据库 session
    url(r'^session_redis_test/$',views.session_redis_test),
    # 测试模板变量
    url(r'^temp_var/$', views.temp_var),
    # 测试模板标签
    url(r'^temp_tags/$', views.temp_tags),
    # 测试模板过滤器
    url(r'^temp_filter/$', views.temp_filter),
    # 模板继承测试
    url(r'^temp_inherit/$', views.temp_inherit),
    # html转义
    url(r'^html_escape/$', views.html_escape),
    # 创建视图login，login_check, post和post_action
    url(r'^login/$', views.login),
    url(r'^login_check/$', views.login_check),
    url(r'^post/$', views.post),
    url(r'^post_action/$',views.post_action),
    # 测试二维码
    url(r'^verify_code/$', views.verify_code),
    #  调用验证码
    url(r'^verify_show/$', views.verify_show),
    # 验证验证码
    url(r'^verify_yz/$', views.verify_yz),
    # 测试反向解析
    url(r'^fan1/$', views.fan1),
    url(r'^fan2/$', views.fan2),
    # 引入反向解析
    url(r'^fan_show/$', views.fan2,name='fan2'),
    # 传递位置参数
    url(r'^fan(\d+)_(\d+)/$', views.fan3,name='fan3'),
    url(r'^fan4/$',views.fan4,name='fan4'),
    # 传递关键字参数，和单纯的传参数区别主要在于
    url(r'^fan(?P<id>\d+)_(?P<age>\d+)/$', views.fan5,name='fan5'),
    # 主意正则里面的下滑线有特殊定义，不能瞎用
    url(r'^fan51/$',views.fan51,name='fan5_1'),
]

# 全局403、404、500错误自定义页面显示
handler404 = views.page_not_found
handler403 = views.permission_denied
handler505 = views.page_error