# Generated by Django 3.0.3 on 2020-05-21 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200518_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='interes_mora',
        ),
    ]
