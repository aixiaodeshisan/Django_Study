# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0004_auto_20191225_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinfo',
            name='btitle',
            field=models.CharField(max_length=20, db_column='title'),
        ),
        migrations.AlterField(
            model_name='heroinfo',
            name='hcomment',
            field=models.CharField(null=True, max_length=200),
        ),
    ]
