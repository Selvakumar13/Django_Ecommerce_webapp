# Generated by Django 4.2.2 on 2023-07-13 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_product_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='customer',
        ),
    ]
