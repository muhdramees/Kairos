# Generated by Django 4.1.5 on 2023-01-07 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_emailuser_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailuser',
            name='username',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
