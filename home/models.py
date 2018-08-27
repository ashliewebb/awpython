from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.core.blocks import BlockQuoteBlock
from wagtail.admin.edit_handlers import StreamFieldPanel


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
