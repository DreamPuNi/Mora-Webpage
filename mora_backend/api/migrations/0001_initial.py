# Generated by Django 5.1.4 on 2025-01-15 10:30

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('cover', models.ImageField(upload_to='images/books-cover')),
                ('description', models.TextField()),
                ('review', models.TextField()),
                ('link', models.URLField()),
                ('tag', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Books',
            },
        ),
        migrations.CreateModel(
            name='CurrencyRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True)),
                ('rate', models.DecimalField(decimal_places=4, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('data', models.ImageField(upload_to=api.models.upload_to_dynamic)),
                ('introduce', models.TextField()),
                ('upload_folder', models.CharField(default='xinpo', max_length=255)),
            ],
            options={
                'db_table': 'Images',
            },
        ),
    ]
