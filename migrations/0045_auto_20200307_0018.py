# Generated by Django 2.2 on 2020-03-06 23:18

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtailmedia.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('birdapp657', '0044_auto_20200302_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solobirdpage',
            name='header',
            field=wagtail.core.fields.StreamField([('header', wagtail.core.blocks.StructBlock([('muted', wagtail.core.blocks.BooleanBlock(default=True, help_text='Muted', required=False)), ('autoplay', wagtail.core.blocks.BooleanBlock(default=False, help_text='Autoplay', required=False)), ('loop', wagtail.core.blocks.BooleanBlock(default=False, help_text='Loop', required=False)), ('controls', wagtail.core.blocks.BooleanBlock(default=True, help_text='Controls', required=False)), ('block_media', wagtailmedia.blocks.AbstractMediaChooserBlock(null=True, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(null=True, required=False)), ('title', wagtail.core.blocks.CharBlock(null=True, required=False)), ('sub_title', wagtail.core.blocks.CharBlock(null=True, required=False)), ('font_color', wagtail.core.blocks.CharBlock(null=True, required=False)), ('bg_color', wagtail.core.blocks.CharBlock(null=True, required=False)), ('text', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'h5', 'bold', 'italic', 'link', 'document-link', 'ol', 'ul'], required=False))], null=True, required=False))], blank=True, null=True),
        ),
    ]
