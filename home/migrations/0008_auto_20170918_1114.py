# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-18 11:14
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20170918_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([('quote', wagtail.wagtailcore.blocks.StructBlock([(b'quote', wagtail.wagtailcore.blocks.BlockQuoteBlock(max_length=225, required=True)), (b'quotee', wagtail.wagtailcore.blocks.CharBlock(classname='quotee'))]))]),
        ),
    ]
