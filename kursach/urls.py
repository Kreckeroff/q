from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('getConf', views.queryGetConference),
    path('addConf', views.querySetConference),
]