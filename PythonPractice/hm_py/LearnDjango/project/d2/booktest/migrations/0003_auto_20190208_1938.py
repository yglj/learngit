# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0002_auto_20190208_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinfo',
            name='comment',
            field=models.CharField(max_length=128, default=''),
        ),
    ]
