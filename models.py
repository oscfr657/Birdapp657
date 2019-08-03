
from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel


from .blocks import BirdCodeBlock


class BirdBasePage(Page):
    author = models.CharField(max_length=255, blank=True, null=True)
    coverImage = models.ForeignKey(
        'wagtailimages.Image',
        blank=True, null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    intro = RichTextField(
        blank=True, null=True,
        features=[
            'h2', 'h3', 'h4',
            'bold', 'italic',
            'superscript', 'subscript', 'strikethrough'
            'ol', 'ul', 'hr',
            'link', 'document-link', 'blockquote']
            )

    content_panels = Page.content_panels + [
        FieldPanel('author'),
        ImageChooserPanel('coverImage'),
        FieldPanel('intro', classname="full")
    ]

    def get_context(self, request):
        context = super().get_context(request)
        try:
            section_root_page = Page.objects.ancestor_of(self)[2]
        except IndexError:
            section_root_page = self
        context['section_root_page'] = section_root_page
        return context


class BirdPage(BirdBasePage):
    body = StreamField([
        # ? ('heading', blocks.CharBlock(classname="full title",required=False,null=True)),
        ('paragraph', blocks.RichTextBlock(
            required=False, null=True,
            features=[
                'h2', 'h3', 'h4',
                'bold', 'italic',
                'superscript', 'subscript', 'strikethrough'
                'ol', 'ul', 'hr',
                'link', 'document-link', 'blockquote'])),
        ('image', ImageChooserBlock(required=False, null=True)),
        ('code', BirdCodeBlock(required=False, null=True)),
    ], blank=True, null=True)

    content_panels = BirdBasePage.content_panels + [
        StreamFieldPanel('body'),
    ]
