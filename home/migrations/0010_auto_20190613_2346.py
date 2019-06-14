# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-13 23:46
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20171018_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='intro',
            field=wagtail.wagtailcore.fields.StreamField((('quote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.BlockQuoteBlock(max_length=225, required=True)), ('quotee', wagtail.wagtailcore.blocks.CharBlock(classname='quotee'))))),)),
        ),
    ]