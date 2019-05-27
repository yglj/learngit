# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0003_auto_20190208_1938'),
    ]

    operations = [
        migrations.CreateModel(
            name='FieldExercise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('two', models.NullBooleanField()),
                ('there', models.TextField()),
                ('four', models.DecimalField(max_digits=4, decimal_places=2)),
                ('five', models.FloatField()),
                ('six', models.DateField()),
                ('seven', models.ImageField(blank=True, null=True, db_column='img', upload_to='')),
            ],
        ),
    ]
