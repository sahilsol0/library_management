# Generated by Django 5.0.2 on 2024-04-10 01:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0010_alter_transaction_issued_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='issued_date',
            field=models.DateField(default=datetime.datetime(2024, 4, 10, 7, 17, 4, 899547)),
        ),
    ]
