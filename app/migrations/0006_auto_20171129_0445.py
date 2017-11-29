# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='pSSN',
            field=models.IntegerField(max_length=9),
        ),
        migrations.AlterField(
            model_name='patient',
            name='pUid',
            field=models.IntegerField(max_length=15),
        ),
    ]
