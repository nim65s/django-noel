# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChristmasGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rotation', models.CommaSeparatedIntegerField(max_length=256, default='')),
                ('group', models.ForeignKey(unique=True, to='auth.Group')),
            ],
        ),
    ]
