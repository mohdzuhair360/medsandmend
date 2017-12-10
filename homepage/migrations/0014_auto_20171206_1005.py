# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-06 02:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0013_searchitem_store_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_location', models.CharField(max_length=10000)),
            ],
        ),
        migrations.RemoveField(
            model_name='searchitem',
            name='store_location',
        ),
    ]