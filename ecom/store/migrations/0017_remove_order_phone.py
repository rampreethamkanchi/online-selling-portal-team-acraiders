# Generated by Django 5.0.3 on 2024-03-17 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_order_cost_alter_order_phone_alter_product_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='phone',
        ),
    ]
