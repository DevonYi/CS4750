# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 18:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_doctor'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Doctor',
        ),
    ]
