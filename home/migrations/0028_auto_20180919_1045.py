# Generated by Django 2.0.8 on 2018-09-19 10:45

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_homepage_props'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('quote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.BlockQuoteBlock(max_length=225, required=True)), ('quotee', wagtail.core.blocks.CharBlock(classname='quotee'))]))]),
        ),
    ]
