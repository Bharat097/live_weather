# Generated by Django 3.0.7 on 2020-07-05 13:36

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('loc', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
    ]
