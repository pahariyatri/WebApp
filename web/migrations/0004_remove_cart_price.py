# Generated by Django 3.0.8 on 2020-07-06 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20200704_0124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='price',
        ),
    ]
