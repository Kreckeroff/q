from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
#from worker_kursach.models import Conference
from .models import Conference, AddConference
from .seriaalizers import ConfSerializer
from worker_kursach.func import getConf, addConf
from drf_spectacular.utils import extend_schema

# Create your views here.
class ConfView(APIView):
    @extend_schema(request=ConfSerializer, responses=ConfSerializer)

    def get(self, request, Title, ConfDate, ConfTag):
        conf = Conference(Title, ConfDate, ConfTag)

        serializer_for_request = ConfSerializer(instance=conf)

        return Response(serializer_for_request.data)

class AddConfView(APIView):
    @extend_schema(request=ConfSerializer, responses=ConfSerializer)
    def get(self, request, Title, ConfDate, ConfTag):
        conf = AddConference(Title, ConfDate, ConfTag)

        conf = addConf(Title,ConfDate, ConfTag)
        serializer_for_request = ConfSerializer(instance=conf)

        return Response(serializer_for_request.data)
class getConfView(APIView):
    @extend_schema(request=ConfSerializer, responses=ConfSerializer)

    def get(self, request, Title, ConfDate, ConfTag):
        a = getConf(Title, ConfDate, ConfTag)
        a = (ConfSerializer(instance=st).data for st in a)if a is not None else[]
        return Response(a)
