# Generated by Django 2.2.1 on 2019-10-23 19:21

import birdapp657.blocks
from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtailmedia.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('birdapp657', '0026_auto_20191013_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solobirdpage',
            name='body',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'superscript', 'subscript', 'strikethroughol', 'ul', 'hr', 'link', 'document-link', 'blockquote', 'embed', 'image'], null=True, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(null=True, required=False)), ('media', birdapp657.blocks.MediaFileBirdBlock(null=True, required=False)), ('extended_media', wagtail.core.blocks.StructBlock([('muted', wagtail.core.blocks.BooleanBlock(default=True, help_text='Muted', required=False)), ('autoplay', wagtail.core.blocks.BooleanBlock(default=False, help_text='Autoplay', required=False)), ('loop', wagtail.core.blocks.BooleanBlock(default=False, help_text='Loop', required=False)), ('controls', wagtail.core.blocks.BooleanBlock(default=True, help_text='Controls', required=False)), ('block_media', wagtailmedia.blocks.AbstractMediaChooserBlock())], null=True, required=False)), ('code', wagtail.core.blocks.StructBlock([('code', wagtail.core.blocks.TextBlock(required=True))], null=True, required=False)), ('racer', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'h5', 'bold', 'italic', 'link', 'document-link', 'ol', 'ul'], required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('right', wagtail.core.blocks.BooleanBlock(help_text='Image to the right else left', required=False)), ('bg_color', wagtail.core.blocks.CharBlock(default='#fff', label='Background color')), ('text_color', wagtail.core.blocks.CharBlock(default='#000', label='Text color'))], null=True, required=False)), ('html', wagtail.core.blocks.StructBlock([('html', wagtail.core.blocks.RawHTMLBlock())], null=True, required=False)), ('feed', wagtail.core.blocks.StructBlock([('children', wagtail.core.blocks.ChoiceBlock(choices=[('c', 'Children'), ('d', 'Descendants')], icon='arrow-down')), ('parent_page', wagtail.core.blocks.PageChooserBlock(label='parent page'))], required=False))], blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='CollectionBirdPage',
        ),
    ]