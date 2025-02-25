# Generated by Django 5.1.6 on 2025-02-13 09:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50, unique=True)),
                ('product_slug', models.SlugField(blank=True, null=True, unique=True)),
                ('product_description', models.TextField(blank=True, max_length=1000)),
                ('price', models.IntegerField(default=0)),
                ('product_images', models.ImageField(upload_to='photos/products')),
                ('stock', models.IntegerField(default=0)),
                ('is_available', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Category.category')),
            ],
        ),
    ]
