# Generated by Django 2.2.3 on 2020-05-23 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0006_auto_20200523_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destinations',
            name='categories',
            field=models.CharField(choices=[('ADVENTURE', 'ADVENTURE'), ('SOLO', 'SOLO'), ('GROUP', 'GROUP'), ('RELIGOUS', 'RELIGOUS'), ('WATER_ACTIVITIES', 'WATER_ACTIVITIES'), ('NATURE', 'NATURE'), ('FAMILY', 'FAMILY'), ('ROMANTIC', 'ROMANTIC')], max_length=30),
        ),
    ]
