# Generated by Django 5.0.3 on 2024-03-31 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_address_options_category_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='customer_message',
            field=models.TextField(blank=True, default='no message'),
        ),
        migrations.AlterField(
            model_name='request',
            name='seller_message',
            field=models.TextField(blank=True, default='no message'),
        ),
    ]
