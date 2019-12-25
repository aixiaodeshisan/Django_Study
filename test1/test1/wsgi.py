"""
WSGI config for test1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件:wsgi.py
@说明:是项目与WSGI兼容的Web服务器入口
@时间:2019/12/23 11:26:51
@作者:MrShiSan
@版本:1.0
'''

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test1.settings")

application = get_wsgi_application()
