#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件：filters.py
@说明：测试自定义过滤器
@时间：2019/12/28 11:06:32
@作者：MrShiSan
@版本：1.0
@运行环境：Python3.5 + Django1.8.2
'''

#导入Library类
from django.template import Library

#创建一个Library类对象
register=Library()

#使用装饰器进行注册
@register.filter
#定义求余函数mod，将value对2求余
def mod(value):
    return value%2 == 0
