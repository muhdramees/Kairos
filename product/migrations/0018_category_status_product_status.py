# Generated by Django 4.1.3 on 2023-03-21 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_remove_category_status_remove_product_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='status',
            field=models.BooleanField(default=False, help_text='0=default, 1=Hidden'),
        ),
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.BooleanField(default=False, help_text='0=default, 1=Hidden'),
        ),
    ]
