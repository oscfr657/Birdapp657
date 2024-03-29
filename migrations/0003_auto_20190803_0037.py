# Generated by Django 2.2.1 on 2019-08-02 22:37

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('birdapp657', '0002_auto_20190721_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='birdpage',
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
                                'strikethroughol',
                                'ul',
                                'hr',
                                'link',
                                'document-link',
                                'blockquote',
                                'code',
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
                ],
                blank=True,
                null=True,
            ),
        ),
    ]
