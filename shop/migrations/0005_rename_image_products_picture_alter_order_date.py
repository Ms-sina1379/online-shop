# Generated by Django 5.0.1 on 2024-02-06 06:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_order_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='image',
            new_name='picture',
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 2, 6, 10, 22, 36, 41966)),
        ),
    ]
