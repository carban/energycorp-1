# Generated by Django 3.0.3 on 2020-05-21 11:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0019_auto_20200520_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='deadDatePay',
            field=models.DateField(default=datetime.datetime(2020, 5, 31, 11, 39, 8, 93838)),
        ),
    ]
