from django.shortcuts import render
from django.http import HttpResponse
from worker_kursach.func import *

def queryGetConference(request):
    Title = request.GET.get("Title")
    ConfDate = request.GET.get("ConfDate")
    ConfTag = request.GET.get("ConfTag")

    conference = getConf(Title, ConfDate, ConfTag)

    return HttpResponse((f"ID: {cf.id} | Название:{cf.Title}, Тема: {cf.ConfTag}, Дата: {cf.ConfDate}<br>" for cf in conference) if len(conference) else f"Конференция не найдена в бд")

def querySetConference(request):
    Title = request.GET.get("Title")
    ConfDate = request.GET.get("ConfDate")
    ConfTag = request.GET.get("ConfTag")

    conference = addConf(Title, ConfDate, ConfTag)

    return HttpResponse(
        (f"ID: {conference.id} | Название:{conference.Title}, Тема: {conference.ConfTag}, Дата: {conference.ConfDate}<br> Успешно добавлена запись"))

