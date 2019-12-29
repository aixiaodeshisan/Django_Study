#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件:models.py
@说明:新闻类和新闻类型模型，多对多关系
@时间:2019/12/26 11:35:27
@作者:MrShiSan
@版本:1.0
'''

from django.db import models

# Create your models here.
# 一个新闻类型下可以用很多条新闻，一条新闻也可能归属于多种新闻类型。
class TypeInfo(models.Model):
  tname = models.CharField(max_length=20)               # 新闻类别

class NewsInfo(models.Model):
  ntitle = models.CharField(max_length=60)              # 新闻标题
  ncontent = models.TextField()                         # 新闻内容
  npub_date = models.DateTimeField(auto_now_add=True)   # 新闻发布时间
  ntype = models.ManyToManyField('TypeInfo')            # 通过ManyToManyField建立TypeInfo类和NewsInfo类之间多对多的关系
