# Generated by Django 2.2.1 on 2019-09-03 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('birdapp657', '0013_auto_20190902_0104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='birdpage',
            name='birdbasepage_ptr',
        ),
        migrations.RemoveField(
            model_name='rawbirdpage',
            name='birdbasepage_ptr',
        ),
        migrations.DeleteModel(
            name='BirdBasePage',
        ),
        migrations.DeleteModel(
            name='BirdPage',
        ),
        migrations.DeleteModel(
            name='RawBirdPage',
        ),
    ]