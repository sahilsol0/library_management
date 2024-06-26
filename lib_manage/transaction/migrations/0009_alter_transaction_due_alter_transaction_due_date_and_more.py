# Generated by Django 5.0.2 on 2024-04-09 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0008_alter_transaction_returned_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='due',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='returned_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
