# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-11 11:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_auto_20171205_1947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='priority',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='username',
        ),
        migrations.AddField(
            model_name='todo',
            name='tag',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='flag',
            field=models.CharField(default='0', max_length=2),
        ),
    ]