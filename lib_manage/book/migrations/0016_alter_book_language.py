# Generated by Django 5.0.2 on 2024-03-12 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0015_book_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
