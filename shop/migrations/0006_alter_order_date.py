# Generated by Django 5.0.1 on 2024-02-06 06:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_rename_image_products_picture_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 2, 6, 10, 24, 50, 589400)),
        ),
    ]
