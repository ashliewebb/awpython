# Generated by Django 2.0.8 on 2018-09-19 10:38

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_auto_20180919_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='props',
            field=wagtail.core.fields.StreamField([('props', wagtail.core.blocks.StreamBlock([('prop', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock()), ('icon', wagtail.core.blocks.CharBlock()), ('link', wagtail.core.blocks.CharBlock(required=False))], icon='success'))]))], blank=True),
        ),
    ]