# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-19 18:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hUid', models.IntegerField()),
                ('hName', models.IntegerField()),
                ('hStreetAddress', models.IntegerField()),
                ('hCapacity', models.IntegerField()),
                ('hZipcode', models.IntegerField()),
                ('hStateCode', models.IntegerField()),
            ],
        ),
    ]
