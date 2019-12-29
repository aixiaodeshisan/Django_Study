#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :__init__.py
@说明    :是一个空文件，表示当前目录booktest可以当作一个python包使用。调用MySQLdb
@时间    :2019/12/22 16:42:00
@作者    :MrShiSan
@版本    :1.1
'''
import pymysql

# MySQLdb只支持Python2.，还不支持3.，可以用PyMySQL代替。安装方法：pip install PyMySQL，然后再__init__中调用
pymysql.install_as_MySQLdb()