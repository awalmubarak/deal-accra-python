# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-11-10 11:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0005_auto_20161108_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='Contact_number',
            field=models.CharField(default=datetime.datetime(2016, 11, 10, 11, 54, 35, 474686, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
