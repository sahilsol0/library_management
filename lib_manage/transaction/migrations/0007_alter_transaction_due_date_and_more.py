# Generated by Django 5.0.2 on 2024-04-07 09:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0006_alter_transaction_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='due_date',
            field=models.DateField(default=datetime.date(2024, 1, 1), null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='returned_date',
            field=models.DateField(default=datetime.date(2024, 1, 1), null=True),
        ),
    ]
