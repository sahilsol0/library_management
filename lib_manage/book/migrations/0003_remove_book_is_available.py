# Generated by Django 5.0.2 on 2024-03-12 01:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_category_book_isbn_book_added_date_book_count_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='is_available',
        ),
    ]
