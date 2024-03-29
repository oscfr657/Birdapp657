# Generated by Django 2.2.9 on 2019-12-25 19:39

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtailmedia.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('birdapp657', '0039_auto_20191218_0130'),
    ]

    operations = [
        migrations.AddField(
            model_name='solobirdpage',
            name='header',
            field=wagtail.fields.StreamField(
                [
                    (
                        'header',
                        wagtail.blocks.StructBlock(
                            [
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
                                    'title',
                                    wagtail.blocks.CharBlock(
                                        null=True, required=False
                                    ),
                                ),
                                (
                                    'sub_title',
                                    wagtail.blocks.CharBlock(
                                        null=True, required=False
                                    ),
                                ),
                                (
                                    'font_color',
                                    wagtail.blocks.CharBlock(
                                        null=True, required=False
                                    ),
                                ),
                            ],
                            null=True,
                            required=False,
                        ),
                    )
                ],
                blank=True,
                null=True,
            ),
        ),
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
                            ],
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
                        'feed',
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    'block_width',
                                    wagtail.blocks.CharBlock(
                                        help_text='Block width class', required=False
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
                                    'number',
                                    wagtail.blocks.IntegerBlock(required=False),
                                ),
                            ],
                            required=False,
                        ),
                    ),
                    (
                        'page_grid',
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    'block_width',
                                    wagtail.blocks.CharBlock(
                                        help_text='Block width class', required=False
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
                                    'number',
                                    wagtail.blocks.IntegerBlock(required=False),
                                ),
                            ],
                            required=False,
                        ),
                    ),
                ],
                blank=True,
                null=True,
            ),
        ),
    ]
