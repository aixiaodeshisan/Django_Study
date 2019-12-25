#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :0001_initial.py
@说明    :均是通过manage.py执行，生成的第一个迁移文件，但是还需要执行迁移：python manage.py migrate，
         自动帮我们在数据库中生成对应的表格
@时间    :2019/12/22 17:20:56
@作者    :MrShiSan
@版本    :1.0
'''

from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo', # 生成迁移文件后，会将modle.py内的对象对应生成
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('btitle', models.CharField(max_length=20)),
                ('bpub_date', models.DateField()),
            ],
        ),
    ]
