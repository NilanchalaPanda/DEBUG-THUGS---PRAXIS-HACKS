# Generated by Django 4.1.7 on 2023-03-03 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_product_prodcut_quantity_product_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prodcut_quantity',
            field=models.SmallIntegerField(default=0),
        ),
    ]
