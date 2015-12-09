# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secret_santa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='christmasgroup',
            name='closed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='christmasgroup',
            name='rotation',
            field=models.CommaSeparatedIntegerField(default='', blank=True, max_length=256),
        ),
    ]
