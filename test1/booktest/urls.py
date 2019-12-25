#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件:urls.py
@说明:在应用中定义URLconf
@时间:2019/12/23 23:55:53
@作者:MrShiSan
@版本:1.0
'''

from django.conf.urls import url
from booktest import views

urlpatterns = [
    # 配置首页url
    url(r'^$', views.index),
    # 配置详细页url，\d+表示多个数字，小括号用于取值，建议复习下正则表达式
    url(r'^(\d+)/$',views.detail),
]