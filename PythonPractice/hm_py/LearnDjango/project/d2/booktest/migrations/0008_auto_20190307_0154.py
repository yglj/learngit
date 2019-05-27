# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0007_auto_20190307_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filetest',
            name='img',
            field=models.ImageField(verbose_name='上传图片', upload_to='booktest/'),
        ),
    ]
