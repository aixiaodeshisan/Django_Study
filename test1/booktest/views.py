#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件:views.py
@说明:跟接收浏览器请求，进行处理，返回页面相关。
@时间:2019/12/23 11:29:12
@作者:MrShiSan
@版本:1.0
'''

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,RequestContext
from django.shortcuts import render

# Create your views here.
# 定义视图
''' 查找视图过程
1. 在浏览器地址栏中输入url
2. 请求到网站后，获取url信息
3. 然后与编写好的URLconf逐条匹配
    3.1 如果匹配成功则调用对应的视图函数
    3.2 如果所有的URLconf都没有匹配成功，则返回404错误
'''
# def index(request):
#     # # 使用视图调用模板
#     # # 1.获取模板
#     # template=loader.get_template('booktest/index.html')
#     # # 2.定义上下文
#     # context=RequestContext(request,{'title':'图书列表','list':range(10)})
#     # # 3.渲染模板
#     # return HttpResponse(template.render(context))

#     # render(request,"路径","上下文字典")函数封装上述三操作，
#     # 1.定义上下文字典
#     context = {'title':'图书馆列表','list':range(10)}
#     # 2.remder 传参数调用模板（调用前端页面）
#     return render(request,"booktest/index.html",context)
#     pass

''' 完整项目的搭建
    1.定义视图
    2.定义URLconf
    3.定义模板
'''
from booktest.models import BookInfo

# 首页展示所有图书
def index(request):
    # 查询所有图书
    booklist = BookInfo.objects.all()
    # 将图书列表传到模板，然后渲染模板
    return render(request,"booktest/index.html",{'booklist':booklist})
    pass

# 详细页
def detail(request,bid):
    # 根据图书编号对应图书
    book = BookInfo.objects.get(id = int(bid))
    # 获得关联集合:查找book图书中的所有英雄信息,django中提供关联的操作方式
    heros = book.heroinfo_set.all()
    # 将图书信息传递到模板中，然后渲染模板
    return render(request, 'booktest/detail.html', {'book':book,'heros':heros})

    pass