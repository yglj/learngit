# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('rname', models.CharField(max_length=20)),
                ('render', models.BooleanField(default=False)),
                ('comment', models.CharField(max_length=128)),
                ('rbook', models.ForeignKey(to='booktest.book')),
            ],
        ),
    ]
