# Generated by Django 4.1.5 on 2023-01-09 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_rename_image_product_product_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_image',
            new_name='image',
        ),
    ]