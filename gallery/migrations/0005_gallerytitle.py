# Generated by Django 5.0 on 2024-05-02 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_remove_gallerytwo_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
            ],
        ),
    ]
