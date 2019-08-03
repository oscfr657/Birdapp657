
from wagtail.core import blocks

class BirdCodeBlock(blocks.StructBlock):

    code = blocks.TextBlock(required=True)

    class Meta:
        label = 'Code'
        icon = 'code'
        template = 'blocks/code.html'