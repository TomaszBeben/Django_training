from django.shortcuts import render, get_object_or_404

from .models import Meetings

def detail(req, id):
    meeting = get_object_or_404(Meetings, pk = id)
    return render(req, 'meetings/detail.html', {'meeting': meeting})