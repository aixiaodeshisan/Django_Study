"""test1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件:urls.py
@说明:是项目的URL配置文件
@时间:2019/12/23 11:27:38
@作者:MrShiSan
@版本:1.1
'''

from django.conf.urls import include, url
from django.contrib import admin

''' URLconf注意点
    1.在test1/urls.py中进行包含配置，在各自应用中创建具体配置。
    2.定义urlpatterns列表，存储url()对象，这个名称是固定的。
        urlpatterns中的每个正则表达式在第一次访问它们时被编译，这使得运行很快。
    url()对象，被定义在django.conf.urls包中，有两种语法结构：
    1.包含，一般在自定义应用中创建一个urls.py来定义url。
        这种语法用于test1/urls.py中，目的是将应用的urls配置到应用内部，数据更清晰并且易于维护。
        url(正则,include('应用.urls'))
    2.语法二：定义，指定URL和视图函数的对应关系。
        在应用内部创建urls.py文件，指定请求地址与视图的对应关系。
        url(正则,'视图函数名称')
        url(r'^$',views.index),
        正则部分推荐使用r，表示字符串不转义，这样在正则表达式中使用\只写一个就可以
        不能在开始加反斜杠，推荐在结束加反斜杠
'''
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # 引入booktest的url配置
    url(r'^', include('booktest.urls')),            # 为urlpatterns列表增加项booktest.urls
    # 引入booktest的url配置
    url(r'^', include('newstest.urls')),
    # 引入反向解析
    url(r'^',include('booktest.urls',namespace='booktest')),
]
