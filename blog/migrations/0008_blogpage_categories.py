# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 10:24
from __future__ import unicode_literals

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20170731_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='categories',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='blog.BlogCategory'),
        ),
    ]
