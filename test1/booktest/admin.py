#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :admin.py
@说明    :跟网站的后台管理相关
@时间    :2019/12/22 16:42:18
@作者    :MrShiSan 
@版本    :1.0
'''

from django.contrib import admin
from booktest.models import BookInfo,HeroInfo

# 自定义管理页面的功能，比如列表页要显示哪些值。
# 默认在列表页只显示出了BookInfo object，对象的其它属性并没有列出来，查看非常不方便
class BookInfoAdmin(admin.ModelAdmin):
    # 定义清单中要显示,注要在下面注册本类
    list_display = ['id','btitle','bpub_date']

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id','hname','hgender','hcomment','hbook']


# Register your models here.
admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)