# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-01 16:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScrapeData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_added_to_db', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_issued', models.CharField(default='', max_length=255)),
                ('finaled_date', models.CharField(default='', max_length=255)),
                ('address', models.CharField(default='', max_length=1000)),
                ('description', models.CharField(default='', max_length=1000)),
                ('permit_number', models.CharField(default='', max_length=255)),
                ('permit_type', models.CharField(default='', max_length=1000)),
                ('valuation', models.CharField(default='', max_length=255)),
                ('fees', models.CharField(default='', max_length=255)),
                ('contractor', models.CharField(default='', max_length=1000)),
                ('status', models.CharField(default='', max_length=255)),
                ('parcel_number', models.CharField(default='', max_length=255)),
                ('owner', models.CharField(default='', max_length=1000)),
            ],
        ),
    ]
