# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0004_fieldexercise'),
    ]

    operations = [
        migrations.AddField(
            model_name='roleinfo',
            name='isDelete',
            field=models.BooleanField(default=0),
        ),
    ]
