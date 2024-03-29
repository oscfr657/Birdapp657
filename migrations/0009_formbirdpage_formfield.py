# Generated by Django 2.2.1 on 2019-08-22 20:39

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('wagtailimages', '0001_squashed_0021'),
        ('birdapp657', '0008_auto_20190816_2311'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormBirdPage',
            fields=[
                (
                    'page_ptr',
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to='wagtailcore.Page',
                    ),
                ),
                ('author', models.CharField(blank=True, max_length=255, null=True)),
                ('intro', wagtail.fields.RichTextField(blank=True, null=True)),
                ('thank_you_text', wagtail.fields.RichTextField(blank=True)),
                (
                    'coverImage',
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name='+',
                        to='wagtailimages.Image',
                    ),
                ),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='FormField',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'sort_order',
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                (
                    'label',
                    models.CharField(
                        help_text='The label of the form field',
                        max_length=255,
                        verbose_name='label',
                    ),
                ),
                (
                    'field_type',
                    models.CharField(
                        choices=[
                            ('singleline', 'Single line text'),
                            ('multiline', 'Multi-line text'),
                            ('email', 'Email'),
                            ('number', 'Number'),
                            ('url', 'URL'),
                            ('checkbox', 'Checkbox'),
                            ('checkboxes', 'Checkboxes'),
                            ('dropdown', 'Drop down'),
                            ('multiselect', 'Multiple select'),
                            ('radio', 'Radio buttons'),
                            ('date', 'Date'),
                            ('datetime', 'Date/time'),
                            ('hidden', 'Hidden field'),
                        ],
                        max_length=16,
                        verbose_name='field type',
                    ),
                ),
                (
                    'required',
                    models.BooleanField(default=True, verbose_name='required'),
                ),
                (
                    'choices',
                    models.TextField(
                        blank=True,
                        help_text='Comma separated list of choices. Only applicable in checkboxes, radio and dropdown.',
                        verbose_name='choices',
                    ),
                ),
                (
                    'default_value',
                    models.CharField(
                        blank=True,
                        help_text='Default value. Comma separated values supported for checkboxes.',
                        max_length=255,
                        verbose_name='default value',
                    ),
                ),
                (
                    'help_text',
                    models.CharField(
                        blank=True, max_length=255, verbose_name='help text'
                    ),
                ),
                (
                    'page',
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='form_fields',
                        to='birdapp657.FormBirdPage',
                    ),
                ),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
