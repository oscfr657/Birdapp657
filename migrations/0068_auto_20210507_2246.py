# Generated by Django 3.1.6 on 2021-05-07 20:46

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtailmedia.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('birdapp657', '0067_auto_20210219_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solobirdpage',
            name='body',
            field=wagtail.fields.StreamField(
                [
                    (
                        'paragraph',
                        wagtail.blocks.RichTextBlock(
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
                            null=True,
                            required=False,
                        ),
                    ),
                    (
                        'image',
                        wagtail.images.blocks.ImageChooserBlock(
                            null=True, required=False
                        ),
                    ),
                    (
                        'media',
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    'block_width',
                                    wagtail.blocks.CharBlock(
                                        help_text='Block width class', required=False
                                    ),
                                ),
                                (
                                    'muted',
                                    wagtail.blocks.BooleanBlock(
                                        default=True, help_text='Muted', required=False
                                    ),
                                ),
                                (
                                    'autoplay',
                                    wagtail.blocks.BooleanBlock(
                                        default=False,
                                        help_text='Autoplay',
                                        required=False,
                                    ),
                                ),
                                (
                                    'loop',
                                    wagtail.blocks.BooleanBlock(
                                        default=False, help_text='Loop', required=False
                                    ),
                                ),
                                (
                                    'controls',
                                    wagtail.blocks.BooleanBlock(
                                        default=True,
                                        help_text='Controls',
                                        required=False,
                                    ),
                                ),
                                (
                                    'block_media',
                                    wagtailmedia.blocks.AbstractMediaChooserBlock(),
                                ),
                            ],
                            null=True,
                            required=False,
                        ),
                    ),
                    (
                        'code',
                        wagtail.blocks.StructBlock(
                            [('code', wagtail.blocks.TextBlock(required=True))],
                            null=True,
                            required=False,
                        ),
                    ),
                    (
                        'html',
                        wagtail.blocks.StructBlock(
                            [('html', wagtail.blocks.RawHTMLBlock())],
                            null=True,
                            required=False,
                        ),
                    ),
                    (
                        'hero',
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    'block_class',
                                    wagtail.blocks.CharBlock(
                                        help_text='Block class',
                                        null=True,
                                        required=False,
                                    ),
                                ),
                                (
                                    'muted',
                                    wagtail.blocks.BooleanBlock(
                                        default=True, help_text='Muted', required=False
                                    ),
                                ),
                                (
                                    'autoplay',
                                    wagtail.blocks.BooleanBlock(
                                        default=False,
                                        help_text='Autoplay',
                                        required=False,
                                    ),
                                ),
                                (
                                    'loop',
                                    wagtail.blocks.BooleanBlock(
                                        default=False, help_text='Loop', required=False
                                    ),
                                ),
                                (
                                    'controls',
                                    wagtail.blocks.BooleanBlock(
                                        default=True,
                                        help_text='Controls',
                                        required=False,
                                    ),
                                ),
                                (
                                    'block_media',
                                    wagtailmedia.blocks.AbstractMediaChooserBlock(
                                        null=True, required=False
                                    ),
                                ),
                                (
                                    'image',
                                    wagtail.images.blocks.ImageChooserBlock(
                                        null=True, required=False
                                    ),
                                ),
                                (
                                    'full_screen',
                                    wagtail.blocks.BooleanBlock(
                                        default=False,
                                        help_text='Full screen',
                                        required=False,
                                    ),
                                ),
                                (
                                    'font_color',
                                    wagtail.blocks.CharBlock(
                                        null=True, required=False
                                    ),
                                ),
                                (
                                    'bg_color',
                                    wagtail.blocks.CharBlock(
                                        null=True, required=False
                                    ),
                                ),
                                (
                                    'text_align',
                                    wagtail.blocks.CharBlock(
                                        default='left', required=False
                                    ),
                                ),
                                (
                                    'text',
                                    wagtail.blocks.RichTextBlock(
                                        features=[
                                            'h1',
                                            'h2',
                                            'h3',
                                            'h4',
                                            'h5',
                                            'bold',
                                            'italic',
                                            'link',
                                            'document-link',
                                            'ol',
                                            'ul',
                                        ],
                                        required=False,
                                    ),
                                ),
                                (
                                    'button_link',
                                    wagtail.blocks.StructBlock(
                                        [
                                            (
                                                'font_color',
                                                wagtail.blocks.CharBlock(
                                                    null=True, required=False
                                                ),
                                            ),
                                            (
                                                'bg_color',
                                                wagtail.blocks.CharBlock(
                                                    null=True, required=False
                                                ),
                                            ),
                                            (
                                                'page_link',
                                                wagtail.blocks.PageChooserBlock(
                                                    help_text='Link to a page.',
                                                    required=False,
                                                ),
                                            ),
                                            (
                                                'external_link',
                                                wagtail.blocks.URLBlock(
                                                    help_text='Link to a URL.',
                                                    label='Link URL',
                                                    max_length=200,
                                                    required=False,
                                                ),
                                            ),
                                            (
                                                'text',
                                                wagtail.blocks.CharBlock(
                                                    help_text='Link text',
                                                    null=True,
                                                    required=False,
                                                ),
                                            ),
                                        ],
                                        null=True,
                                        required=False,
                                    ),
                                ),
                            ],
                            null=True,
                            required=False,
                        ),
                    ),
                    (
                        'hero_bt',
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    'block_class',
                                    wagtail.blocks.CharBlock(
                                        help_text='Block class',
                                        null=True,
                                        required=False,
                                    ),
                                ),
                                (
                                    'full_screen',
                                    wagtail.blocks.BooleanBlock(
                                        default=False,
                                        help_text='Full screen',
                                        required=False,
                                    ),
                                ),
                                (
                                    'font_color',
                                    wagtail.blocks.CharBlock(
                                        null=True, required=False
                                    ),
                                ),
                                (
                                    'bg_color',
                                    wagtail.blocks.CharBlock(
                                        null=True, required=False
                                    ),
                                ),
                                (
                                    'text_align',
                                    wagtail.blocks.CharBlock(
                                        default='left', required=False
                                    ),
                                ),
                                (
                                    'text',
                                    wagtail.blocks.RichTextBlock(
                                        features=[
                                            'h1',
                                            'h2',
                                            'h3',
                                            'h4',
                                            'bold',
                                            'italic',
                                            'link',
                                            'document-link',
                                        ],
                                        required=False,
                                    ),
                                ),
                                (
                                    'button_link',
                                    wagtail.blocks.StructBlock(
                                        [
                                            (
                                                'font_color',
                                                wagtail.blocks.CharBlock(
                                                    null=True, required=False
                                                ),
                                            ),
                                            (
                                                'bg_color',
                                                wagtail.blocks.CharBlock(
                                                    null=True, required=False
                                                ),
                                            ),
                                            (
                                                'page_link',
                                                wagtail.blocks.PageChooserBlock(
                                                    help_text='Link to a page.',
                                                    required=False,
                                                ),
                                            ),
                                            (
                                                'external_link',
                                                wagtail.blocks.URLBlock(
                                                    help_text='Link to a URL.',
                                                    label='Link URL',
                                                    max_length=200,
                                                    required=False,
                                                ),
                                            ),
                                            (
                                                'text',
                                                wagtail.blocks.CharBlock(
                                                    help_text='Link text',
                                                    null=True,
                                                    required=False,
                                                ),
                                            ),
                                        ],
                                        null=True,
                                        required=False,
                                    ),
                                ),
                            ],
                            null=True,
                            required=False,
                        ),
                    ),
                    (
                        'feed',
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    'block_class',
                                    wagtail.blocks.CharBlock(
                                        help_text='Block class', required=False
                                    ),
                                ),
                                (
                                    'children',
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ('c', 'Children'),
                                            ('d', 'Descendants'),
                                        ],
                                        icon='arrow-down',
                                    ),
                                ),
                                (
                                    'parent_page',
                                    wagtail.blocks.PageChooserBlock(
                                        label='parent page'
                                    ),
                                ),
                                (
                                    'exclude',
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.PageChooserBlock(
                                            label='Exclude page'
                                        ),
                                        default=[],
                                        required=False,
                                    ),
                                ),
                                (
                                    'tags',
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.CharBlock(label='Tag'),
                                        required=False,
                                    ),
                                ),
                                (
                                    'show_title',
                                    wagtail.blocks.BooleanBlock(
                                        default=True, required=False
                                    ),
                                ),
                                (
                                    'show_intro',
                                    wagtail.blocks.BooleanBlock(
                                        default=False, required=False
                                    ),
                                ),
                                (
                                    'show_content',
                                    wagtail.blocks.BooleanBlock(
                                        default=False, required=False
                                    ),
                                ),
                                (
                                    'show_meta',
                                    wagtail.blocks.BooleanBlock(
                                        default=False, required=False
                                    ),
                                ),
                                (
                                    'show_author',
                                    wagtail.blocks.BooleanBlock(
                                        default=False, required=False
                                    ),
                                ),
                                (
                                    'show_date',
                                    wagtail.blocks.BooleanBlock(
                                        default=False, required=False
                                    ),
                                ),
                                (
                                    'use_grid_template',
                                    wagtail.blocks.BooleanBlock(
                                        default=False, required=False
                                    ),
                                ),
                                (
                                    'bg_color',
                                    wagtail.blocks.CharBlock(
                                        default='white', label='Background color'
                                    ),
                                ),
                                (
                                    'text_color',
                                    wagtail.blocks.CharBlock(
                                        default='black', label='Text color'
                                    ),
                                ),
                                (
                                    'max_number',
                                    wagtail.blocks.IntegerBlock(required=False),
                                ),
                            ],
                            required=False,
                        ),
                    ),
                    (
                        'grid',
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    'block_class',
                                    wagtail.blocks.CharBlock(
                                        help_text='Block class', required=False
                                    ),
                                ),
                                (
                                    'children',
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ('c', 'Children'),
                                            ('d', 'Descendants'),
                                        ],
                                        icon='arrow-down',
                                    ),
                                ),
                                (
                                    'parent_page',
                                    wagtail.blocks.PageChooserBlock(
                                        label='parent page'
                                    ),
                                ),
                                (
                                    'exclude',
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.PageChooserBlock(
                                            label='Exclude page'
                                        ),
                                        default=[],
                                        required=False,
                                    ),
                                ),
                                (
                                    'tags',
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.CharBlock(label='Tag'),
                                        required=False,
                                    ),
                                ),
                                (
                                    'bg_color',
                                    wagtail.blocks.CharBlock(
                                        default='white', label='Background color'
                                    ),
                                ),
                                (
                                    'text_color',
                                    wagtail.blocks.CharBlock(
                                        default='black', label='Text color'
                                    ),
                                ),
                                (
                                    'max_number',
                                    wagtail.blocks.IntegerBlock(required=False),
                                ),
                            ],
                            required=False,
                        ),
                    ),
                    (
                        'simplegrid',
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    'block_class',
                                    wagtail.blocks.CharBlock(
                                        help_text='Block class', required=False
                                    ),
                                ),
                                (
                                    'children',
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ('c', 'Children'),
                                            ('d', 'Descendants'),
                                        ],
                                        icon='arrow-down',
                                    ),
                                ),
                                (
                                    'parent_page',
                                    wagtail.blocks.PageChooserBlock(
                                        label='parent page'
                                    ),
                                ),
                                (
                                    'exclude',
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.PageChooserBlock(
                                            label='Exclude page'
                                        ),
                                        default=[],
                                        required=False,
                                    ),
                                ),
                                (
                                    'tags',
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.CharBlock(label='Tag'),
                                        required=False,
                                    ),
                                ),
                                (
                                    'bg_color',
                                    wagtail.blocks.CharBlock(
                                        default='white', label='Background color'
                                    ),
                                ),
                                (
                                    'text_color',
                                    wagtail.blocks.CharBlock(
                                        default='black', label='Text color'
                                    ),
                                ),
                                (
                                    'max_number',
                                    wagtail.blocks.IntegerBlock(required=False),
                                ),
                            ],
                            required=False,
                        ),
                    ),
                    (
                        'racer',
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    'text',
                                    wagtail.blocks.RichTextBlock(
                                        features=[
                                            'h2',
                                            'h3',
                                            'h4',
                                            'h5',
                                            'bold',
                                            'italic',
                                            'link',
                                            'document-link',
                                            'ol',
                                            'ul',
                                        ],
                                        required=False,
                                    ),
                                ),
                                (
                                    'image',
                                    wagtail.images.blocks.ImageChooserBlock(
                                        required=False
                                    ),
                                ),
                                (
                                    'page_image_link',
                                    wagtail.blocks.PageChooserBlock(
                                        help_text='Link image to a page.',
                                        required=False,
                                    ),
                                ),
                                (
                                    'external_image_link',
                                    wagtail.blocks.URLBlock(
                                        help_text='Link image to a URL.',
                                        label='Link URL',
                                        max_length=200,
                                        required=False,
                                    ),
                                ),
                                (
                                    'right',
                                    wagtail.blocks.BooleanBlock(
                                        help_text='Image to the right else left',
                                        required=False,
                                    ),
                                ),
                                (
                                    'bg_color',
                                    wagtail.blocks.CharBlock(
                                        default='#fff', label='Background color'
                                    ),
                                ),
                                (
                                    'text_color',
                                    wagtail.blocks.CharBlock(
                                        default='#000', label='Text color'
                                    ),
                                ),
                                (
                                    'block_class',
                                    wagtail.blocks.CharBlock(
                                        help_text='Block class', required=False
                                    ),
                                ),
                            ],
                            null=True,
                            required=False,
                        ),
                    ),
                    (
                        'simpleracer',
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    'text',
                                    wagtail.blocks.RichTextBlock(
                                        features=[
                                            'h2',
                                            'h3',
                                            'h4',
                                            'h5',
                                            'bold',
                                            'italic',
                                            'link',
                                            'document-link',
                                            'ol',
                                            'ul',
                                        ],
                                        required=False,
                                    ),
                                ),
                                (
                                    'image',
                                    wagtail.images.blocks.ImageChooserBlock(
                                        required=False
                                    ),
                                ),
                                (
                                    'page_image_link',
                                    wagtail.blocks.PageChooserBlock(
                                        help_text='Link image to a page.',
                                        required=False,
                                    ),
                                ),
                                (
                                    'external_image_link',
                                    wagtail.blocks.URLBlock(
                                        help_text='Link image to a URL.',
                                        label='Link URL',
                                        max_length=200,
                                        required=False,
                                    ),
                                ),
                                (
                                    'right',
                                    wagtail.blocks.BooleanBlock(
                                        help_text='Image to the right else left',
                                        required=False,
                                    ),
                                ),
                                (
                                    'bg_color',
                                    wagtail.blocks.CharBlock(
                                        default='#fff', label='Background color'
                                    ),
                                ),
                                (
                                    'text_color',
                                    wagtail.blocks.CharBlock(
                                        default='#000', label='Text color'
                                    ),
                                ),
                                (
                                    'block_class',
                                    wagtail.blocks.CharBlock(
                                        help_text='Block class', required=False
                                    ),
                                ),
                            ],
                            null=True,
                            required=False,
                        ),
                    ),
                ],
                blank=True,
                null=True,
            ),
        ),
    ]
