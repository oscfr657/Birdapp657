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


class MediaFileBirdBlock(AbstractMediaChooserBlock):
    # TODO: Implement muted autoplay loop controls ?
    #muted = blocks.BooleanBlock(default=True, help_text='Muted')
    #autoplay = blocks.BooleanBlock(default=False, help_text='Autoplay')
    #loop = blocks.BooleanBlock(default=False, help_text='Loop')
    #controls = blocks.BooleanBlock(default=True, help_text='Controls')

    class Meta:
        label = 'MediaFile'
        icon = 'media'
        #template = 'blocks/media_file_bird_block.html'

    def render_basic(self, value, context=None):
        #TODO: But what about webm and ogg ? sad_face
        if not value:
            return ''
        if value.type == 'video':
            player_code = '''
            <div>
                <video muted autoplay controls >
                    <source src="{0}" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
            </div>
            '''
        else:
            player_code = '''
            <div>
                <audio controls>
                    <source src="{0}" type="audio/mpeg">
                    Your browser does not support the audio element.
                </audio>
            </div>
            '''
        return format_html(player_code, value.file.url)
