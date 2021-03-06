# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-21 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meds_name', models.CharField(max_length=100)),
                ('meds_price', models.FloatField(max_length=10)),
                ('meds_image', models.CharField(max_length=100)),
                ('meds_overview', models.CharField(max_length=1000)),
                ('meds_description', models.CharField(max_length=500)),
                ('meds_direction', models.CharField(max_length=1000)),
                ('meds_ingredient', models.CharField(max_length=1000)),
                ('meds_indication', models.CharField(max_length=1000)),
                ('meds_caution', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Supplement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supp_name', models.CharField(max_length=100)),
                ('supp_price', models.FloatField(max_length=10)),
                ('supp_image', models.CharField(max_length=100)),
                ('supp_overview', models.CharField(max_length=1000)),
                ('supp_description', models.CharField(max_length=500)),
                ('supp_direction', models.CharField(max_length=1000)),
                ('supp_ingredient', models.CharField(max_length=1000)),
                ('supp_indication', models.CharField(max_length=1000)),
                ('supp_caution', models.CharField(max_length=1000)),
            ],
        ),
    ]
