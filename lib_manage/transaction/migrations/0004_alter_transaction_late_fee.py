# Generated by Django 5.0.2 on 2024-04-05 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0003_alter_transaction_late_fee_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='late_fee',
            field=models.IntegerField(null=True),
        ),
    ]