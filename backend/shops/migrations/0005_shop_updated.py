# Generated by Django 4.1.6 on 2023-02-13 08:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shops", "0004_alter_shop_business_phone"),
    ]

    operations = [
        migrations.AddField(
            model_name="shop",
            name="updated",
            field=models.DateField(auto_now=True),
        ),
    ]
