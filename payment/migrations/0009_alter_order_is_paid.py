# Generated by Django 5.0 on 2024-08-17 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0008_alter_order_is_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
    ]