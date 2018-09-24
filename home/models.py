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
        icon = 'openquote'
        template = 'blocks/quote.html'


class ValueProp(blocks.StructBlock):
    name = blocks.CharBlock()
    icon = blocks.CharBlock()
    link = blocks.CharBlock(required=False)

    class Meta:
        icon = 'success'
        template = 'blocks/value-prop.html'


class HomePage(Page):
    intro = StreamField([
        ('quote', QuoteBlock())
    ], blank=True)

    props = StreamField([
        ('prop', ValueProp())
    ], blank=True)

    body = StreamField([
        ('quote', QuoteBlock()),
        ('heading', blocks.CharBlock(classname='full title', icon='title')),
        ('paragraph', blocks.RichTextBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('intro'),
        StreamFieldPanel('props'),
        StreamFieldPanel('body')
    ]
