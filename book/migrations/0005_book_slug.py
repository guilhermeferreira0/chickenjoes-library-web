# Generated by Django 5.0.6 on 2024-05-30 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_book_image_delete_bookimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
