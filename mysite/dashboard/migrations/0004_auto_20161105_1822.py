# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-05 18:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20161105_1814'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='activity',
            new_name='activityfeed',
        ),
        migrations.RenameField(
            model_name='journalentry',
            old_name='journal_entry',
            new_name='journalentrylist',
        ),
        migrations.RenameField(
            model_name='reward',
            old_name='reward',
            new_name='rewardfeed',
        ),
    ]
