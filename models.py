# -*- coding: utf-8 -*-

from django.db import models
from django.shortcuts import render
from django import forms

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core import blocks
from wagtail.search.models import Query
from wagtail.search import index
from wagtail.admin.edit_handlers import (
    FieldPanel, StreamFieldPanel, InlinePanel )
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.contrib.forms.models import AbstractForm, AbstractFormField
from wagtail.contrib.forms.edit_handlers import FormSubmissionsPanel

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from .forms import SearchBirdForm
from .blocks import (BirdCodeBlock, RacerBirdBlock,
    HTMLBirdBlock, MediaFileBirdBlock, FeedBirdBlock)
from wagtail.contrib.settings.models import BaseSetting, register_setting


@register_setting
class BrandingSettings(BaseSetting):
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
        StreamFieldPanel('footer'),
    ]


class BirdMixin(models.Model):
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
    content_with = models.CharField(max_length=50, blank=True, null=True)
    show_menu = models.BooleanField(default=True)
    hover_over_menu = models.BooleanField(default=False)
    show_breadcrumbs = models.BooleanField(default=False)
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
        ImageChooserPanel('coverImage'),
        FieldPanel('intro', classname="full"),
    ]
    settings_panels = [
        FieldPanel('content_with'),
        FieldPanel('show_menu'),
        ImageChooserPanel('menu_icon'),
        ImageChooserPanel('hover_menu_icon'),
        FieldPanel('hover_over_menu'),
        FieldPanel('show_breadcrumbs'),
        FieldPanel('show_coverImage'),
        FieldPanel('show_title'),
        FieldPanel('show_meta'),
        FieldPanel('show_author'),
        FieldPanel('show_date'),
        FieldPanel('exclude_from_sitemap'),
    ]


class SoloBirdPageTag(TaggedItemBase):
    content_object = ParentalKey('SoloBirdPage', on_delete=models.CASCADE, related_name='tagged_items')


class SoloBirdPage(Page, BirdMixin):
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
        ('racer', RacerBirdBlock(required=False, null=True)),
        ('html', HTMLBirdBlock(required=False, null=True)),
        ('feed', FeedBirdBlock(required=False)),
    ], blank=True, null=True)

    tags = ClusterTaggableManager(through=SoloBirdPageTag, blank=True)
    
    search_fields = Page.search_fields + BirdMixin.search_fields + [
        index.SearchField('body'),
        ]

    content_panels = Page.content_panels + BirdMixin.content_panels + [
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
    
    content_panels = Page.content_panels + BirdMixin.content_panels
    settings_panels = Page.settings_panels + BirdMixin.settings_panels

    def serve(self, request):
        if request.method == 'POST':
            form = SearchBirdForm(request.POST)
            if form.is_valid():
                search_query = form.cleaned_data['search_query']
                search_results = self.get_parent().get_descendants().live().public().search(search_query)

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

    content_panels = BirdMixin.content_panels + AbstractForm.content_panels + [
            FormSubmissionsPanel(),
            InlinePanel('form_fields', label="Form fields"),
            FieldPanel('thank_you_text', classname="full"),
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
            if form.data["bird_pot"]:
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
