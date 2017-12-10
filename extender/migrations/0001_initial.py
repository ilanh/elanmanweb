# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-10 19:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortname', models.CharField(max_length=32)),
                ('desc', models.CharField(max_length=64, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ApiSectionObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortname', models.CharField(max_length=32)),
                ('exid', models.CharField(max_length=8, null=True)),
                ('desc', models.CharField(max_length=64, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('api', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='extender.ApiObject')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ApiSubObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortname', models.CharField(max_length=32)),
                ('exid', models.CharField(max_length=8, null=True)),
                ('desc', models.CharField(max_length=64, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='extender.ApiSectionObject')),
            ],
        ),
        migrations.CreateModel(
            name='ApiValueObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exid', models.CharField(max_length=8, null=True)),
                ('value', models.CharField(max_length=256, null=True)),
                ('desc', models.CharField(max_length=64, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('subobject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='extender.ApiSubObject')),
            ],
        ),
        migrations.CreateModel(
            name='ConfigSectionObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortname', models.CharField(max_length=32)),
                ('exid', models.CharField(max_length=8, null=True)),
                ('desc', models.CharField(max_length=64, null=True)),
                ('listobject', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ConfigSubObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortname', models.CharField(max_length=32)),
                ('exid', models.CharField(max_length=8, null=True)),
                ('desc', models.CharField(max_length=64, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='extender.ConfigSectionObject')),
            ],
        ),
        migrations.CreateModel(
            name='ConfigValueObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exid', models.CharField(max_length=8, null=True)),
                ('value', models.CharField(max_length=256, null=True)),
                ('desc', models.CharField(max_length=64, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('subobject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='extender.ConfigSubObject')),
            ],
        ),
        migrations.CreateModel(
            name='LogicalGroupObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortname', models.CharField(max_length=32)),
                ('exid', models.CharField(max_length=8, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RoleObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortname', models.CharField(max_length=32)),
                ('exid', models.CharField(max_length=8, null=True)),
                ('desc', models.CharField(max_length=64, null=True)),
                ('addon', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RoleTaskObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortname', models.CharField(max_length=32)),
                ('desc', models.CharField(max_length=64, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='extender.RoleObject')),
            ],
        ),
        migrations.CreateModel(
            name='RoleTemplateObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortname', models.CharField(max_length=32)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('desc', models.CharField(max_length=64, null=True)),
                ('istemplate', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='extender.RoleObject')),
            ],
        ),
    ]
