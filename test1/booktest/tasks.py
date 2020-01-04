#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件：tasks.py
@说明：Celery-分布式-task任务模块
@时间：2020/01/04 22:51:13
@作者：MrShiSan
@版本：1.0
@运行环境：Python3.5 + Django1.8.2
'''

import time
from celery import task

# @task
# def sayhello():
#     print('hello ...')
#     time.sleep(2)
#     print('world ...')

# @note 修改为发送邮件的代码，就可以实现无阻塞发送邮件。
from django.conf import settings
from django.core.mail import send_mail

@task
def sayhello():
    msg='<a href="http://www.itcast.cn/subject/pythonzly/index.shtml" target="_blank">点击激活</a>'
    send_mail('注册激活','',settings.EMAIL_FROM,
              ['itcast88@163.com'],
              html_message=msg)