from django.shortcuts import render
from django.http import HttpResponse
from worker_kursach.func import *


def queryGetConference(request):
    Title = request.GET.get("Title")
    ConfDate = request.GET.get("ConfDate")
    ConfTag = request.GET.get("ConfTag")
    conference = getConf(Title, ConfDate, ConfTag)
    print(conference)
    return HttpResponse(
        (f"ID Конференции: {obj['id']} - Конференция: {obj['Title']}, дата конференции: {obj['ConfDate']}, тег конференции: {obj['ConfTag']}<br>" for obj in conference)
        if len(conference) else f"Конференции не существует в базе")

def querySetConference(request):
    Title = request.GET.get("Title")
    ConfDate = request.GET.get("ConfDate")
    ConfTag = request.GET.get("ConfTag")
    conference = getConf(Title, ConfDate, ConfTag)
    return HttpResponse(
        (f"ID Конференции: {conference['id']} - Название: {conference['Title']}, дата конференции: {conference['ConfDate']}, "
         f"тег конференции: {conference['ConfTag']}<br>"))