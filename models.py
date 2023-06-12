import requests
from django.db import models
from django.shortcuts import render
from django import forms

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField, StreamField
from wagtail.blocks import RichTextBlock

from wagtail.search import index

from wagtail.admin.panels import (
    FieldPanel,
    InlinePanel,
)

from wagtail.images.blocks import ImageChooserBlock

from wagtail.contrib.forms.models import AbstractForm, AbstractFormField
from wagtail.contrib.forms.panels import FormSubmissionsPanel

from wagtail.contrib.settings.models import BaseSiteSetting, register_setting

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from modelcluster.contrib.taggit import ClusterTaggableManager

from taggit.models import TaggedItemBase

from .blocks import (
    HeroBirdBlock,
    HeroBTBirdBlock,
    BirdCodeBlock,
    HTMLBirdBlock,
    MediaFileBirdBlock,
    FeedBirdBlock,
    RacerBirdBlock,
    SimpleRacerBirdBlock,
    GridBirdBlock,
    SimpleGridBirdBlock,
    HighGridBirdBlock,
    ColumnBirdBlock,
)


class FontFace(Orderable):
    brand = ParentalKey(
        'BirdAppSettings', related_name='brand_fonts', on_delete=models.CASCADE
    )
    src_file = models.ForeignKey(
        'wagtaildocs.Document', on_delete=models.CASCADE, related_name='+'
    )
    font_family = models.CharField(max_length=50)
    font_format = models.CharField(max_length=50)
    panels = [
        FieldPanel('src_file'),
        FieldPanel('font_family'),
        FieldPanel('font_format'),
    ]


@register_setting
class BirdAppSettings(BaseSiteSetting, ClusterableModel):
    icon = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    logo = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    show_name = models.BooleanField(default=True)
    lang_code = models.CharField(max_length=5, blank=True, null=True)
    extra_head = models.TextField(blank=True, null=True)
    extra_css = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    extra_js = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    footer = StreamField(
        [
            (
                'paragraph',
                RichTextBlock(
                    required=False,
                    null=True,
                    features=[
                        'h2',
                        'h3',
                        'h4',
                        'bold',
                        'italic',
                        'superscript',
                        'subscript',
                        'strikethrough',
                        'ol',
                        'ul',
                        'hr',
                        'link',
                        'document-link',
                        'blockquote',
                    ],
                ),
            ),
            ('html', HTMLBirdBlock(required=False, null=True)),
        ],
        blank=True,
        null=True,
        use_json_field=True,
    )

    panels = [
        FieldPanel('icon'),
        FieldPanel('logo'),
        FieldPanel('show_name'),
        FieldPanel('lang_code'),
        FieldPanel('extra_head'),
        FieldPanel('extra_css'),
        FieldPanel('extra_js'),
        InlinePanel('brand_fonts', label="Brand fontfaces"),
        FieldPanel('footer'),
    ]


class BirdMixin(models.Model):
    image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    intro = RichTextField(
        blank=True,
        null=True,
        features=[
            'h2',
            'h3',
            'h4',
            'bold',
            'italic',
            'superscript',
            'subscript',
            'strikethrough',
            'ol',
            'ul',
            'hr',
            'link',
            'document-link',
            'blockquote',
        ],
    )
    show_breadcrumbs = models.BooleanField(default=False)
    transparent_header = models.BooleanField(default=False)
    hide_header = models.BooleanField(default=False)
    exclude_from_sitemap = models.BooleanField(default=False)

    class Meta:
        abstract = True

    search_fields = [
        index.SearchField('intro'),
    ]
    content_panels = [
        FieldPanel('owner'),
        FieldPanel('image'),
        FieldPanel('intro'),
    ]
    settings_panels = [
        FieldPanel('show_breadcrumbs'),
        FieldPanel('transparent_header'),
        FieldPanel('hide_header'),
        FieldPanel('exclude_from_sitemap'),
    ]


class SoloBirdPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'SoloBirdPage', on_delete=models.CASCADE, related_name='tagged_items'
    )


class SoloBirdPage(Page, BirdMixin):
    body = StreamField(
        [
            (
                'paragraph',
                RichTextBlock(
                    required=False,
                    null=True,
                    features=[
                        'h2',
                        'h3',
                        'h4',
                        'bold',
                        'italic',
                        'superscript',
                        'subscript',
                        'strikethrough',
                        'ol',
                        'ul',
                        'hr',
                        'link',
                        'document-link',
                        'blockquote',
                        'embed',
                        'image',
                    ],
                ),
            ),
            ('columns', ColumnBirdBlock(required=False, null=True)),
            ('image', ImageChooserBlock(required=False, null=True)),
            ('media', MediaFileBirdBlock(required=False, null=True)),
            ('code', BirdCodeBlock(required=False, null=True)),
            ('html', HTMLBirdBlock(required=False, null=True)),
            ('hero', HeroBirdBlock(required=False, null=True)),
            ('hero_bt', HeroBTBirdBlock(required=False, null=True)),
            ('feed', FeedBirdBlock(required=False)),
            ('grid', GridBirdBlock(required=False)),
            ('simplegrid', SimpleGridBirdBlock(required=False)),
            ('highgrid', HighGridBirdBlock(required=False)),
            ('racer', RacerBirdBlock(required=False, null=True)),
            ('simpleracer', SimpleRacerBirdBlock(required=False, null=True)),
        ],
        blank=True,
        null=True,
        use_json_field=True,
    )

    tags = ClusterTaggableManager(through=SoloBirdPageTag, blank=True)

    search_fields = (
        Page.search_fields
        + BirdMixin.search_fields
        + [
            index.SearchField('body'),
            index.SearchField('tags'),
        ]
    )

    content_panels = (
        Page.content_panels
        + BirdMixin.content_panels
        + [
            FieldPanel('body'),
        ]
    )
    promote_panels = Page.promote_panels + [
        FieldPanel('tags'),
    ]
    settings_panels = Page.settings_panels + BirdMixin.settings_panels

    def get_sitemap_urls(self, request=None):
        if self.exclude_from_sitemap:
            return []
        else:
            return super(SoloBirdPage, self).get_sitemap_urls(request=request)


