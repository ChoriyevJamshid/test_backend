# Generated by Django 4.2.7 on 2024-04-27 12:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_alter_product_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productmaterial",
            name="quantity",
            field=models.FloatField(),
        ),
    ]
