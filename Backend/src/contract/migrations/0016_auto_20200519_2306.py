# Generated by Django 3.0.3 on 2020-05-19 23:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0015_auto_20200519_2238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='mora',
        ),
        migrations.AddField(
            model_name='invoice',
            name='interestMora',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='invoice',
            name='totalMora',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='deadDatePay',
            field=models.DateField(default=datetime.datetime(2020, 5, 29, 23, 6, 52, 94902)),
        ),
    ]
