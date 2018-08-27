# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core import blocks
from wagtail.core.blocks import BlockQuoteBlock
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock


class HistoricalEvent(blocks.StructBlock):
    year = blocks.CharBlock()
    desc = blocks.RichTextBlock()

    class Meta:
        template = 'blocks/historical-event.html'


class ContentPage(Page):
    subtitle = models.CharField(max_length=250, default='')
    intro = RichTextField(blank=True)
    body = StreamField([
        ('heading', blocks.CharBlock(classname='full title')),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('quote', BlockQuoteBlock()),
        ('historical_event', HistoricalEvent())
    ])

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('intro'),
        StreamFieldPanel('body')
    ]
