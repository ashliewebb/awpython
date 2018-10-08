# Generated by Django 2.0.8 on 2018-09-24 10:14

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_auto_20180919_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='props',
            field=wagtail.core.fields.StreamField([('prop', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock()), ('icon', wagtail.core.blocks.CharBlock()), ('link', wagtail.core.blocks.CharBlock(required=False))]))], blank=True),
        ),
    ]
