# Generated by Django 5.0.3 on 2024-03-14 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_alter_product_age_alter_product_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_sale',
            field=models.BooleanField(default=True),
        ),
    ]