# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 05:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='accounttype',
            options={'ordering': ['type']},
        ),
    ]
