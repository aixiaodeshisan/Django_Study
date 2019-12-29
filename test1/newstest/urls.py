#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件:url.py
@说明:
@时间:2019/12/26 11:53:08
@作者:MrShiSan
@版本:1.0
'''
from django.conf.urls import url
from newstest import views

urlpatterns = [
    # 配置首页url
    url(r'^$', views.index),
]