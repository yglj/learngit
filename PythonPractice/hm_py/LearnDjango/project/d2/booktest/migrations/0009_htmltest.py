# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0008_auto_20190307_0154'),
    ]

    operations = [
        migrations.CreateModel(
            name='HtmlTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('ahtml', tinymce.models.HTMLField()),
            ],
        ),
    ]
