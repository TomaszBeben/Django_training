from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

def welcome(req):
    return HttpResponse('Welcome to the Meeting Planner!')

def date(req):
    return HttpResponse('Page was served at: ' + str(datetime.now()))