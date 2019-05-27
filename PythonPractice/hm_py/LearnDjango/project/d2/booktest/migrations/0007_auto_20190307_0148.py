# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0006_areainfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('img', models.ImageField(verbose_name='上传图片', upload_to='')),
            ],
        ),
        migrations.AlterModelTable(
            name='bookinfo',
            table='booktest_bookinfo',
        ),
    ]
