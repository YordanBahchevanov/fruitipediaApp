# Generated by Django 4.2.4 on 2024-01-13 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fruits', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fruit',
            old_name='Image_url',
            new_name='image_url',
        ),
    ]
