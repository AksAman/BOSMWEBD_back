# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 10:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='Winner',
            field=models.CharField(choices=[(models.CharField(max_length=50), models.CharField(max_length=50)), (models.CharField(max_length=50), models.CharField(max_length=50)), ('tie', 'Tie')], default='None', max_length=30),
        ),
    ]