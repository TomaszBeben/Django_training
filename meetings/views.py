from django.shortcuts import render, get_object_or_404
from django.forms import modelform_factory

from .models import Meetings, Room

def detail(req, id):
    meeting = get_object_or_404(Meetings, pk = id)
    return render(req, 'meetings/detail.html', {'meeting': meeting})

def rooms_list(req):
    return render(req, 'meetings/rooms_list.html', {'rooms': Room.objects.all()})

MeetingForm = modelform_factory(Meetings, exclude=[])

def new(req):
    form  = MeetingForm()
    return render(req, 'meetings/new.html', {'form': form})