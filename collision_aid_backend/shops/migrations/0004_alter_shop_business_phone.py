# Generated by Django 4.1.6 on 2023-02-12 06:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shops", "0003_rename_name_shop_business_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shop",
            name="business_phone",
            field=models.CharField(max_length=20),
        ),
    ]
