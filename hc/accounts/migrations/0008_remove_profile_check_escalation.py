# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-06 12:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_profile_check_escalation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='check_escalation',
        ),
    ]
