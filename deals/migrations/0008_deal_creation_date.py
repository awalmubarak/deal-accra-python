# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-11-10 16:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0007_auto_20161110_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 11, 10, 16, 45, 23, 303195, tzinfo=utc)),
            preserve_default=False,
        ),
    ]