# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-10 02:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20180109_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date_hired',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
