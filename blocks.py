# -*- coding: utf-8 -*-

from django.core.exceptions import FieldError
from django.utils.html import format_html

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

from wagtailmedia.blocks import AbstractMediaChooserBlock



class LinkBirdBlock(blocks.StructBlock):
    font_color = blocks.CharBlock(required=False, null=True)
    bg_color = blocks.CharBlock(required=False, null=True)
    page_link = blocks.PageChooserBlock(
        required=False,
        help_text='Link to a page.'
    )
    external_link = blocks.URLBlock(
        label='Link URL',
        max_length=200,
        required=False,
        help_text='Link to a URL.'
    )
    text = blocks.CharBlock(required=False, null=True, help_text='Link text')

    class Meta:
        label = 'Link'
        template = 'blocks/link.html'


class HeaderBirdBlock(blocks.StructBlock):
    block_class = blocks.CharBlock(required=False, null=True, help_text='Block class')

    muted = blocks.BooleanBlock(required=False, default=True, help_text='Muted')
    autoplay = blocks.BooleanBlock(required=False, default=False, help_text='Autoplay')
    loop = blocks.BooleanBlock(required=False, default=False, help_text='Loop')
    controls = blocks.BooleanBlock(required=False, default=True, help_text='Controls')
    block_media = AbstractMediaChooserBlock(required=False, null=True)
    
    image = ImageChooserBlock(required=False, null=True)
    
    font_color = blocks.CharBlock(required=False, null=True)
    bg_color = blocks.CharBlock(required=False, null=True)
    text_align = blocks.CharBlock(required=False, default='left')
    text = blocks.RichTextBlock(
        required=False,
        features=[
            'h2', 'h3', 'h4', 'h5',
            'bold', 'italic',
            'link', 'document-link',
            'ol', 'ul'])
    
    button_link = LinkBirdBlock(required=False, null=True)

    class Meta:
        label = 'Header'
        icon = 'image'
        template = 'blocks/header.html'


class BirdCodeBlock(blocks.StructBlock):  # TODO: Rename to CodeBirdBlock ?

    code = blocks.TextBlock(required=True)

    class Meta:
        label = 'Code'
        icon = 'code'
        template = 'blocks/code.html'


class RacerBirdBlock(blocks.StructBlock):
    text = blocks.RichTextBlock(
        required=False,
        features=[
            'h2', 'h3', 'h4', 'h5',
            'bold', 'italic',
            'link', 'document-link',
            'ol', 'ul'])
    image = ImageChooserBlock(required=False)
    page_image_link = blocks.PageChooserBlock(
        required=False,
        help_text='Link image to a page.'
    )
    external_image_link = blocks.URLBlock(
        label='Link URL',
        max_length=200,
        required=False,
        help_text='Link image to a URL.'
    )
    right = blocks.BooleanBlock(
        required=False,
        help_text='Image to the right else left')
    bg_color = blocks.CharBlock(
        default='#fff',
        label='Background color')
    text_color = blocks.CharBlock(
        default='#000',
        label='Text color')
    block_class = blocks.CharBlock(required=False, help_text='Block class')

    class Meta:
        label = 'Racer'
        icon = 'image'
        template = 'blocks/racer.html'


class HTMLBirdBlock(blocks.StructBlock):

    html = blocks.RawHTMLBlock()

    class Meta:
        label = 'HTML'
        icon = 'code'
        template = 'blocks/html_bird_block.html'


class MediaFileBirdBlock(blocks.StructBlock):
    block_width = blocks.CharBlock(required=False, help_text='Block width class')
    muted = blocks.BooleanBlock(required=False, default=True, help_text='Muted')
    autoplay = blocks.BooleanBlock(required=False, default=False, help_text='Autoplay')
    loop = blocks.BooleanBlock(required=False, default=False, help_text='Loop')
    controls = blocks.BooleanBlock(required=False, default=True, help_text='Controls')
    block_media = AbstractMediaChooserBlock()

    class Meta:
        label = 'MediaFile'
        icon = 'media'
        template = 'blocks/media_file_bird_block.html'


class FeedBirdBlock(blocks.StructBlock):
    block_class = blocks.CharBlock(required=False, help_text='Block class')
    children = blocks.ChoiceBlock(choices=[
            ('c', 'Children'),
            ('d', 'Descendants'),
        ],
        icon='arrow-down',
        required=True
        )
    parent_page = blocks.PageChooserBlock(label='parent page')
    #exclude = blocks.ListBlock(blocks.PageChooserBlock(label="Exclude page"), required=False)
    tags = blocks.ListBlock(blocks.CharBlock(label="Tag"), required=False)
    show_title = blocks.BooleanBlock(required=False, default=True)
    show_intro = blocks.BooleanBlock(required=False, default=False)
    show_content = blocks.BooleanBlock(required=False, default=False)
    show_meta = blocks.BooleanBlock(required=False, default=False)
    show_author = blocks.BooleanBlock(required=False, default=False)
    show_date = blocks.BooleanBlock(required=False, default=False)
    use_grid_template = blocks.BooleanBlock(required=False, default=False)
    bg_color = blocks.CharBlock(
        default='white',
        label='Background color')
    text_color = blocks.CharBlock(
        default='black',
        label='Text color')
    max_number = blocks.IntegerBlock(required=False)

    def get_context(self, value):
        context = super(FeedBirdBlock, self).get_context(value)
        if value['children'] == 'c':
            feed_posts = value[
                'parent_page'].get_children().live().public().not_in_menu().order_by(
                    '-go_live_at').distinct()
        elif value['children'] == 'd':
            feed_posts = value[
                'parent_page'].get_descendants().live().public().not_in_menu().order_by(
                    '-go_live_at').distinct()
        tags = value['tags']
        posts = []
        for post in feed_posts.specific():
            try:
                if tags:
                    if set(post.tags.all().values_list('name', flat=True)).intersection(set(tags)):
                        post = post
                    else:
                        continue
                if post.coverImage:
                    posts.append(post)
            except (FieldError, AttributeError):
                pass
        feed_posts = posts
        max_number = value['max_number']
        if max_number:
            feed_posts = feed_posts[:max_number]
        context['feed_posts'] = feed_posts
        return context

    class Meta:
        label = 'FeedBlock'
        icon = 'list-ul'
        template = 'blocks/feed_bird_block.html'

