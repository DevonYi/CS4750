# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_delete_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('dUid', models.IntegerField(primary_key=True, serialize=False)),
                ('dName', models.CharField(help_text='name', max_length=20)),
                ('dPractice', models.CharField(help_text='practice', max_length=20)),
            ],
        ),
    ]
