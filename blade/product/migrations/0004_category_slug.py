# Generated by Django 5.1.4 on 2025-01-08 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_productimage_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='default_slug', unique=True),
            preserve_default=False,
        ),
    ]
