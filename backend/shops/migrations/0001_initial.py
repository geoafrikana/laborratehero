# Generated by Django 4.1.6 on 2023-02-09 15:29

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('lat', models.DecimalField(decimal_places=2, max_digits=5)),
                ('lon', models.DecimalField(decimal_places=2, max_digits=5)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('geom_m', django.contrib.gis.db.models.fields.PointField(srid=3857)),
            ],
        ),
        migrations.CreateModel(
            name='ZipCodes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ZIP', models.CharField(max_length=6)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=10)),
                ('lon', models.DecimalField(decimal_places=6, max_digits=10)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=3857)),
            ],
        ),
    ]
