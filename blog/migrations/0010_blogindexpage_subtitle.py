# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-18 11:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20170731_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogindexpage',
            name='subtitle',
            field=models.CharField(default='', max_length=255),
        ),
    ]
