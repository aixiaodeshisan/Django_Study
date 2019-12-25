#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :models.py
@说明    :文件跟数据库操作相关,ORM映射操作数据库
@时间    :2019/12/22 16:41:01
@作者    :MrShiSan
@版本    :1.0
'''
from django.db import models

# Create your models here.
# 图书类
class BookInfo(models.Model):
    btitle = models.CharField(max_length = 20)
    bpub_date = models.DateField()                      # data 型
    
    # 重写str函数
    def __str__(self):
        # 返回书的标题,否则把对象名对象返回
        return self.btitle

# 一本书里对应多个英雄，在生成表后，默认会生成一个id对应主键
class HeroInfo(models.Model):
    hname = models.CharField(max_length = 20)           # Vchar 型
    hgender = models.BooleanField()                     # Bool 型
    hcomment = models.CharField(max_length = 100)
    hbook = models.ForeignKey("BookInfo")               # 这句代码就让BookInfo类和HeroInfo类之间建立了一对多的关，通过外键联系。

    def __str__(self):
        # 返回英雄名
        return self.hname