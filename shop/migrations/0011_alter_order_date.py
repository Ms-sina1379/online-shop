# Generated by Django 5.0.1 on 2024-02-14 06:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 2, 14, 9, 55, 49, 412077)),
        ),
    ]
