# Generated by Django 3.2.9 on 2021-12-06 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20211205_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=60, verbose_name='Category Slug'),
        ),
    ]
