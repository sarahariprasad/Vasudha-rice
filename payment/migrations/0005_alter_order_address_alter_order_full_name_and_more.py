# Generated by Django 5.0 on 2024-08-14 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_order_city_order_full_name_order_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.TextField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='order',
            name='full_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='post_code',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(default='', max_length=30),
        ),
    ]