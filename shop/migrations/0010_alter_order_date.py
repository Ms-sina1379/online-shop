# Generated by Django 5.0.1 on 2024-02-14 06:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 2, 14, 9, 54, 35, 123763)),
        ),
    ]