class FormField(AbstractFormField):
    page = ParentalKey(
        'FormBirdPage', on_delete=models.CASCADE, related_name='form_fields'
    )


class FormBirdPage(AbstractForm, BirdMixin):

    prolog = StreamField(
        [
            (
                'paragraph',
                RichTextBlock(
                    required=False,
                    null=True,
                    features=[
                        'h2',
                        'h3',
                        'h4',
                        'bold',
                        'italic',
                        'superscript',
                        'subscript',
                        'strikethrough',
                        'ol',
                        'ul',
                        'hr',
                        'link',
                        'document-link',
                        'blockquote',
                        'embed',
                        'image',
                    ],
                ),
            ),
            ('image', ImageChooserBlock(required=False, null=True)),
            ('media', MediaFileBirdBlock(required=False, null=True)),
            ('hero', HeroBirdBlock(required=False, null=True)),
            ('hero_bt', HeroBTBirdBlock(required=False, null=True)),
            ('racer', RacerBirdBlock(required=False, null=True)),
            ('simpleracer', SimpleRacerBirdBlock(required=False, null=True)),
            ('columns', ColumnBirdBlock(required=False, null=True)),
        ],
        blank=True,
        null=True,
        use_json_field=True,
    )

    thank_you_text = RichTextField(
        blank=True,
        null=True,
        features=[
            'h2',
            'h3',
            'h4',
            'bold',
            'italic',
            'superscript',
            'subscript',
            'strikethrough',
            'ol',
            'ul',
            'hr',
            'link',
            'document-link',
            'blockquote',
            'embed',
            'image',
        ],
    )
    reCaptcha_key = models.CharField(max_length=50, blank=True, null=True)
    reCaptcha_secret = models.CharField(max_length=50, blank=True, null=True)
    # post_scriptum = StreamField(...

    content_panels = (
        AbstractForm.content_panels
        + BirdMixin.content_panels
        + [
            FieldPanel('prolog'),
            FieldPanel('reCaptcha_key'),
            FieldPanel('reCaptcha_secret'),
            FieldPanel('thank_you_text'),
            InlinePanel('form_fields', label="Form fields"),
            FormSubmissionsPanel(),
        ]
    )
    settings_panels = Page.settings_panels + BirdMixin.settings_panels

    def get_sitemap_urls(self, request=None):
        if self.exclude_from_sitemap:
            return []
        else:
            return super(FormBirdPage, self).get_sitemap_urls(request=request)

    def serve(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = self.get_form(
                request.POST, request.FILES, page=self, user=request.user
            )
            if form.data.get('bird_pot'):
                return self.render_landing_page(request, None, *args, **kwargs)
            if self.reCaptcha_key and form.is_valid():
                if not form.data.get('g-recaptcha-response'):
                    return self.render_landing_page(request, None, *args, **kwargs)
                recaptcha_response = requests.post(
                    'https://www.google.com/recaptcha/api/siteverify',
                    data={
                        'secret': self.reCaptcha_secret,
                        'response': form.data.get('g-recaptcha-response')})
                if recaptcha_response.status_code != 200 or not recaptcha_response.json()['success']:
                    return self.render_landing_page(request, None, *args, **kwargs)
            if form.is_valid():
                form_submission = self.process_form_submission(form)
                return self.render_landing_page(
                    request, form_submission, *args, **kwargs
                )
        else:
            form = self.get_form(page=self, user=request.user)
            form.fields["bird_pot"] = forms.CharField(required=False)
        context = self.get_context(request)
        context['form'] = form
        return render(request, self.get_template(request), context)


"""
class TiberiusBirdPageTag(TaggedItemBase):
    content_object = ParentalKey('TiberiusBirdPage', on_delete=models.CASCADE, related_name='tagged_items')


class TiberiusBirdPage(Page, BirdMixin):
    body = StreamField([
        ('paragraph', blocks.RichTextBlock(
            required=False, null=True,
            features=[
                'h2', 'h3', 'h4',
                'bold', 'italic',
                'superscript', 'subscript', 'strikethrough',
                'ol', 'ul', 'hr',
                'link', 'document-link',
                'blockquote', 'embed', 'image'])),
        ('image', ImageChooserBlock(required=False, null=True)),
        ('media', MediaFileBirdBlock(required=False, null=True)),
        ('html', HTMLBirdBlock(required=False, null=True)),
        ('code', BirdCodeBlock(required=False, null=True)),
    ], blank=True, null=True)

    tags = ClusterTaggableManager(through=TiberiusBirdPageTag, blank=True)
    
    search_fields = Page.search_fields + BirdMixin.search_fields + [
        index.SearchField('body'),
        index.SearchField('tags'),
        ]

    content_panels = Page.content_panels + BirdMixin.content_panels + [
        StreamFieldPanel('header'),
        StreamFieldPanel('body'),
        ]
    promote_panels = Page.promote_panels + [
        FieldPanel('tags'),
        ]
    settings_panels = Page.settings_panels + BirdMixin.settings_panels

    def get_sitemap_urls(self, request=None):
        if self.exclude_from_sitemap:
            return []
        else:
            return super(TiberiusBirdPage, self).get_sitemap_urls(request=request)
"""
