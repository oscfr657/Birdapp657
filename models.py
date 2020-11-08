# -*- coding: utf-8 -*-

from django.db import models
from django.shortcuts import render
from django import forms

from wagtail.core.models import (
    Page, Orderable
    )
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core import blocks

from wagtail.search.models import Query
from wagtail.search import index

from wagtail.admin.edit_handlers import (
    FieldPanel, StreamFieldPanel, InlinePanel,
    PageChooserPanel )

from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.documents.models import Document
from wagtail.documents.edit_handlers import DocumentChooserPanel

from wagtail.contrib.forms.models import AbstractForm, AbstractFormField
from wagtail.contrib.forms.edit_handlers import FormSubmissionsPanel

from wagtail.contrib.settings.models import BaseSetting, register_setting

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from modelcluster.contrib.taggit import ClusterTaggableManager

from taggit.models import TaggedItemBase

from .forms import SearchBirdForm
from .blocks import (HeroBirdBlock, BirdCodeBlock,
    HTMLBirdBlock, MediaFileBirdBlock,
    FeedBirdBlock,
    RacerBirdBlock,
    GridBirdBlock, SimpleGridBirdBlock)


class FontFace(Orderable):
    brand = ParentalKey(
        'BrandingSettings',
        related_name='brand_fonts',
        on_delete=models.CASCADE
    )
    src_file = models.ForeignKey(
        'wagtaildocs.Document',
        on_delete=models.CASCADE,
        related_name='+'
    )
    font_family = models.CharField(max_length=50)
    font_format =  models.CharField(max_length=50)
    panels = [
        DocumentChooserPanel('src_file'),
        FieldPanel('font_family'),
        FieldPanel('font_format'),
    ]


@register_setting
class BrandingSettings(BaseSetting, ClusterableModel):
    icon = models.ForeignKey(
        'wagtailimages.Image',
        blank=True, null=True,
        on_delete=models.SET_NULL,
        related_name='+'
        )
    logo = models.ForeignKey(
        'wagtailimages.Image',
        blank=True, null=True,
        on_delete=models.SET_NULL,
        related_name='+'
        )
    show_name = models.BooleanField(default=True)
    mobile_menu_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    lang_code = models.CharField(max_length=5, blank=True, null=True)
    extra_head = models.TextField(blank=True, null=True)
    extra_css = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    extra_js = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    footer = StreamField([
        ('paragraph', blocks.RichTextBlock(
            required=False, null=True,
            features=[
                'h2', 'h3', 'h4',
                'bold', 'italic',
                'superscript', 'subscript', 'strikethrough',
                'ol', 'ul', 'hr',
                'link', 'document-link',
                'blockquote',])),
        ('html', HTMLBirdBlock(required=False, null=True)),
    ], blank=True, null=True)

    panels = [
        ImageChooserPanel('icon'),
        ImageChooserPanel('logo'),
        FieldPanel('show_name'),
        PageChooserPanel('mobile_menu_page'),
        FieldPanel('lang_code'),
        FieldPanel('extra_head'),
        DocumentChooserPanel('extra_css'),
        DocumentChooserPanel('extra_js'),
        InlinePanel('brand_fonts', label="Brand fontfaces"),
        StreamFieldPanel('footer'),
    ]


class BirdMixin(models.Model):
    author = models.CharField(max_length=255, blank=True, null=True)
    image = models.ForeignKey(
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
            'superscript', 'subscript', 'strikethrough',
            'ol', 'ul', 'hr',
            'link', 'document-link', 'blockquote']
            )
    menu_icon = models.ForeignKey(
        'wagtailimages.Image',
        blank=True, null=True,
        on_delete=models.SET_NULL,
        related_name='+'
        )
    hover_menu_icon = models.ForeignKey(
        'wagtailimages.Image',
        blank=True, null=True,
        on_delete=models.SET_NULL,
        related_name='+'
        )
    content_width = models.CharField(max_length=50, blank=True, null=True)
    show_menu = models.BooleanField(default=True)
    hover_over_menu = models.BooleanField(default=False)
    show_breadcrumbs = models.BooleanField(default=False)
    transparent_header = models.BooleanField(default=False)
    show_coverImage = models.BooleanField(default=False)
    show_title = models.BooleanField(default=True)
    show_meta = models.BooleanField(default=False)
    show_author = models.BooleanField(default=False)
    show_date = models.BooleanField(default=False)
    exclude_from_sitemap = models.BooleanField(default=False)

    class Meta:
        abstract = True

    search_fields = [
        index.SearchField('intro'),
        #index.FilterField('author'),
    ]
    content_panels = [
        FieldPanel('author'),
        ImageChooserPanel('image'),
        FieldPanel('intro', classname="full"),
    ]
    settings_panels = [
        FieldPanel('content_width'),
        FieldPanel('show_menu'),
        ImageChooserPanel('menu_icon'),
        ImageChooserPanel('hover_menu_icon'),
        FieldPanel('hover_over_menu'),
        FieldPanel('show_breadcrumbs'),
        FieldPanel('transparent_header'),
        FieldPanel('show_coverImage'),
        FieldPanel('show_title'),
        FieldPanel('show_meta'),
        FieldPanel('show_author'),
        FieldPanel('show_date'),
        FieldPanel('exclude_from_sitemap'),
    ]


class SoloBirdPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'SoloBirdPage',
        on_delete=models.CASCADE,
        related_name='tagged_items')


class SoloBirdPage(Page, BirdMixin):
    top_hero = StreamField([
        ('hero', HeroBirdBlock(required=False, null=True)),
    ], blank=True, null=True)
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
        ('code', BirdCodeBlock(required=False, null=True)),
        ('html', HTMLBirdBlock(required=False, null=True)),
        ('feed', FeedBirdBlock(required=False)),
        ('grid', GridBirdBlock(required=False)),
        ('simplegrid', SimpleGridBirdBlock(required=False)),
        ('racer', RacerBirdBlock(required=False, null=True)),
    ], blank=True, null=True)

    tags = ClusterTaggableManager(through=SoloBirdPageTag, blank=True)
    
    search_fields = Page.search_fields + BirdMixin.search_fields + [
        index.SearchField('body'),
        index.SearchField('tags'),
        ]

    content_panels = Page.content_panels + BirdMixin.content_panels + [
        StreamFieldPanel('top_hero'),
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
            return super(SoloBirdPage, self).get_sitemap_urls(request=request)


class SearchBirdPage(Page, BirdMixin):
    
    top_hero = StreamField([
        ('hero', HeroBirdBlock(required=False, null=True)),
    ], blank=True, null=True)

    content_panels = Page.content_panels + BirdMixin.content_panels + [
        StreamFieldPanel('top_hero'),
        ]
    settings_panels = Page.settings_panels + BirdMixin.settings_panels

    def serve(self, request):
        search_query = ''
        if request.method == 'POST':
            form = SearchBirdForm(request.POST)
            if form.is_valid():
                search_query = form.cleaned_data['search_query']
                search_results = self.get_parent().get_descendants().live(
                    ).public().exclude(
                        show_in_menus=True).order_by(
                            '-first_published_at').search(
                                search_query, order_by_relevance=False)

                Query.get(search_query).add_hit()

                form = SearchBirdForm()
            else:
                search_results = Page.objects.none()
        else:
            form = SearchBirdForm()
            search_results = Page.objects.none()

        return render(request, 'birdapp657/search_bird_page.html', {
            'page': self,
            'form': form,
            'search_query': search_query,
            'search_results': search_results,
        })
    
    def get_sitemap_urls(self, request=None):
        if self.exclude_from_sitemap:
            return []
        else:
            return super(SearchBirdPage, self).get_sitemap_urls(request=request)


class FormField(AbstractFormField):
    page = ParentalKey(
        'FormBirdPage',
        on_delete=models.CASCADE,
        related_name='form_fields')
        

class FormBirdPage(AbstractForm, BirdMixin):

    top_hero = StreamField([
        ('hero', HeroBirdBlock(required=False, null=True)),
    ], blank=True, null=True)

    thank_you_text = RichTextField(
        blank=True, null=True,
        features=[
            'h2', 'h3', 'h4',
            'bold', 'italic',
            'superscript', 'subscript', 'strikethrough',
            'ol', 'ul', 'hr',
            'link', 'document-link',
            'blockquote', 'embed', 'image']
            )
    #show_result = models.BooleanField(default=False)

    content_panels = AbstractForm.content_panels + BirdMixin.content_panels + [
            StreamFieldPanel('top_hero'),
    #        FieldPanel('show_result'),
            InlinePanel('form_fields', label="Form fields"),
            FieldPanel('thank_you_text', classname="full"),
            FormSubmissionsPanel(),
        ]
    settings_panels = Page.settings_panels + BirdMixin.settings_panels

    def get_sitemap_urls(self, request=None):
        if self.exclude_from_sitemap:
            return []
        else:
            return super(FormBirdPage, self).get_sitemap_urls(request=request)

    def serve(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = self.get_form(request.POST, request.FILES, page=self, user=request.user)
            if form.data.get('bird_pot'):
                return self.render_landing_page(request, None, *args, **kwargs)
            if form.is_valid():
                form_submission = self.process_form_submission(form)
                return self.render_landing_page(request, form_submission, *args, **kwargs)
        else:
            form = self.get_form(page=self, user=request.user)
            form.fields["bird_pot"] = forms.CharField(
                # initial='bird' % time.now().format(),  # Time of creation and check time at submission ?
                # empty_value='bird',  # Time of creation and check time at submission ?
                # validators=[validate_honey_pot, forms.CharField.default_validators],  # Does not work. :/
                required=False)
        context = self.get_context(request)
        context['form'] = form
        return render(
            request,
            self.get_template(request),
            context
            )


"""
class TiberiusBirdPageTag(TaggedItemBase):
    content_object = ParentalKey('TiberiusBirdPage', on_delete=models.CASCADE, related_name='tagged_items')


class TiberiusBirdPage(Page, BirdMixin):
    header = StreamField([
        ('header', HeaderBirdBlock(required=False, null=True)),
    ], blank=True, null=True)
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
        ('racer', RacerBirdBlock(required=False, null=True)),
        ('feed', FeedBirdBlock(required=False)),
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