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

''' @note 请求的url的获取值
    1.请求的url被看做是一个普通的python字符串，进行匹配时不包括域名、get或post参数
        http://127.0.0.1:8000/delete1/?a=10,自动会删除域名等
            (1).delete1/
    2.获取值需要在正则表达式中使用小括号，分为两种方式：
        方式一：位置参数
        方式二：关键字参数
'''
urlpatterns = [
    # @audit-ok -配置首页url
    url(r'^$', views.index),
    # @audit-ok -配置详细页url，\d+表示多个数字，小括号用于取值，建议复习下正则表达式
    # url(r'^(\d+)/$',views.detail),
    url(r'^delete(\d+)/$',views.delete),
    url(r'^create/$',views.create),
    url(r'^area/$',views.area),
    # url(r'^show\d+/$',views.show_arg),
    # url(r'^show(\d+)/$',views.show_arg),                  # 直接使用小括号，通过位置参数传递给视图。
    # @audit-ok - ?P部分表示为这个参数定义的名称为id，可以是其它名称,对应的视图参数必须一致
    url(r'^show(?P<id1>\d+)/$',views.show_arg),             # 关键字参数
    # 开始显示服务器创建的request对象属性
    url(r'^method_show/$', views.method_show),              # method属性
    url(r'^show_reqarg/$', views.show_reqarg),              # GET、POST属性
    # @audit-ok - 开始测试HttpResponse对象
    url(r'^index2/$',views.index2),                         # 直接返回数据
    url(r'^index3/$',views.index3),                         # 调用模板进行回应
    url(r'^index4/$',views.index4),                         # 调用模板简写函数render
    # @audit-ok - 开始进行jquery数据的JsonResponse响应
    url(r'^json1/$', views.json1),
    url(r'^json2/$', views.json2),
    # @audit-ok - 定义重定义向视图，转向首页
    url(r'^red1/$', views.red1),
    # @audit-ok -重定向简写函数redirect
    url(r'^red2/$', views.red2),
    # @audit-ok -设置Cookies
    url(r'^cookie_set/$',views.cookie_set),
    # @audit-ok -读取cookie
    url(r'^cookie_get/$',views.cookie_get),
    # @audit-ok -写session
    url(r'^session_test/$',views.session_test),
    # @audit-ok -读session
    url(r'^session_read_test/$',views.session_read_test),
    # @audit-ok -删除session
    url(r'^session_delete_test/$',views.session_delete_test),
    # @audit-ok -测试redis数据库 session
    url(r'^session_redis_test/$',views.session_redis_test),
    # @audit-ok -测试模板变量
    url(r'^temp_var/$', views.temp_var),
    # @audit-ok -测试模板标签
    url(r'^temp_tags/$', views.temp_tags),
    # @audit-ok -测试模板过滤器
    url(r'^temp_filter/$', views.temp_filter),
    # @audit-ok -模板继承测试
    url(r'^temp_inherit/$', views.temp_inherit),
    # @audit-ok -html转义
    url(r'^html_escape/$', views.html_escape),
    # @audit-ok -创建视图login，login_check, post和post_action
    url(r'^login/$', views.login),
    url(r'^login_check/$', views.login_check),
    url(r'^post/$', views.post),
    url(r'^post_action/$',views.post_action),
    # @audit-ok -测试二维码
    url(r'^verify_code/$', views.verify_code),
    # @audit-ok -调用验证码
    url(r'^verify_show/$', views.verify_show),
    # 验证验证码
    url(r'^verify_yz/$', views.verify_yz),
    # @audit-ok -测试反向解析
    url(r'^fan1/$', views.fan1),
    url(r'^fan2/$', views.fan2),
    # @audit-ok -引入反向解析
    url(r'^fan_show/$', views.fan2,name='fan2'),
    # @audit-ok -传递位置参数
    url(r'^fan(\d+)_(\d+)/$', views.fan3,name='fan3'),
    url(r'^fan4/$',views.fan4,name='fan4'),
    # @audit-ok -传递关键字参数，和单纯的传参数区别主要在于
    url(r'^fan(?P<id>\d+)_(?P<age>\d+)/$', views.fan5,name='fan5'),
    # @audit-ok -主意正则里面的下滑线有特殊定义，不能瞎用
    url(r'^fan51/$',views.fan51,name='fan5_1'),
    # @audit-ok 静态页面的配置
    url(r'^static_test/$',views.static_test,name='static'),
    # @audit-ok 测试中间件
    url(r'^mid_test/$',views.mid_test,name='mid'),
    # @audit-ok 自定义表单上传图片
    url(r'^pic_upload/$', views.pic_upload),
    # @audit-ok 用作接收表单保存图片
    url(r'^pic_handle/$', views.pic_handle),
    # @audit-ok 显示上传图片
    url(r'^pic_show/$', views.pic_show),
    # @audit-ok 显示页码
    url(r'^page(?P<pIndex>[0-9]*)/$', views.page_test),
    # @audit-ok 显示下拉列表控件,专让用户和数据交互
    url(r'^area1/$', views.area1),
    # @audit-ok 获取具体数据
    url(r'^area2/$', views.area2),
    # @audit-ok 根据编号获取对应的子级信息
    url(r'^area3_(\d+)/$', views.area3),
    # @audit-ok 测试Django第三方模块
    url(r'^third_party_pack/$',views.third_pack_test),
    # @audit-ok 自定义视图使用富文本编辑器
    url(r'^editor/',views.editor),
    # @audit-ok 关闭模板中默认html转义
    url(r'^show_tinymce/', views.show_tinymce),
    # @audit-ok 使用全文检索（第三方库）
    url(r'^query/', views.query),
    # @audit-ok 发送邮件(第三方，以XXX.@160.com)
    url(r'^send/$',views.send),
    # @audit-ok celery分布式分布式任务类别，处理大量消息的分布式系统，耗时的程序要放过来
    url(r'^sayhello$',views.sayhello),
]

# @audit-ok -全局403、404、500错误自定义页面显示
handler404 = views.page_not_found
handler403 = views.permission_denied
handler505 = views.page_error