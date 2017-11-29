# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20171129_0445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='pSSN',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='patient',
            name='pUid',
            field=models.IntegerField(),
        ),
    ]
