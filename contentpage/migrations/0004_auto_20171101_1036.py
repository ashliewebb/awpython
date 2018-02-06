# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 10:36
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('contentpage', '0003_auto_20171018_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('quote', wagtail.wagtailcore.blocks.BlockQuoteBlock()), ('historical_event', wagtail.wagtailcore.blocks.StructBlock([(b'year', wagtail.wagtailcore.blocks.CharBlock()), (b'desc', wagtail.wagtailcore.blocks.RichTextBlock())]))]),
        ),
    ]
