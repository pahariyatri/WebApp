# Generated by Django 3.0.8 on 2020-07-03 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='price',
            field=models.ManyToManyField(to='web.Price'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='portfolio_site',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
    ]
