# Generated by Django 3.0.5 on 2020-08-26 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0004_auto_20200827_0011'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(default='', max_length=50),
        ),
    ]
