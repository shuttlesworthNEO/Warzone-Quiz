# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-08 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]