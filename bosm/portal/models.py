# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse


class Event(models.Model):

    EVENT_CHOICES = (
        ('1v1', '1 vs 1'),
        ('athletics', 'Athletics'),
        ('team', 'Team'),
    )

    type = models.CharField(max_length=20, choices=EVENT_CHOICES)
    name = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    description = models.CharField(max_length=1000)
    team_A = models.CharField(max_length=50)
    team_B = models.CharField(max_length=50)
    venue = models.CharField(max_length=50)
    winner = models.CharField(max_length=20,default='none')

    def __str__(self):
        return self.name + str(self.pk)

    def get_absolute_url(self):
        return reverse('portal:detail')


class Results(models.Model):
    name = models.ForeignKey(Event, on_delete=models.CASCADE)
    winner = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse('portal:detail')

    def __str__(self):
        return self.name.name
