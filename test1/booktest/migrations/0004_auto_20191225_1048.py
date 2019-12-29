# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0003_auto_20191222_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinfo',
            name='bcomment',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='bread',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='isDelete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='heroinfo',
            name='isDelete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='heroinfo',
            name='hcomment',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='heroinfo',
            name='hgender',
            field=models.BooleanField(default=True),
        ),
    ]
