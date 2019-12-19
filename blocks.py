# -*- coding: utf-8 -*-

from django.utils.html import format_html

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

from wagtailmedia.blocks import AbstractMediaChooserBlock


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
    right = blocks.BooleanBlock(
        required=False,
        help_text='Image to the right else left')
    bg_color = blocks.CharBlock(
        default='#fff',
        label='Background color')
    text_color = blocks.CharBlock(
        default='#000',
        label='Text color')
    #block_width = blocks.CharBlock(required=False, help_text='Block width class')

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
    block_width = blocks.CharBlock(required=False, help_text='Block width class')
    children = blocks.ChoiceBlock(choices=[
            ('c', 'Children'),
            ('d', 'Descendants'),
        ],
        icon='arrow-down',
        required=True
        )
    parent_page = blocks.PageChooserBlock(label='parent page')
    show_title = blocks.BooleanBlock(required=False, default=True)
    show_intro = blocks.BooleanBlock(required=False, default=False)
    show_content = blocks.BooleanBlock(required=False, default=False)
    show_meta = blocks.BooleanBlock(required=False, default=False)
    show_author = blocks.BooleanBlock(required=False, default=False)
    show_date = blocks.BooleanBlock(required=False, default=False)
    number = blocks.IntegerBlock(required=False)

    def get_context(self, value):
        context = super(FeedBirdBlock, self).get_context(value)
        if value['children'] == 'c':
            feed_posts = value[
                'parent_page'].get_children().live().public().not_in_menu().order_by(
                    '-go_live_at')
        elif value['children'] == 'd':
            feed_posts = value[
                'parent_page'].get_descendants().live().public().not_in_menu().order_by(
                    '-go_live_at')
        number = value['number']
        if number:
            feed_posts = feed_posts[:number]
        context['feed_posts'] = feed_posts
        return context
    
    class Meta:
        label = 'FeedBlock'
        icon = 'list-ul'
        template = 'blocks/feed_bird_block.html'

class PageGridBirdBlock(blocks.StructBlock):
    block_width = blocks.CharBlock(required=False, help_text='Block width class')
    children = blocks.ChoiceBlock(choices=[
            ('c', 'Children'),
            ('d', 'Descendants'),
        ],
        icon='arrow-down',
        required=True
        )
    parent_page = blocks.PageChooserBlock(label='parent page')
    show_title = blocks.BooleanBlock(required=False, default=True)
    show_intro = blocks.BooleanBlock(required=False, default=False)
    show_content = blocks.BooleanBlock(required=False, default=False)
    show_meta = blocks.BooleanBlock(required=False, default=False)
    show_author = blocks.BooleanBlock(required=False, default=False)
    show_date = blocks.BooleanBlock(required=False, default=False)
    number = blocks.IntegerBlock(required=False)

    def get_context(self, value):
        context = super(PageGridBirdBlock, self).get_context(value)
        if value['children'] == 'c':
            grid_posts = value[
                'parent_page'].get_children().live().public().not_in_menu().order_by(
                    '-go_live_at')
        elif value['children'] == 'd':
            grid_posts = value[
                'parent_page'].get_descendants().live().public().not_in_menu().order_by(
                    '-go_live_at')
        number = value['number']
        if number:
            grid_posts = grid_posts[:number]
        context['grid_posts'] = grid_posts
        return context
    
    class Meta:
        label = 'GridBlock'
        icon = 'grip'
        template = 'blocks/page_grid_bird_block.html'
