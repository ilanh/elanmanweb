# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 18:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('extender', '0003_configsectionobject_roletaskobject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roletaskobject',
            name='exid',
        ),
        migrations.RemoveField(
            model_name='roletaskobject',
            name='listobject',
        ),
        migrations.AddField(
            model_name='roletaskobject',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='extender.RoleObject'),
        ),
    ]
