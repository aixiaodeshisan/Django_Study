# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0002_heroinfor'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HeroInfor',
            new_name='HeroInfo',
        ),
    ]
