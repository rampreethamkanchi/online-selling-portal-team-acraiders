# Generated by Django 5.0.3 on 2024-03-23 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_alter_order_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='city',
        ),
    ]