# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-18 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentpage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentpage',
            name='subtitle',
            field=models.CharField(default='', max_length=250),
        ),
    ]
