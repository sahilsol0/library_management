# Generated by Django 5.0.2 on 2024-04-21 01:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0025_alter_book_added_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(default='author', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='added_date',
            field=models.DateField(default=datetime.date(2024, 4, 21)),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='category or genre', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.CharField(default='publisher name', max_length=100, unique=True),
        ),
    ]