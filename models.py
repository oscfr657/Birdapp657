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

from .forms import SearchBirdForm
from .blocks import BirdCodeBlock, RacerBirdBlock


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
            'superscript', 'subscript', 'strikethrough'
            'ol', 'ul', 'hr',
            'link', 'document-link', 'blockquote']
            )

    class Meta:
        abstract = True

    search_fields = [
        index.SearchField('intro'),
        #index.FilterField('author'),
    ]

    content_panels = [
        FieldPanel('author'),
        ImageChooserPanel('coverImage'),
        FieldPanel('intro', classname="full")
    ]


class BirdBasePage(Page, BirdMixin):  # TODO: Remove to CollectionBirdPage ?
    search_fields = Page.search_fields + BirdMixin.search_fields

    content_panels = Page.content_panels + BirdMixin.content_panels

    def get_context(self, request):
        context = super().get_context(request)
        try:
            section_root_page = Page.objects.ancestor_of(self)[2]
        except IndexError:
            section_root_page = self
        context['section_root_page'] = section_root_page
        return context


class CollectionBirdPage(Page, BirdMixin):
    search_fields = Page.search_fields + BirdMixin.search_fields

    content_panels = Page.content_panels + BirdMixin.content_panels

    def get_context(self, request):
        context = super().get_context(request)
        try:
            section_root_page = Page.objects.ancestor_of(self)[2]
        except IndexError:
            section_root_page = self
        context['section_root_page'] = section_root_page
        return context


class SoloBirdPage(Page, BirdMixin):
    body = StreamField([
        # ? ('heading', blocks.CharBlock(classname="full title",required=False,null=True)),
        ('paragraph', blocks.RichTextBlock(
            required=False, null=True,
            features=[
                'h2', 'h3', 'h4',
                'bold', 'italic',
                'superscript', 'subscript', 'strikethrough'
                'ol', 'ul', 'hr',
                'link', 'document-link',
                'blockquote', 'embed', 'image'])),
        ('image', ImageChooserBlock(required=False, null=True)),
        ('code', BirdCodeBlock(required=False, null=True)),
        ('racer', RacerBirdBlock(required=False, null=True)),
    ], blank=True, null=True)

    search_fields = Page.search_fields + BirdMixin.search_fields + [
        index.SearchField('body'),
        #index.FilterField('author'),
    ]
    content_panels = Page.content_panels + BirdMixin.content_panels +[
        StreamFieldPanel('body'),
    ]


class BirdPage(BirdBasePage):  # Remove
    body = StreamField([
        # ? ('heading', blocks.CharBlock(classname="full title",required=False,null=True)),
        ('paragraph', blocks.RichTextBlock(
            required=False, null=True,
            features=[
                'h2', 'h3', 'h4',
                'bold', 'italic',
                'superscript', 'subscript', 'strikethrough'
                'ol', 'ul', 'hr',
                'link', 'document-link',
                'blockquote', 'embed', 'image'])),
        ('image', ImageChooserBlock(required=False, null=True)),
        ('code', BirdCodeBlock(required=False, null=True)),
        ('racer', RacerBirdBlock(required=False, null=True)),
    ], blank=True, null=True)

    search_fields = Page.search_fields + BirdMixin.search_fields + [
        index.SearchField('body'),
        #index.FilterField('author'),
    ]
    content_panels = Page.content_panels + BirdMixin.content_panels +[
        StreamFieldPanel('body'),
    ]


class RawBirdPage(BirdBasePage):  # Remove
    html = models.TextField(blank=True, null=True)
    
    content_panels = Page.content_panels + BirdMixin.content_panels + [
        FieldPanel('html', classname="full"),
    ]


class HTMLBirdPage(Page, BirdMixin):
    html = models.TextField(blank=True, null=True)
    
    content_panels = Page.content_panels + BirdMixin.content_panels + [
        FieldPanel('html', classname="full"),
    ]


class SearchBirdPage(Page):
    
    def serve(self, request):
        if request.method == 'POST':
            form = SearchBirdForm(request.POST)
            if form.is_valid():
                search_query = form.cleaned_data['search_query']
                search_results = self.get_parent().get_descendants().live().search(search_query)

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
            'superscript', 'subscript', 'strikethrough'
            'ol', 'ul', 'hr',
            'link', 'document-link',
            'blockquote', 'embed', 'image']
            )

    content_panels = BirdMixin.content_panels + AbstractForm.content_panels + [
            FormSubmissionsPanel(),
            InlinePanel('form_fields', label="Form fields"),
            FieldPanel('thank_you_text', classname="full"),
        ]

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
