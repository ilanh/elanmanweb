# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-14 12:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extender', '0003_auto_20171211_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='apisubobject',
            name='trailngspace',
            field=models.BooleanField(default=False),
        ),
    ]
