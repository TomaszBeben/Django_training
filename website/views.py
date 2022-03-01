from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

from meetings.models import Meetings

def welcome(req):
    return render(req, 'website/welcome.html',
                  {'num_meetings': Meetings.objects.count()})

def date(req):
    return HttpResponse('Page was served at: ' + str(datetime.now()))

def about(req):
    return HttpResponse('YO! this is only django traning, keep going...')