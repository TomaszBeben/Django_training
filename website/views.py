from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

from meetings.models import Meetings, Room

def welcome(req):
    return render(req, 'website/welcome.html',
                    {
                        'num_meetings': Meetings.objects.count(),
                        'meetings_all': Meetings.objects.all(),
                        'num_rooms': Room.objects.count()
                    }
                    )

def date(req):
    return HttpResponse('Page was served at: ' + str(datetime.now()))

def about(req):
    return HttpResponse('YO! this is only django traning, keep going...')

def rooms(req):
    return render(req, 'website/rooms.html',
                  {
                      'num_rooms': Room.objects.count(),
                      'rooms_all': Meetings.objects.all(),
                  }
                  )