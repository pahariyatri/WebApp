# Generated by Django 2.2.3 on 2020-03-09 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0003_auto_20200309_0844'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upcoming_destination',
            name='date',
        ),
    ]
