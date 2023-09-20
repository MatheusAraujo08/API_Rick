from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.permissions import IsAuthenticated

# Create your views here.

class CharacterAPIView(ModelViewSet):
    queryset= Character.objects.all() #Informa p/ a lib qual as cosultas a serem feitas
    serializer_class=CharacterSerializer #informa o serializer
    filter_backends = [DjangoFilterBackend] #usa a lib do djago-filter
    filterset_fields = ['name', 'status', 'species', 'type']
    permission_classes = (IsAuthenticated,)

class LocationAPIView(ModelViewSet):
    queryset= Location.objects.all() #Informa p/ a lib qual as cosultas a serem feitas
    serializer_class=LocationSerializer #informa o serializer
    filter_backends = [DjangoFilterBackend] #usa a lib do djago-filter
    filterset_fields = ['name', 'type', 'dimension', 'residents']
    permission_classes = (IsAuthenticated,)

class EpisodeAPIView(ModelViewSet):
    queryset= Episode.objects.all() #Informa p/ a lib qual as cosultas a serem feitas
    serializer_class=EpisodeSerializer #informa o serializer
    filter_backends = [DjangoFilterBackend] #usa a lib do djago-filter
    filterset_fields = ['name', 'episode']
    permission_classes = (IsAuthenticated,)