from .models import *
from django.db import connection

def addConf(Title, ConfDate, ConfTag):
    conference = Conference(Title=Title, ConfDate=ConfDate, ConfTag=ConfTag)
    conference.save()
    return conference

def getConf(Title, ConfDate, ConfTag):
        try:
            conference = Conference.objects.filter( Title__icontains=Title) & Conference.objects.filter( ConfDate__icontains=ConfDate) & Conference.objects.filter( ConfTag__icontains=ConfTag)
        except Conference.DoesNotExist:
            conference = None

        return conference
