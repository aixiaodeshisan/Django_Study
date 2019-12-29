# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('ntitle', models.CharField(max_length=60)),
                ('ncontent', models.TextField()),
                ('npub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('tname', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='newsinfo',
            name='ntype',
            field=models.ManyToManyField(to='newstest.TypeInfo'),
        ),
    ]
