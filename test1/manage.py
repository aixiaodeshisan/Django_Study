#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :manage.py
@说明    :项目管理文件，通过它管理项目
@时间    :2019/12/22 16:43:45
@作者    :MrShiSan
@版本    :1.0
'''

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test1.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
