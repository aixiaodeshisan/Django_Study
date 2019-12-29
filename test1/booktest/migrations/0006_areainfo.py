# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0005_auto_20191225_1942'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('atitle', models.CharField(max_length=30)),
                ('aParent', models.ForeignKey(blank=True, null=True, to='booktest.AreaInfo')),
            ],
        ),
    ]
