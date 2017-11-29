# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('pUid', models.CharField(max_length=15)),
                ('pName', models.CharField(max_length=50)),
                ('pHealthCare', models.CharField(max_length=50)),
                ('pSSN', models.CharField(max_length=9)),
                ('pAllergies', models.CharField(max_length=200)),
            ],
        ),
    ]
