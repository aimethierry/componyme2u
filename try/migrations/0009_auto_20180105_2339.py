# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-05 23:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('try', '0008_auto_20180105_2330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='adress',
        ),
        migrations.RemoveField(
            model_name='client',
            name='name',
        ),
        migrations.AddField(
            model_name='client',
            name='compony',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='try.compony'),
        ),
        migrations.AddField(
            model_name='users',
            name='compony',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='try.compony'),
        ),
        migrations.AlterField(
            model_name='compony',
            name='name',
            field=models.CharField(max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='users',
            name='first_name',
            field=models.CharField(max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='last_name',
            field=models.CharField(max_length=140, null=True),
        ),
    ]