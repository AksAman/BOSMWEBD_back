# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 10:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_remove_event_winner'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='winner',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
    ]
