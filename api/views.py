from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
#from worker_kursach.models import Conference
from .seriaalizers import ConfSerializer
from worker_kursach.func import getConf, addConf
from drf_spectacular.utils import extend_schema

# Create your views here.
class getConfView(APIView):
    @extend_schema(request=ConfSerializer, responses=ConfSerializer)
    def get(self, request, Title, ConfDate, ConfTag):
        conference = getConf(Title, ConfDate, ConfTag)
        print(conference)
        conference = (ConfSerializer(instance=st).data for st in conference) if conference is not None else []

        return Response(conference)

class AddConfView(APIView):
    @extend_schema(request=ConfSerializer, responses=ConfSerializer)
    def get(self, request, Title, ConfDate, ConfTag):
        conference = addConf(Title, ConfDate, ConfTag)
        return Response(conference)