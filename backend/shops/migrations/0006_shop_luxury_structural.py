# Generated by Django 4.1.6 on 2023-02-13 17:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shops", "0005_shop_updated"),
    ]

    operations = [
        migrations.AddField(
            model_name="shop",
            name="luxury_structural",
            field=models.IntegerField(default="60"),
            preserve_default=False,
        ),
    ]