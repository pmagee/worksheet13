# Generated by Django 2.2.5 on 2019-10-24 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='category',
            name='products',
            field=models.ManyToManyField(to='shop.Product'),
        ),
    ]
