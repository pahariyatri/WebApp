# Generated by Django 2.2.3 on 2020-03-22 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destinations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('price', models.IntegerField()),
                ('detail', models.CharField(blank=True, max_length=1000)),
                ('level', models.CharField(choices=[('Easy', 'Easy'), ('Moderate', 'Moderate'), ('Difficult', 'Difficult')], max_length=30)),
                ('day', models.IntegerField()),
                ('night', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Home_background',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_large', models.CharField(max_length=15)),
                ('text_small', models.CharField(max_length=25)),
                ('background_image', models.ImageField(upload_to='pics')),
            ],
        ),
        migrations.CreateModel(
            name='Popular_destinations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('price', models.IntegerField()),
                ('detail', models.CharField(blank=True, max_length=1000)),
                ('type', models.CharField(choices=[('a', 'Advan'), ('w', 'WildLife'), ('f', 'Widthfrandes'), ('s', 'solo')], max_length=30)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Special_offers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='pics')),
            ],
        ),
        migrations.CreateModel(
            name='Thought',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000)),
            ],
        ),
    ]
