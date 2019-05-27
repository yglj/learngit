# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('b_title', models.CharField(max_length=40)),
                ('pub_date', models.DateField()),
                ('read', models.IntegerField()),
                ('comment', models.CharField(max_length=128)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='RoleInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('r_name', models.CharField(max_length=40)),
                ('render', models.BooleanField(default=False)),
                ('comment', models.CharField(max_length=128)),
                ('book', models.ForeignKey(to='booktest.BookInfo')),
            ],
        ),
    ]
