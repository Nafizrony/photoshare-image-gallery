# Generated by Django 4.2 on 2023-06-09 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='gallery',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True),
        ),
    ]
