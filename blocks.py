
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

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
        icon = 'picture'
        template = 'blocks/racer.html'
