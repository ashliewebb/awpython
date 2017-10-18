from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.blocks import BlockQuoteBlock
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel


class QuoteBlock(blocks.StructBlock):
    quote = BlockQuoteBlock(required=True, max_length=225)
    quotee = blocks.CharBlock(classname='quotee')

    class Meta:
        template = 'blocks/quote.html'


class HomePage(Page):
    intro = StreamField([
        ('quote', QuoteBlock())
    ])

    # body = StreamField([
    #     ('quote', QuoteBlock())
    # ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('intro')
        # StreamFieldPanel('body')
    ]
