# Generated by Django 4.0.5 on 2022-07-13 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Stock_status',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='gender',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]