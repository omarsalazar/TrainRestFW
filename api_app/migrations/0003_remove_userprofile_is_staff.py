# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-20 00:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0002_auto_20180220_0034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='is_staff',
        ),
    ]
