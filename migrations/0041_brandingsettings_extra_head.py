# Generated by Django 2.2.9 on 2020-01-24 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birdapp657', '0040_auto_20191225_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='brandingsettings',
            name='extra_head',
            field=models.TextField(blank=True, null=True),
        ),
    ]
