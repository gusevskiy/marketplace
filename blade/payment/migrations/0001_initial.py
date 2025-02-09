# Generated by Django 5.1.4 on 2025-02-08 12:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0002_alter_orderitem_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_id', models.CharField(max_length=100, unique=True)),
                ('status', models.CharField(default='pending', max_length=20)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
            ],
        ),
    ]
