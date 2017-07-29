# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, View
from .models import Event,Results
from .forms import EventForm,WinnerForm
# Create your views here.


def index(request):
    return render(request, 'portal/index.html')


def eveRegister(request):
    return render(request, 'portal/register.html')


class EventCreate(CreateView):
    form_class=EventForm
    model = Event


def detail(request):
    event_details=Event.objects.all()
    return render(request,'portal/details.html',{'event_details':event_details})


class Result(CreateView):
    model = Results
    template_name = 'portal/result.html'
    form_class = WinnerForm
