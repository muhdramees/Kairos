# Generated by Django 4.1.5 on 2023-03-24 04:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0020_productoffer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_id',
            field=models.CharField(default=0, max_length=250),
        ),
        migrations.AlterField(
            model_name='productoffer',
            name='product_name',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.product'),
            preserve_default=False,
        ),
    ]