# Generated by Django 4.1.5 on 2023-04-04 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0026_category_status_category_trending_product_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.CharField(max_length=200),
        ),
    ]
