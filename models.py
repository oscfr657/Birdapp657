
from django.db import models
from django.shortcuts import render

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core import blocks
from wagtail.search.models import Query
from wagtail.search import index
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel

from .forms import SearchBirdForm
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

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        #index.FilterField('author'),
    ]

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
                'link', 'document-link',
                'blockquote', 'embed', 'image'])),
        ('image', ImageChooserBlock(required=False, null=True)),
        ('code', BirdCodeBlock(required=False, null=True)),
    ], blank=True, null=True)

    content_panels = BirdBasePage.content_panels + [
        StreamFieldPanel('body'),
    ]


class RawBirdPage(BirdBasePage):
    html = models.TextField(blank=True, null=True)
    
    content_panels = BirdBasePage.content_panels + [
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
