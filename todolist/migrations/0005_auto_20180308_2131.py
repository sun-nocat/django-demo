# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-08 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0004_auto_20171211_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='flag',
            field=models.CharField(max_length=2),
        ),
    ]
