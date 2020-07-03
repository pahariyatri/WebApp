# Generated by Django 2.2.3 on 2020-07-02 11:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0004_auto_20200702_1005'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(max_length=100)),
                ('apartment_address', models.CharField(max_length=100)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('zip', models.CharField(max_length=100)),
                ('address_type', models.CharField(choices=[('H', 'Home'), ('O', 'Office')], max_length=1)),
                ('default', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('tagline', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('img', models.ImageField(upload_to='')),
                ('price', models.IntegerField()),
                ('location', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=5000)),
                ('duration', models.CharField(choices=[('3', '1 to 3'), ('5', '4 to 5'), ('7', '6 to 7'), ('10', 'more then week')], max_length=50)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_code', models.CharField(blank=True, max_length=20, null=True)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('ordered_date', models.DateTimeField()),
                ('ordered', models.BooleanField(default=False)),
                ('refund_requested', models.BooleanField(default=False)),
                ('refund_granted', models.BooleanField(default=False)),
                ('billing_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='billing_address', to='web.Address')),
                ('coupon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='web.Coupon')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('quantity', models.IntegerField(default=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='destinationbooking',
            name='destination',
        ),
        migrations.RemoveField(
            model_name='destinationbooking',
            name='user',
        ),
        migrations.AlterField(
            model_name='refund',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Order'),
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.DeleteModel(
            name='DestinationBooking',
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='web.OrderItem'),
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='web.Payment'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
