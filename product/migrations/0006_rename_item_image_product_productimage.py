# Generated by Django 4.1.5 on 2023-01-09 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_rename_product_image_product_item_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='item_image',
            new_name='productimage',
        ),
    ]
